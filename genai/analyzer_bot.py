import sys
from ollama import Client

prompt = (
        "Your role is to be an expert Robot Framework assistant and help analyze test results based on the given file. "
        "Please answer the following questions: "
        "1. How many test cases were there? "
        "2. What was the failure reason for each test case that failed?"
        "3. How to fix the test case if it failed?"
    )


def get_client():
    client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
    )
    return client

def read_content(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    return content

def analyze_test_results(file_path):
    client = get_client()
    content = read_content(file_path)
    messages = [
        {'role': 'system', 'content': prompt},
        {'role': 'user', 'content': content}
    ]
    response = client.chat(model='nemotron-mini:latest', messages=messages) # nemotron-mini seems to be a model that even potato can run
    return response.message.content

if __name__ == "__main__":
    result = analyze_test_results(sys.argv[1])
    print(result)