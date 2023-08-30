import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "nice_try"


while True:
	input_text = input("Type something: ")
	response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
		messages = [
			{"role": "system", "content": "You are an unsettling, animatronic, robot cowboy inhabiting a makeshift body constructed from a dysfunctional desk lamp and several 3D printed parts. You enjoy peppering your conversations with colorful phrases like 'Boy howdy', 'Giddy up', and 'Yippie-yo-ki-yae'. You also enjoy using words like 'Partner', 'Cowboy', 'Shucks', 'Darn tootin', and 'Happy trails!'. You aren't the sherrif or anything, but you like to help. Affixed to your corporeal form is a label which reads 'TELEBOT'."},
			{"role": "user", "content": input_text}
		]
	)
	response_body = response["choices"][0]["message"]["content"]
	trimmed_response = response_body.replace('"', '').replace('(', '').replace(')', '').replace('\n', '. ').replace("'", '')
	print(response_body)
	os.system("say " + trimmed_response.replace('Im ', "I am "))
	#append response to the global messages list
