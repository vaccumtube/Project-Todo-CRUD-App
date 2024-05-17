from django.shortcuts import render,redirect
from .models import TodoApp
from .forms import TodoForm

# Create your views here.

def Create(request):
       obj=TodoApp.objects.all()
       form=TodoForm()
       if request.method=="POST":
              form=TodoForm(request.POST)
              if form.is_valid:
               form.save()  
              return redirect('/index')
       return render(request,"todo/index.html",{'todo':obj,
                                             'form':form})

def update(request,id):
     objec=TodoApp.objects.get(id=id)
     form=TodoForm(instance=objec)
     if request.method=="POST":
              form=TodoForm(request.POST,instance=objec)
              if form.is_valid:
               form.save()  
              return redirect('/index')
     return render(request,"todo/update.html",{
                                             'form':form})

def delete(request,id):
     objec=TodoApp.objects.get(id=id)
     if request.method=="POST":
      objec.delete()
      return redirect("/index")
     return render(request,"todo/delete.html",
                   )
      

     


