from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from . models import Que

# Create your views here.
# def que(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         password = request.POST['password']
#         answer=Que(name=name, password=password)
#         answer.save()
#         return render(request,'project1/answer.html')
#     return render(request, 'project1/login.html')

def que(request):
    if request.method == 'POST':
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        emailId= request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['cpassword']
        answer=Que(firstName=firstName, lastName=lastName, emailId= emailId, password=password, confirmPassword=confirmPassword)
        answer.save()
        return render(request,'project1/answer.html')
    return render(request, 'project1/signup.html')


def login(request):
    return render(request, 'project1/login.html')


    
def answer(request):
    return render(request,'project1/answer.html')