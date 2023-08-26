from django.shortcuts import render

from .models import passwords , chats ,answers





# Create your views here.
def home(request):
    username = request.POST.get('username')
    address = request.POST.get('address')
    number = request.POST.get('number')
    color =  request.POST.get('color')
 
    data = passwords(username= username ,address = address , number = number , color = color)
  
    if request.method == 'POST':
        data.save()
    return render(request,'home.html')

def ecommere(request):
    username = request.POST.get('username')
    address = request.POST.get('address')
    number = request.POST.get('number')
    color =  request.POST.get('color')
    data = passwords(username= username ,address = address , number = number , color = color)
    if request.method == 'POST':
        data.save()
    return render(request,'ecommere.html')



def support(request):
    chat = request.POST.get('chat')
    data = chats(chat = chat)
    if request.method == 'POST':
        data.save()
    context = { "answers": answers.objects.all()}
    return render(request,'support.html', context)

def chatbot(request):
    return render(request,'chatbot.html',  {"chats": answers.objects.all()})

   
# myapp/views.py



# accounts/views.py


# your_app_name/views.py
