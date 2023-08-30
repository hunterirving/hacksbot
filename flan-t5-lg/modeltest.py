from transformers import T5Tokenizer, T5ForConditionalGeneration
import os

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")

while True:
	input_text = input("Type something: ")
	#input_text = "Please tell me a bedtime story about a cute dog named Scout who loves to chase rabbits."
	input_ids = tokenizer(input_text, return_tensors="pt").input_ids

	outputs = model.generate(input_ids,  max_new_tokens=200)
	outputs0 = tokenizer.decode(outputs[0])[6:][:-4]
	print(outputs0)
	os.system("say " + outputs0.replace('"', '').replace("'", '').replace('(', '').replace(')', ''))
