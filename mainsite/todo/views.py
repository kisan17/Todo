from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

def getdata(request):
    category=Category.objects.all()
    todolist=TodoList.objects.all()
    context={
        'category':category,
        'todolist':todolist,
    }
    if request.method=='POST':
        if 'taskadd' in request.POST:

            title = request.POST["description"]
            category = request.POST["category_select"]
            date = str(request.POST["date"])
            content=title+'--'+date+''+category
            
            todo=TodoList(title=title,due_date=date,content=content,category = Category.objects.get(name=category))
            todo.save()
            return redirect("/")

    if request.method=='POST':
        if 'taskDelete' in request.POST:
            checked=request.POST.get('checkedbox')
            for todo in checked:
                todo=TodoList.objects.get(id=int(todo))
                todo.delete()
                return redirect('/')

    return render(request,'todo/getdata.html',context)


