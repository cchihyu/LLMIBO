from openai import OpenAI
import os
import sys

# Create an instance of the OpenAI client
client = OpenAI()

def gen(comment):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"{comment}"
        }
    ]

    # Call the OpenAI API to generate the completion
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    # Access the message content correctly
    message_content = completion.choices[0].message.content  # Access the message's content

    return message_content

if __name__ == "__main__":
    # Check if an argument was passed
    if len(sys.argv) != 2:
        print("Usage: python example.py <uppercase_letter>")
        sys.exit(1)

    # Get the capital letter input from the command line arguments
    comment = sys.argv[1]

    try:
        word = gen(comment)
        print(f"{word}")
    except Exception as e:
        print(f"Error: {e}")
