from multiprocessing import context
from pickle import EMPTY_LIST
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *

q = Question.objects.all()
a = Answer.objects.all()

# print(q[0].tags.all()[0])

QUESTIONS = [
    {
        "id": f"{q[i].id}",
        "title": f"{q[i].title}",
        "text": f"{q[i].text}",
        "number": i,
        "tags": [q[i].tags.all()[j] for j in range(len(q[i].tags.all()))],
        "likes": f"{LikeQuestion.objects.with_count_on_question_id(q[i].id)}"
    } for i in range(len(q))
]

QUESTIONSLIKES = [
    {
        "user": f"{q[i].title}",
        "text": f"{q[i].text}",
        "number": i,
        "tags": ["This is a tag", "another tag", "tag"]
    } for i in range(len(q))
]

ANSWERS = [
    {
        "id": f"{a[i].id}",
        "text": f"{a[i].text}",
        "number": i,
        "likes": f"{LikeAnswer.objects.with_count_on_answer_id(a[i].id)}"
    } for i in range(len(a))
]

def paginate(objects_list, request, per_page=10):
    items_paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page')
    page = items_paginator.get_page(page_num)
    return page

def index(request):
    page = paginate(QUESTIONS, request, 5)
    return render(request, "index.html", {'page': page})

## hotq
@login_required(login_url="/asker.com/login")
def ask(request):
    print(request.POST)

    if request.method == 'GET':
        ask_form = QuestionForm()
    elif request.method == 'POST':
        ask_form = QuestionForm(data=request.POST)
        if ask_form.is_valid():
            data = Question.objects.create(title=request.POST.get('title'),
                                    text=request.POST.get('text'),
                                    user_id=q[0].user_id)
            data.save()
            print(data)

    return render(request, "ask.html", {'form': ask_form})


def question(request, i: int): #, title: str):
    answers = Answer.objects.filter(question = QUESTIONS[i].get('id'))
    page = paginate(answers, request, 5)

    if request.method == 'GET':
        answer_form = AnswerForm()
    elif request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            data = Answer.objects.create(text=request.POST.get('text'),
                                        user_id=q[0].user_id,
                                        question=QUESTIONS[i].get('id'))
            data.save()
            print(data)

    return render(request, "question_page.html", {
        "question": QUESTIONS[i], 
        "page": page, 
        'form': answer_form
    }) #, "title": title})

def signup(request):
    print(request.POST)

    if request.method == 'GET':
        user_form = RegistrationForm()
    elif request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            CustomUser.objects.create_user(username=request.POST.get('username'), 
                                           password=request.POST.get('password'), 
                                           first_name=request.POST.get('first_name'),
                                           last_name=request.POST.get('last_name'),
                                           email=request.POST.get('email'))
            return redirect(reverse('index'))

    return render(request, "signup.html", {'form': user_form})

def login(request):
    print(request.POST)

    if request.method == 'GET':
        user_form = LoginForm()
    elif request.method == 'POST':
        user_form = LoginForm(data=request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request, **user_form.cleaned_data)
            if user:
                return redirect(reverse('index'))
    return render(request, "login.html", {'form': user_form})

@login_required(login_url='asker.com/login/')
@require_http_methods(['GET', 'POST'])
def profile(request):
    if request.method == 'GET':
        initial_data = model_to_dict(request.user)
        form = SettingsForm(initial=initial_data)
    elif request.method == 'POST':
        initial_data = request.POST
        instance = request.user
        form = SettingsForm(initial=initial_data, instance=instance, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    return render(request, "profile.html", {'form': form})

def tags(request, tag: str):
    return render(request, "tags.html", {"questions": QUESTIONS, "tag": tag})


# @login_required
@require_POST
def vote(request):
    question_id = request.POST['question_id']
    question = Question.objects.get(id=question_id)
    try:
        like = LikeQuestion.objects.create(user=request.user, question=question)
        like.save()
    except:
        print("Like already exists")
    new_rating = LikeQuestion.objects.with_count_on_question_id(question_id)
    return JsonResponse({'new_rating': new_rating})
