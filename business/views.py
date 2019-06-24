from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from business.forms import AddSentenceForm, SubmitSuggestForm
from django.views.generic.list import ListView
from django.shortcuts import redirect
from business.models import Sentence


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


@login_required
def submit_suggest(request):
    if request.method == "POST":
        form = SubmitSuggestForm(request.POST)
        if form.is_valid():
            suggest = form.save(request)
            suggest.save()
            return redirect('home')
    else:
        form = SubmitSuggestForm()
    return render(request, 'submit_suggest.html', {'form': form})


class SentenceList(ListView):
    model = Sentence
    template_name = 'sentence_list.html'


@login_required
def sentence_detail(request, sentence_id, sentence_title):
    if request.method == "POST":
        form = SubmitSuggestForm(request.POST)
        if form.is_valid():
            suggest = form.save(request)
            suggest.save()
            return redirect('home')
    else:
        form = SubmitSuggestForm()
        sentence = get_object_or_404(Sentence, id=sentence_id)
        return render(request, 'sentence_detail.html', {'sentence': sentence,
                                                        'form': form})
