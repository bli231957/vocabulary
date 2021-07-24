from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Question
from .models import Word


def index(request):
    latest_question_list = Word.objects.order_by('headword')[:5]
    output = ', '.join([q.headword for q in latest_question_list])
    template = loader.get_template('card/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    item = get_object_or_404(Word, pk=id)
    return render(request, 'card/detail.html', {'item': item})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def cards(request):
    items = []
    for question in latest_question_list:
        items.append(get_object_or_404(Word, pk=question.id))

    return render(request, 'card/cards.html', {'question': items})
