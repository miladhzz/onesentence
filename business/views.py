from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from business.forms import AddSentenceForm

from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')


@login_required
def add_sentence(request):
    if request.method == "POST":
        form = AddSentenceForm(request.POST)
        if form.is_valid():
            sentence = form.save(request)
            sentence.save()
            return redirect('home')
    else:
        form = AddSentenceForm()
    return render(request, 'add_sentence.html', {'form': form})
