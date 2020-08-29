
    
    
    
    
    
from django.shortcuts import render
import requests
import json
import random

# Create your views here.

#question=""
#options={}
#corr_answer=""
#qnCount=0
#score=0
def one(request):
    if "qnCount" not in request.session:
        request.session['qnCount']=0
    if "details" not in request.session:
        request.session['details']={'question':'', 'options':{'A':'', 'B':'', 'C':'', 'D':''}, 'corr_answer':''}
    #global qnCount
    #query=api(request.session['details'])
    api(request.session['details'])
    request.session['qnCount']+=1
    return render(request, 'app/1.html', {'qn':request.session['details']['question'], 'optA':request.session['details']['options']['A'], 'optB':request.session['details']['options']['B'], 'optC':request.session['details']['options']['C'], 'optD':request.session['details']['options']['D']})


def two(request):
    #global score
    if "score" not in request.session:
        request.session['score']=0
    var=request.GET.get('useropt')
    # print(var)
    if(request.session['details']['options'][var]==request.session['details']['corr_answer']):
        request.session['score']+=1
        return render(request, 'app/2.html', {'key':'Correct', 'qnCount': request.session['qnCount'], 'score': request.session['score']})
    else:
        return render(request, 'app/3.html', {'key':'Incorrect', 'corr_answer':request.session['details']['corr_answer'], 'qnCount': request.session['qnCount'], 'score': request.session['score']})

def three(request):
    if request.GET.get('Quit')=='quit':
        return render(request, 'app/4.html')
    else:
        return one(request)

def api(details): #returns question, options and correct answer
    #global question
    #global options
    #global corr_answer
    result=requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
    resulte=json.loads(result.text)
    details['question']=resulte['results'][0]['question']
    tot_answers=resulte['results'][0]['incorrect_answers']
    details['corr_answer']=resulte['results'][0]['correct_answer']
    tot_answers.insert(random.randint(0, len(tot_answers)), details['corr_answer'])
    details['options']={'A':tot_answers[0], 'B':tot_answers[1], 'C':tot_answers[2], 'D':tot_answers[3]}
