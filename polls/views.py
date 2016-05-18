from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context,request))
##    output = ', '.join([q.question_text for q in latest_question_list])
##    return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
##    try:
##        question = Question.objects.get(pk=question_id)
##    except Question.DoesNotExist:
##        raise Http404("존재하지 않는 질문입니다.")
##    return render(request, "polls/detail.html",{'question': question})
##    return HttpResponse("당신은 질문 %s을 보고 있습니다."% question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
##    response = "당신은 질문 %s의 결과를 보고 있습니다."
##    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "선택지를 골라주세요.",
                        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
##    return HttpResponse("당신은 질문 %s에 투표하고 있습니다."% question_id)

