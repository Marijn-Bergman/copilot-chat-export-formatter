import json
from subprocess import run

def format_chat_log(chat_log):
    formatted_chat_log = ""
    turns = chat_log['providerState']['turns']
    for turn in turns:
        request_message = turn['request']['message']
        response_message = turn['response']['message']
        formatted_chat_log += f"# request:\n{request_message}\n# response:\n{response_message}\n\n---\n"
    return formatted_chat_log

# Path to the JSON file
file_path = 'chat.json'
# Path to the output text file (newly created)
output_file_path = 'formatted_chat_log.txt'

# Reading the JSON file
with open(file_path, 'r') as file:
    raw_data = file.read()

# Finding the index where the relevant portion starts
start_index = raw_data.find('"providerId": "copilot"')
relevant_data = raw_data[start_index:]

# Parsing the relevant JSON data
chat_log = json.loads('{' + relevant_data)

# Formatting the chat log
formatted_chat_log = format_chat_log(chat_log)

# Creating and saving the formatted chat log to a new text file
with open(output_file_path, 'w') as file:
    file.write(formatted_chat_log)


command = 'gh gist create --filename copilot.md -'
result = run(command, input=formatted_chat_log, shell=True, capture_output=True, text=True)

# Print the output of the command
print(result.stdout)
