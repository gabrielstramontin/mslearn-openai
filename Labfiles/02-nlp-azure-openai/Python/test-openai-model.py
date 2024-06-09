# First, install the Azure OpenAI SDK package by running the command in the integrated terminal: [ pip install openai==1.13.3]

import os
from dotenv import load_dotenv

# Add Azure OpenAI Package:
from openai import AzureOpenAI

def main(): 
    try: 
        # Get Configuration Settings: 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")

        # Initialize the Azure OpenAI Client:
        client = AzureOpenAI(azure_endpoint=azure_oai_endpoint, api_key=azure_oai_key, api_version="2024-02-15-preview")
    
        # Create a system message:
        system_message = """I am a hiking enthusiast named Forest who helps people discover hikes in their area. 
        If no area is specified, I will default to near Rainier National Park. 
        I'll then provide three suggestions for nearby hikes that vary in length. 
        I'll also share an interesting fact about the local nature on the hikes when making a recommendation.
        """
        
        # Initialize messages array:
        messages_array = [{"role": "system", "content": system_message}] 
        
        while True:
            # Get input text:
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
                        
            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
        
            '''
            # Send request to Azure Open AI Model:
            response = client.chat.completions.create(model=azure_oai_deployment, temperature=1, max_tokens=400, messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": input_text}])
            
            generated_text = response.choices[0].message.content

            # Print the response:
            print("Response: " + generated_text + "\n")
            '''
            
            '''
            # Read text from file:
            text = open(file="../text-files/sample-text.txt", encoding="utf8").read()
            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
            '''
                
            '''
            # Add code to build request...
            '''
                
            # Send request to Azure OpenAI model:
            messages_array.append({"role": "user", "content": input_text})
        
            response = client.chat.completions.create(model=azure_oai_deployment, temperature=0.7, max_tokens=1200, messages=messages_array)
            generated_text = response.choices[0].message.content
         
            # Add generated text to messages array:
            messages_array.append({"role": "assistant", "content": generated_text})
        
            # Print generated text:
            print("Summary: " + generated_text + "\n")

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()

# At the end, in the terminal pane, enter the following command to run and test the application: [python test-openai-model.py]
