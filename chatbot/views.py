from django.shortcuts import render


def home(request):
	if request.method == 'POST':
		question = request.POST.get('question')
		return render(request, 'chatbot/home.html', {"question": question})

	return render(request, 'chatbot/home.html', {"question": question})