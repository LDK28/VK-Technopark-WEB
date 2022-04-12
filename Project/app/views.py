from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for q #{i}",
        "number": i,
        "tags": ["This is a tag", "another tag", "tag"]
    } for i in range(10)
]

QUESTIONS.append({"title": f"Title #{10}",
                  "text": f"This is text for q #{10}",
                  "number": 10,
                  "tags": ["This is a tag", "Technopark", "C++"]})
QUESTIONS.append({"title": f"Title #{11}",
                  "text": f"This is text for q #{11}",
                  "number": 11,
                  "tags": ["Python", "Technopark"]})


def index(request):
    questions_paginator = Paginator(QUESTIONS, 5)
    page_num = request.GET.get('page')
    page = questions_paginator.get_page(page_num)


    return render(request, "index.html", {'page': page})


def ask(request):
    return render(request, "ask.html")


def question(request, i: int):
    return render(request, "question_page.html", {"question": QUESTIONS[i]})

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def tags(request, tag: str):
    return render(request, "tags.html", {"questions": QUESTIONS, "tag": tag})
