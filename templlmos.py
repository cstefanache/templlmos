import shutil
import argparse
import json
import re

from src.llm import LLM
from src.compiler import Compiler


parser = argparse.ArgumentParser()
parser.add_argument("--serve", action="store_true", help="Serve the application")
parser.add_argument("--descriptor", default="templlmos.json", help="Descriptor file")
parser.add_argument("--recompile", action="store_true", help="Force build")
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


def rebuild():
    html_content = compiler.build()
    output_filename = re.sub(r"\.json", ".html", descriptor)
    with open(output_filename, "w") as file:
        file.write(html_content)

# if args.serve:
#     serve()


rebuild()