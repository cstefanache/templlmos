from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import BaseServer
from compiler import Compiler
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

hostName = "localhost"
serverPort = 8080

compiler = Compiler("templlmos.json", force_build=False)


class TempLLMOS(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/ping":
            self.send_response(200)
            self.end_headers()
        else:
            self.serve_compiled()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        json_data = json.loads(post_data)
        model = json_data["model"]
        instruction = json_data["instruction"]
        result = compiler.call_llm(model, instruction)
        result = compiler.process_output(result)
        self.send_response(200)
        self.send_header("Content-type", "application/text")
        self.end_headers()
        self.wfile.write(bytes(result, "utf-8"))

    def serve_compiled(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("templlmos.html", "r") as file:
            self.wfile.write(bytes(file.read(), "utf-16"))


class OSSourcesHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Event type: {event.event_type}  path : {event.src_path}")
        print(
            event.src_path.endswith(".json"),
            "cache" not in event.src_path,
            "debug" not in event.src_path,
        )
        if (
            event.src_path.endswith(".json")
            and "cache" not in event.src_path
            and "debug" not in event.src_path
        ):
            print("OS source file changed, recompiling...", event.src_path)
            try:
                compiler.run_compile()
            except Exception as e:
                print(f"Error recompiling: {e}")


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), TempLLMOS)
    print("Server started http://%s:%s" % (hostName, serverPort))

    event_handler = OSSourcesHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
