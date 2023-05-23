from django.shortcuts import render
import openai


# Homepage View
def home(request):
	question = ""
	response = ""

	if request.method == 'POST':
		question = request.POST.get('question')	

		# Openai API 
		openai.api_key = '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'
		openai.Model.list()
		response = openai.Completion.create(
			model='text-davinci-003',
			prompt=question,
			temperature=0,
			max_tokens=60,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0
			)

		# parse the response
		response = (response["choices"][0]["text"]).strip()

		return render(request, 'chatbot/home.html', {"question": question, 
		"response": response})

	return render(request, 'chatbot/home.html', {"question": question, 
		"response": response})