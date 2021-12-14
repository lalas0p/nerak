# pass
import openai
import os
import openai
import sys
from time import sleep

import pyttsx3

class Nerak:
    openai.api_key = "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"
    def __init__(self) -> None:
        self.completion = openai.Completion()
        self.start_chat_log = '''Human: Hello, who are you?
        AI: I am doing great. How can I help you today?
        '''
        self.chat_log = self.start_chat_log

    def ask(self, question, chat_log=None):
        if chat_log is None:
            chat_log = self.start_chat_log
        # prompt = f'{chat_log}Human: {question}\nAI:'
        prompt = f'{self.chat_log}Human: {question}\nAI:'
        response = self.completion.create(
            prompt=prompt, engine="davinci", stop=['\nHuman', "Human"], temperature=0.8,
            top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
            max_tokens=150)
        answer = response.choices[0].text.strip()
        return answer

    def append_interaction_to_chat_log(self, question, answer, chat_log=None):
        if chat_log is None:
            chat_log = self.start_chat_log
        return f'{chat_log}Human: {question}\nAI: {answer}\n'

    def getInput(self):
        q = input(">> ")
        a = self.ask(q)
        self.chat_log = self.append_interaction_to_chat_log(q, a, self.chat_log)
        return a

    def typeReply(self, reply):
        for char in reply:
            sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\n")

    def speakReply(self, command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()