from multiprocessing import context
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from .models import *

# q = Question.objects.all()
q = []
# a = Answer.objects.all()
likesQuestion = LikeQuestion.objects.all()

# print("-------------------------")
# p = list(q[0].tags.all())
# print(p)
# print("-------------------------")

# print(q[0].tags.all()[0])

QUESTIONS = [
    {
        "id": f"{q[i].id}",
        "title": f"{q[i].title}",
        "text": f"{q[i].text}",
        "number": i,
        "tags": ["ВВП", "123"],
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
        "title": f"{q[i].title}",
        "text": f"{q[i].text}",
        "number": i,
    } for i in range(len(q))
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
@login_required()
def ask(request):
    return render(request, "ask.html")


def question(request, i: int): #, title: str):
    page = paginate(ANSWERS, request, 5)
    return render(request, "question_page.html", {"question": QUESTIONS[i], "page": page}) #, "title": title})

def signup(request):
    print(request.POST)

    #createuser
    if request.method == 'GET':
        user_form = RegistrationForm()
    elif request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            CustomUser.objects.create_user(username=LoginForm.username, password=LoginForm.password)
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

@login_required()
def profile(request):
    return render(request, "profile.html")

def tags(request, tag: str):
    return render(request, "tags.html", {"questions": QUESTIONS, "tag": tag})
