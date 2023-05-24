from django.shortcuts import render, redirect
from django.contrib import messages
import openai
from .models import History


# Homepage View
def home(request):
	question = ""
	response = ""
	past_responses = ""

	if request.method == 'POST':
		question = request.POST.get('question')	
		past_responses = request.POST.get('past_responses', '')

		# Openai API 
		openai.api_key = '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'
		openai.Model.list()
		try:
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

			# logic for past_responses
			if "skmvosno" in past_responses:
				past_responses = response
			else:
				past_responses = f"{past_responses}</br></br>{response}"

			# save to database
			record = History(question=question, answer=response)
			record.save()

			return render(request, 'chatbot/home.html', {"question": question, 
			"response": response, "past_responses": past_responses})
		except Exception as e:
			return render(request, 'chatbot/home.html', {"question": e, 
			"response": response, "past_responses": past_responses})

	return render(request, 'chatbot/home.html', {"question": question, 
		"response": response, "past_responses": past_responses})

def history_view(request):
	history = History.objects.all()
	return render(request, 'chatbot/history.html', {"history": history})

def delete_record(request, record_id):
	record = History.objects.get(id=record_id)
	record.delete()
	messages.success(request, 'The record has been deleted!')
	return redirect('history-view')