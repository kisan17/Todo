from rest_framework import serializers
from todo.models import *

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoList
        fields='__all__'