from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import tasks
from .forms import taskform,createform

# Create your views here.
def entry (request):
   return render(request,"entry.html")

@login_required(login_url="entry")
def tasklist (request):
   context = {}
   
   context['Tasks'] = tasks.objects.filter(user = request.user)
   count = context['Tasks'].filter(complete = False).count()
   search_key = request.GET.get('search-area','')
   if search_key:
      context['Tasks'] = context['Tasks'].filter(Title__startswith=search_key)
   return render(request,"task_display.html",{"tasks":context['Tasks'],'User':request.user,'search':search_key,'count':count})


@login_required(login_url="entry")
def viewtask (request,taskid):
   Task = tasks.objects.get(id = taskid)
   if Task.complete == True:
      Task.complete = "Done"
   else:
      Task.complete = "Not Done"
   return render(request,"task_view.html",{"Task":Task})

@login_required(login_url="entry")
def createtask (request):
   n = len(tasks.objects.all())
   if request.method == "POST":
      form = createform(request.POST)
      if form.is_valid():
         form.save()
         task = tasks.objects.get(id = n+1)
         task.user = request.user
         task.save()
         return redirect("tasklist")
   else:
      form = createform()
   return render (request,"task_create.html" ,{'form':form})

@login_required(login_url="entry")
def deletetask (request,taskid):
   task = tasks.objects.get(id = taskid)
   if request.method == "POST":
      task.delete()
      return redirect('tasklist')

   return render (request,"task_delete.html",{'Task':task})

@login_required(login_url="entry")
def updatetask (request,taskid):
   task = tasks.objects.get(id = taskid)
   form = taskform(request.POST or None,instance= task)
   if request.method == "POST":
      form = taskform(request.POST,instance=task)
      if form.is_valid():
         form.save()
         return redirect("tasklist")
   return render (request,"task_update.html" ,{'form':form})

def register(request):
   if request.method == "POST":
      username =  request.POST['username']
      name =  request.POST['name']
      if name == "":
         name = username
      email =  request.POST['email']
      password1 =  request.POST['pass1']
      password2 =  request.POST['pass2']
      if username != "":
         if email != "":
            if password1 == password2 and password1 != "" and password2 != "":
               myuser = User.objects.create_user(username,email,password1)
               myuser.name = name
               myuser.save()
               messages.success(request,"You are registered!!")
               return redirect("signin") 

            else:
               messages.error(request,"Confirm Password and Password must be same")
               return redirect("register")
         else:
            return redirect("register")

      else:
         return redirect("register")


 
   return render(request,"register.html")

def signin(request):
   if request.method == "POST":
      username = request.POST["username"]
      password1 = request.POST["pass"]

      user = authenticate(username = username , password=password1)

      if user is not None:
         login(request,user)
         return redirect("tasklist")
      else:
         messages.warning(request,"Wrong password or username")
         return redirect("signin") 
   return render(request,"signin.html")

@login_required(login_url="entry")
def signout (request):
   logout(request)
   messages.success(request,"Successfully signed out. Come back soon....")
   return redirect('/')