import shutil
import argparse
import json
import re

from src.llm import LLM
from src.compiler import Compiler


with open("templlmos.json", "r") as read_file:
    data = json.load(read_file)

llm = LLM(data["models"])

print("Avaialble models:")
print(llm.runtime_models.keys())


def process_output(output, single_group = True):
    groups = re.findall(r"```\S{0,}\n(.*?)```", output, re.DOTALL)

    if single_group:
        return groups[0]
    else:
        result = ""
        for group in groups:
            result += group + "\n"
        return result


with open("test.txt", "r") as read_file:
    data = read_file.read()
    result = llm.call_llm("deepseek-coder-6.7b-instruct.Q5_K_M.gguf", data, include_stop=False)

    print(process_output(result, single_group=False))

