from openai import OpenAI
import os
import sys

# Create an instance of the OpenAI client
client = OpenAI()

def generate_values_for_bayesian_optimization(dim,mn,mx,n):
    messages = [
        {"role": "system", "content": "You are an assistant, your main rule is to help me with maximizing a black box function."},
        {
            "role": "user",
            "content": f"The input space is {dim} dimensional, the upper bound and lower bound of each dimensional is between {mn} and {mx}. Please provide exactly {n} diverse yet effective values to initiate a Bayesian Optimization process for this problem. Each point must be inside (). Seperate the points using a space and without any additional text or explanation. "
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
    try:
        dim = sys.argv[1]
        mn = sys.argv[2]
        mx = sys.argv[3]
        n = sys.argv[4]
        
        values = generate_values_for_bayesian_optimization(dim,mn,mx,n)
        print(values)
    except Exception as e:
        print(f"Error: {e}")
