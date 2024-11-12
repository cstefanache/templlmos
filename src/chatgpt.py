import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()  # take environment variables from .env.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


class ChatGPT:
    def __init__(self):
        pass

    def get_dependencies(self, dependencies):
        if len(dependencies.strip()) == 0:
            return ""
        
        return f"""
Given the following implemented functions:
{dependencies}
"""

    def get_system_message(self, to, tag, isLibrary=False):
        system_prompt = ""
        if tag == "style":
            system_prompt = "You are a code generator that produces CSS code exclusively. When responding to queries, provide only valid and complete CSS code without any additional explanations or comments. Do not include any HTML, JavaScript, or commentary unless explicitly asked to. Follow best practices for CSS and ensure compatibility across modern browsers."
        elif tag == "script":
            system_prompt = "You are a code generator that produces JavaScript code exclusively using vanilla JavaScript that will execute in a browser window. When responding to queries, provide only valid and complete JavaScript code without any additional explanations or comments. Do not include any frameworks or libraries such as jQuery, React, or others. Follow best practices for vanilla JavaScript and ensure compatibility with modern browsers. Do not write node or server-side code."
            if isLibrary == True:
                system_prompt += ". For each function, provide a brief description of its purpose in jsdoc format."
        elif to[0] == "body":
            system_prompt = "You are a code generator that produces the specified DOM element exclusively. When responding to queries, provide only valid and complete HTML code without any additional explanations or comments. Do not include any CSS, JavaScript, or commentary unless explicitly asked to. Follow best practices for HTML and ensure compatibility across modern browsers."
        return system_prompt

    def get_instruction(self, instruction, dependencies, to, tag, isLibrary=False):
        system_prompt = self.get_system_message(to, tag, isLibrary)
        compiled_instruction = f"""
{system_prompt}
{self.get_dependencies(dependencies)}
{instruction}
"""
        return compiled_instruction

    def execute(self, instruction, dependencies, to, tag, isLibrary=False, max_tokens = 2048):
        messages = [
            {
                "role": "system",
                "content": self.get_instruction(instruction, dependencies, to, tag, isLibrary=isLibrary),
            }
        ]

        if len(dependencies.strip()) > 0:
            messages.append(
                {
                    "role": "user",
                    "content": self.get_dependencies(dependencies)
                }
            )   
        
        messages.append(
            {
                "role": "user",
                "content": instruction,
            }
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0,
            max_tokens=max_tokens,
            top_p=1,
        )

        return response.choices[0].message.content
