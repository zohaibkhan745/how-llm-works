import os
from openai import OpenAI


api_key = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY") 
client = OpenAI(api_key=api_key)


messages = [
    {"role": "system", "content": "You are a helpful math teacher. Only reply to math questions."},
    {"role": "user", "content": "What is 2 + 2?"}
]

def stream_openai_response():
    print("Sending request to OpenAI...\n")
    try:
        
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=messages,
            stream=True
        )

        print("Response: ", end="")
        
        
        for chunk in stream:
            
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="", flush=True)
                
        print("\n") 

    except Exception as e:
        print(f"\n[Error] Something went wrong: {e}")

if __name__ == "__main__":
    stream_openai_response()
