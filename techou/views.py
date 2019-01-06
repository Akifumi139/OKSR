from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def See(request):
    db = {
        'messages': Message.objects.all(),
    }
    return render(request, 'See.html',db)

def Write(request):
    if request.method == 'POST':
        obj = Message()
        message = MessageForm(request.POST, instance=obj)
        message.save()
        return redirect('See')

    params = {
        'title': '登録',
        'form': MessageForm(),
    }
    return render(request, 'Write.html',params)

def take_img(request):
    return render(request, 'take_img.html')
