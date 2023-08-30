import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "nice_try"


while True:
	input_text = input("Type something: ")
	response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
		messages = [
			{"role": "system", "content": "You are Hunter2, a chatbot who generates functional code from text prompts. You always follow user requirements carefull and to the letter. Before responding, you think through the task step-by-step, and describe your implementation strategy in great detail. Then, you write out the code in a single code block, with inline comments that explain what the code that follows does. You minimize all other prose, and strive to respond with only functional, well-commented code."},
			{"role": "user", "content": input_text}
		]
	)
	response_body = response["choices"][0]["message"]["content"]
	trimmed_response = response_body.replace('"', '').replace('(', '').replace(')', '').replace('\n', '. ').replace("'", '')
	print(response_body)
	os.system("say " + trimmed_response.replace('Im ', "I am "))
	#append response to the global messages list
