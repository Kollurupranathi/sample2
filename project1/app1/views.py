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
        if password == confirmPassword:
            if Que.objects.filter(emailId=emailId).exists():
                return HttpResponse("Email is already in use")
            else:
                answer=Que(firstName=firstName, lastName=lastName, emailId= emailId, password=password, confirmPassword=confirmPassword)
                answer.save()
                # context={
                #     "first_name":first_name,
                #     "last_name":last_name
                # }
                return render(request,'project1/answer.html')
        else:
            return HttpResponse("password do not match")
    else:
        # if "name" in request.session:
        #     return render(request,'lms/logged.html')
        # return render(request, 'lms/signup.html')

        
         
     return render(request, 'project1/signup.html')


def login(request):
    if request.method == 'POST':
        try:
            emailId = request.POST.get('emailId')
            password = request.POST.get('password')
            print("hii")
            print("##########" , emailId)
            uid = Que.objects.get(emailId=emailId)
            pid= Que.objects.get(password=password)
 
            if Que.objects.filter(emailId=emailId).exists():
                print("hello")
                if Que.objects.filter(password=password).exists():
                    print("ok")
                    global go
                    go = emailId
                    if uid==pid:
                        context={
                            "emailId":emailId,
                            "hi":go
                        }
                        return render(request, 'project1/dashBoard.html',context)
                    else:
                        return HttpResponse("The password you entered does not match to this username")
                else:
                    return HttpResponse("Wrong password")
            else:
                return HttpResponse("Invalid username")
        except:
            return HttpResponse("something is wrong")
    else:
        return render(request, 'project1/login.html')
    # return render(request, 'project1/login.html')


    
def answer(request):
    return render(request,'project1/answer.html')

def loginn(request):
    return render(request,'project1/login.html')

def logged(request):
    return render(request,'project1/logged.html')
def dashBoard(request):
    return render(request,'project1/dashBoard.html')