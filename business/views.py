from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from business.forms import AddSentenceForm, SubmitSuggestForm
from django.views.generic.list import ListView
from django.shortcuts import redirect
from business.models import Sentence, SuggestStatus, Suggest
from django.contrib.auth import logout
from onesentence.enums import SuggestEnum, SentenceEnum


def home(request):
    return render(request, 'home.html')


@login_required
def add_sentence(request):
    if request.method == "POST":
        form = AddSentenceForm(request.POST, user=request.user,)
        if form.is_valid():
            sentence = form.save(request)
            sentence.save()
            return redirect('business:home')
    else:
        form = AddSentenceForm()
    return render(request, 'add_sentence.html', {'form': form})


class SentenceList(ListView):
    model = Sentence
    template_name = 'sentence_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Only show not annotate sentence
        context['sentence_list'] = Sentence.objects.filter(status=SentenceEnum.Saved.value)
        return context


@login_required
def sentence_detail(request, sentence_id, sentence_title):
    sentence = get_object_or_404(Sentence, id=sentence_id)
    suggest_count = Suggest.objects.filter(sentence_id=sentence.id).count()
    current_user_suggest = {}
    if suggest_count > 0:
        current_user_suggest = Suggest.objects.filter(sentence_id=sentence.id, mojri=request.user)
    if request.method == "POST":
        form = SubmitSuggestForm(request.POST, user=request.user, sentence=sentence)
        if form.is_valid():
            suggest = form.save(commit=False)
            suggest.mojri = request.user
            suggest.status = SuggestStatus.objects.get(id=SuggestEnum.Waiting.value)
            suggest.sentence = sentence
            suggest.save()
            return redirect('business:home')
    else:
        form = SubmitSuggestForm()
    return render(request, 'sentence_detail.html', {'sentence': sentence,
                                                    'suggest_count': suggest_count,
                                                    'current_user_suggest': current_user_suggest,
                                                    'form': form})


def logout_view(request):
    logout(request)
    return redirect('business:home')
