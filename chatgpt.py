import openai

# Set up authentication
openai.api_key = 'My_OpenAI_API_Key'

# Define conversation
conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Hi there! I am ChatGPT. Ask me anything.'},
]

# Create prompt
def create_prompt(conversation):
    prompt = ''
    for message in conversation:
        prompt += f'{message["role"]}: {message["content"]}\n'
    return prompt

# Send request to the API
def send_request(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response

# Process and display response
def process_response(response):
    reply = response.choices[0].text.strip().split('\n')[-1]
    return reply

# Main loop
while True:
    user_input = input('User: ')
    conversation.append({'role': 'user', 'content': user_input})
    prompt = create_prompt(conversation)
    response = send_request(prompt)
    reply = process_response(response)
    conversation[-1]['content'] = reply  # Update the assistant's reply
    if 'assistant: That is not a valid question.' not in reply:
        print('ChatGPT: ', reply)
