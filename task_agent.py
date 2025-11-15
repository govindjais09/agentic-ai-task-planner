import os
from dotenv import load_dotenv

from google import genai

#load env
load_dotenv()

client = genai.Client(
    api_key = os.getenv("gemini")
)

#read task from file 
def read_task_from_file(file_path):
    with open(file_path, 'r') as f:
        task = f.read().strip()
    return task


#make a call to api with prompt to categorize the task

def summarize_task(tasks):
    prompt =f""" 
    
    You are a smart task planning agent ,
    Given a list of tasks, categorize them into 3 priority buckets:
    -High Priority 
    -Medium Priority
    -Low Priority

    Tasks:
    {tasks}

    Return the response in this format:
    High Priority:
    - Task 1
    - Task 2

    Medium Priority:
    - Task 1
    - Task 2

    Low Priority:
    - Task 1  
    - Task 2
    
    """
    
    #model call
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
       )
    return response.candidates[0].content.parts[0].text

if __name__ == "__main__":
    task_text = read_task_from_file('tasks.txt')
    summary = summarize_task(task_text)
    print(f"Task Summary:\n\n{summary}\n\n")