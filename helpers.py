import requests

# Constants OLLAMA Local Setup
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}



def build_payload(messages):
    MODEL = "llama3.2:1b"
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }
    return payload


def get_response(payload):
    try:
        response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
        if response.status_code == 200:
            return response.json()['message']['content']
    except Exception as e :
        print(f"Error Occured : {e}")
