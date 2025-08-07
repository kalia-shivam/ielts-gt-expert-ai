import functions_framework
from dotenv import load_dotenv
import os
import time
from openai import OpenAI

# Load env vars locally (ignored on Google Cloud)
load_dotenv()

@functions_framework.http
def get_answer(request):
    # declare assistant id
    assistant_id = os.environ.get("OPENAI_ASSISTANT_ID")
    
    # get inputs
    request_json = request.get_json(silent=True)
    question = request_json['question']

    # initialize openai
    client = OpenAI(api_key==os.environ.get("OPENAI_API_KEY"))

    # create a thread
    thread = client.beta.threads.create()

    # create message (question) in thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=question
    )

    # run assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        instructions=""
    )

    # wait 30 seconds for response
    time.sleep(30)

    # get answer
    thread_messages = client.beta.threads.messages.list(thread.id)
    answer = thread_messages.data[0].content[0].text.value

    result = {
        'answer': answer
    }
    return result
