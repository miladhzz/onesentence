from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Suggest, Sentence
import logging
from django.db.models import Count
from django.shortcuts import redirect
from onesentence.enums import SuggestEnum, SentenceEnum
from dashboard.forms import EditCompleteFileForm
import datetime

logger = logging.getLogger(__name__)


@login_required
def dashboard_ap(request):
    my_sentence = Sentence.objects.annotate(num_suggests=Count('suggest')).filter(
        user=request.user)
    return render(request, 'applicant_dashboard.html', {'my_sentence': my_sentence})


@login_required
def dashboard_tr(request):
    my_suggests = Suggest.objects.filter(mojri=request.user)
    logger.error('Test log error')
    return render(request, 'translator_dashboard.html', {'my_suggests': my_suggests})


@login_required
def check_suggest(request, sentence_id):
    sentence = get_object_or_404(Sentence, id=sentence_id)
    suggests = Suggest.objects.filter(sentence_id=sentence.id)
    if request.method == "POST":
        suggest_id = request.POST.get('suggest_id')
        sentence_id = request.POST.get('sentence_id')
        # check if suggest_id exist in sentence
        suggests_count = Sentence.objects.filter(id=sentence_id, suggest__id=suggest_id,
                                                 suggest__status_id=1).count()
        if suggests_count == 1:
            suggest = Suggest.objects.get(id=suggest_id)
            # update status of selected suggest
            Suggest.objects.filter(id=suggest_id).update(status_id=SuggestEnum.Accept.value)
            # update sentence status
            Sentence.objects.filter(id=sentence_id).update(status_id=SentenceEnum.Processing.value,
                                                           translator=suggest.mojri)
            # update another suggest to reject
            reject_suggests = Suggest.objects.filter(sentence_id=sentence_id).exclude(sentence_id=sentence_id,
                                                                                      status_id=2)
            for reject_suggest in reject_suggests:
                Suggest.objects.filter(id=reject_suggest.id).update(status_id=SuggestEnum.Reject.value)
            return redirect('dashboard:dashboard_ap')
        return redirect('business:home')
    else:
        return render(request, 'check_suggests.html', {"sentence": sentence,
                                                       "suggests": suggests})


@login_required
def sentence_detail_dashboard(request, sentence_id, sentence_title):
    sentence = get_object_or_404(Sentence, id=sentence_id)
    accept_suggest = Suggest.objects.filter(sentence_id=sentence.id, status=SuggestEnum.Accept.value)
    suggest = Suggest
    try:
        suggest = Suggest.objects.get(sentence_id=sentence.id, status=SuggestEnum.Accept.value)
    except:
        pass
    if request.method == "POST":
        form_file = EditCompleteFileForm(request.POST, request.FILES, instance=suggest)
        if form_file.is_valid():
            suggest = form_file.save(commit=False)
            suggest.upload_time = datetime.datetime.now()

            suggest.save()
            # update sentence status
            Sentence.objects.filter(id=sentence.id).update(status_id=SentenceEnum.Completed.value)
            return redirect("dashboard:dashboard_tr")
    else:
        form_file = EditCompleteFileForm(instance=suggest)
    return render(request, 'sentence_detail_dashboard.html', {"sentence": sentence,
                                                              "accept_suggest": accept_suggest,
                                                              "form_file": form_file})
