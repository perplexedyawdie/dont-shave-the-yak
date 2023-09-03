from dotenv import load_dotenv
import os
import openai
from prompts import abc_analysis_prompt, markdown_formatter, batch_pro_prompt, cpm_prompt, wellbeing_prompt
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model="gpt-3.5-turbo-0613"
def md_formatter(text):
    chat_completion = openai.ChatCompletion.create(model=model, messages=[
                                                        {"role": "system", "content": markdown_formatter},
                                                        {"role": "user", "content": f"{text}"}],
                                                        temperature=0,
                                                        max_tokens=1000,)
    return chat_completion.choices[0].message.content  

def abc_analyser(tasks): 
    chat_completion = openai.ChatCompletion.create(model=model, messages=[
                                                        {"role": "system", "content": abc_analysis_prompt},
                                                        {"role": "user", "content": f"{tasks}"}])
    return chat_completion.choices[0].message.content

def task_batcher(tasks): 
    chat_completion = openai.ChatCompletion.create(model=model, messages=[
                                                        {"role": "system", "content": batch_pro_prompt},
                                                        {"role": "user", "content": f"{tasks}"}])
    return chat_completion.choices[0].message.content

def critical_path_finder(tasks): 
    chat_completion = openai.ChatCompletion.create(model=model, messages=[
                                                        {"role": "system", "content": cpm_prompt},
                                                        {"role": "user", "content": f"{tasks}"}])
    return chat_completion.choices[0].message.content

def mood_booster(time): 
    chat_completion = openai.ChatCompletion.create(model=model, messages=[
                                                        {"role": "system", "content": wellbeing_prompt},
                                                        {"role": "user", "content": f"{time}"}])
    return chat_completion.choices[0].message.content