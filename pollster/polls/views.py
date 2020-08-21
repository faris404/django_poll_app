from django.shortcuts import render,get_object_or_404

from .models import Question, Choice
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# get quetsions and display
def index(request):

    latest_question_list = Question.objects.all()[:5]   #   getting 5 questions
    context = {"latest_questions":latest_question_list}
    return render(request,'polls/index.html',context)

#   show specific question and choice
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('question does not exist')
    return render(request,'polls/detail.html',{'question':question})

#   get question and display result
def result(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question':question})


# vote for a question choice
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select any choice,"})

    else:
        select_choice.votes+=1
        select_choice.save()

        return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))