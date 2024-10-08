import shutil
import argparse
import json
import time
import re

from src.llm import LLM
from src.compiler import Compiler

from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

parser = argparse.ArgumentParser()
parser.add_argument("--serve", action="store_true", help="Serve the application")
parser.add_argument("--descriptor", default="templlmos.json", help="Descriptor file")
parser.add_argument("--recompile", action="store_true", help="Force build")
parser.add_argument("--listen", action="store_true", help="Listen for changes")
args = parser.parse_args()

descriptor = args.descriptor
with open(descriptor, "r") as read_file:
    data = json.load(read_file)

llm = LLM(data["models"])

print("Avaialble models:")
print(llm.runtime_models.keys())

recompile = args.recompile

if recompile:
    shutil.rmtree("./cache")
    shutil.rmtree("./debug")

compiler = Compiler(llm, data, recompile)


def rebuild(update_response=None):
    html_content = compiler.build(update_response=update_response)
    output_filename = re.sub(r"\.json", ".html", descriptor)
    with open(output_filename, "w") as file:
        file.write(html_content)


response = "Output panel\n-------------------------------\n"


def update_response(x):
    global response
    response += x


class Server(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response = ""

    def log_message(self, format, *args):
        return

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header(
            "Access-Control-Allow-Headers", "X-Requested-With, Content-type"
        )
        self.end_headers()

    def do_GET(self):
        if self.path == "/ping":
            self.send_response(200)
            self.send_header("Content-type", "application/text")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes("pong", "utf-8"))
        elif self.path == "/output":
            self.send_response(200)
            self.send_header("Content-type", "application/text")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes(response, "utf-8"))
        else:
            self.serve_compiled()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        global response

        output = ""

        post_data = self.rfile.read(content_length).decode("utf-8")
        json_data = json.loads(post_data)
        # model = json_data["model"]
        instructions = json_data["instruction"]

        dependencies = re.findall(r"^#include:? (\w+)", instructions, re.MULTILINE)
        instruction = re.sub(r"^#include:? \w+", "", instructions, flags=re.MULTILINE)
        response = ""
        print("Dependencies: ", dependencies)
        compiled_dependencies = ""
        for dependency in dependencies:
            try:
                compiled_dependencies += compiler.api[dependency] + "\n"
            except KeyError:
                print(f"Dependency not found: {dependency}")

        for instruction in instructions.split("---"):
            update_response(instruction + "\n" + "-------------------------------" + "\n")
            result = compiler.llm.call_default_llm(
                instruction,
                dependencies=compiled_dependencies,
                update_fn=update_response,
                with_cache=True,
            )
            if json_data.get("full", False) is False:
                output += compiler.process_output(result)
            compiled_dependencies += compiler.get_api(result)

        self.send_response(200)
        self.send_header("Content-type", "application/text")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(bytes("(() => {\n" + output + "\n})()", "utf-8"))

    def serve_compiled(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        with open("templlmos.html", "r") as file:
            self.wfile.write(bytes(file.read(), "utf-16"))


class OSSourcesHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if (
            event.src_path.endswith(".json")
            and "cache" not in event.src_path
            and "debug" not in event.src_path
        ):
            print("OS source file changed, recompiling...", event.src_path)
            try:
                global response
                response = "Recompiling ..."
                start_time = time.time()
                rebuild(update_response)
                response += f"\nCompleted in {time.time() - start_time} seconds.\n"
            except Exception as e:
                print(f"Error recompiling: {e}")


if __name__ == "__main__":
    rebuild()
    if args.listen:
        event_handler = OSSourcesHandler()
        observer = Observer()
        observer.schedule(event_handler, path=".", recursive=True)
        observer.start()

        if not args.serve:
            try:
                while True:
                    pass
            except KeyboardInterrupt:
                observer.stop()
                observer.join()

    if args.serve:
        server = ThreadingHTTPServer(("0.0.0.0", 8080), Server)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

        server.server_close()
        print("Server stopped.")
