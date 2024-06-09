# First, install the Azure OpenAI SDK package by running the command in the integrated terminal: [pip install openai==1.13.3]

import os
from dotenv import load_dotenv

# Add Azure OpenAI Package:
from openai import AsyncAzureOpenAI

# Set to True to print the full response from OpenAI for each call:
printFullResponse = False

def main():
    try: 
        # Get Configuration Settings: 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")
        
        # Configure the Azure OpenAI Client:
        client = AsyncAzureOpenAI(azure_endpoint = azure_oai_endpoint, api_key=azure_oai_key, api_version="2024-02-15-preview")
            
        while True:
            print('1: Basic prompt (no prompt engineering)\n' +
                  '2: Prompt with email formatting and basic system message\n' +
                  '3: Prompt with formatting and specifying content\n' +
                  '4: Prompt adjusting system message to be light and use jokes\n' +
                  '\'quit\' to exit the program\n')
            command = input('Enter a number:')
            if command == '1':
                call_openai_model(messages="../prompts/basic.txt", model=azure_oai_model, client=client)
            elif command =='2':
                call_openai_model(messages="../prompts/email-format.txt", model=azure_oai_model, client=client)
            elif command =='3':
                call_openai_model(messages="../prompts/specify-content.txt", model=azure_oai_model, client=client)
            elif command =='4':
                call_openai_model(messages="../prompts/specify-tone.txt", model=azure_oai_model, client=client)
            elif command.lower() == 'quit':
                print('Exiting program...')
                break
            else :
                print("Invalid input. Please try again.")

    except Exception as ex:
        print(ex)

def call_openai_model(messages, model, client):
    # In this sample, each file contains both the system and user messages. First, read them into variables, strip whitespace, then build the messages array:
    file = open(file=messages, encoding="utf8")
    system_message = file.readline().split(':', 1)[1].strip()
    user_message = file.readline().split(':', 1)[1].strip()

    # Print the messages to the console:
    print("System message: " + system_message)
    print("User message: " + user_message)

    # Format and send the request to the model:
    print("\nAdding grounding context from grounding.txt")
    grounding_text = open(file="grounding.txt", encoding="utf8").read().strip()
    user_message = grounding_text + user_message
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    
    print("\nSending request to Azure OpenAI model...\n")

    # Call the Azure OpenAI model:
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=800     
    )
    
    if printFullResponse:
        print(response)

    print("Completion: \n\n" + response.choices[0].message.content + "\n")

if __name__ == '__main__': 
    main()
        
# At the end, in the integrated terminal, enter the following command to run the application: [python prompt-engineering.py]
