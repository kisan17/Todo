from django.shortcuts import render
from todo.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoListSerializer


@api_view(['GET'])
def showall(request):
    todo=TodoList.objects.all()
    serializer= TodoListSerializer(todo,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request,id):
    todo=TodoList.objects.get(pk=id)
    serializer=TodoListSerializer(todo)
    return Response(serializer.data)

@api_view(['POST'])
def Update(request,id):
    todo=TodoList.objects.get(pk=id)
    serializer=TodoListSerializer(todo,instance=todo)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer=TodoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def delete(request,id):
    todo=TodoList.objects.get(pk=id)
    todo.delete()
    return Response("Item delete Sucessfully")