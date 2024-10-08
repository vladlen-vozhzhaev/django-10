from django.http import HttpResponse
import random

from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import UserRegisterFrom, UserAuthForm
from django.contrib.auth import login, authenticate
# Create your views here.

def index(req):
    articles = Article.objects.all()
    return render(req, "index.html", {'articles': articles, 'title': 'Мой блог'})
def article(req, id):
    article = get_object_or_404(Article, id=id)
    return render(req,"post.html", {'article': article, 'title': article.title})

def register(req):
    if req.method == 'POST':
        print("Принимаем данные от пользователя")
        form = UserRegisterFrom(req.POST)
        if form.is_valid():
            print("Валидация прошла успешно")
            user = form.save()
            login(req, user)
            return redirect("home")
    else:
        form = UserRegisterFrom()
    return render(req, 'register.html', {'form': form, 'title': "Регистрация на сайте"})

def login_handler(req):
    if req.method == 'POST':
        form = UserAuthForm(req, data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect("home")
    else:
        form = UserAuthForm()
    return render(req, 'login.html', {'form': form, 'title': "Вход на сайт"})

def contact(req):
    print(req.POST.get('name'))
    print(req.POST.get('email'))
    print(req.POST.get('message'))
    return HttpResponse("Форма успешно отправлена")

def game(request):
    num1 = random.randint(0,3)
    num2 = random.randint(0, 3)
    num3 = random.randint(0, 3)
    if num1 == num2 == num3:
        response = f"Победа, все 3 числа равны! Числа: {num1}, {num2}, {num3}"
    else:
        response = f"Повезёт в следующий раз! Числа: {num1}, {num2}, {num3}"
    return HttpResponse(response)

def get_phrase1(req):
    return HttpResponse("Первая фраза")

def get_phrase2(req):
    return HttpResponse("Вторая фраза")
