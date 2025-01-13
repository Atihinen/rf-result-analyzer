import sys
from ollama import Client

prompt = (
        "Your role is to be expert robotframework assistant and help out to analyze test results based on given file. "
        "Please answer to following questions: How many test cases there were and what was the failure reason if the test case was failing."
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
    response = client.chat(model='nemotron-mini:latest', messages=messages)
    return response.message.content

if __name__ == "__main__":
    result = analyze_test_results(sys.argv[1])
    print(result)
