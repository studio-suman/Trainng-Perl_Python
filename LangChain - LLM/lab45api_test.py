import requests  # Import the requests module to send HTTP requests

# Define the API endpoint for querying the document completion skill
completion_endpoint = f"https://api.lab45.ai/v1.1/skills/completion/query"

# Set the headers for the request, including content type, accepted response format, and authorization token
headers = {
    'Content-Type': "application/json",  # The content type of the request is JSON, meaning the request body will be in JSON format
    'Accept': "text/event-stream, application/json",  # The server is expected to respond with either event-stream or JSON
    'Authorization': "Bearer token|123675a6-95f6-4fb7-bc95-30095472ae3a|02de311fd83421a7fd637bf34dc8f959caa29f39888d2919e4b9640a2220224b"  # Replace <api_key> with your actual API key for authentication
}

# Define the payload (request body) for the API call, which contains the user's query and skill parameters
payload = {
        "messages": [
            {
            "content": "what is difference between cat and dog?",
            "role": "user"
            }
        ],
        "skill_parameters": {
            "model_name": "gpt-35-turbo-16k",
            "max_output_tokens": 256,
            "temperature": 0,
            "top_k": 5
        },
    "stream_response": False
    }
 
 
try:
    response = requests.post(completion_endpoint, headers=headers, json=payload)
    response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
    print(response.json())  # Print the response data
except requests.exceptions.RequestException as e:
    print(f"Error making the request: {e}")
 
# Print the response from the API call to inspect the result (status code, content, etc.)