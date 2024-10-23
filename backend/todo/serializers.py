from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User
#Serializer to give out the models in the right format
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'content', ' created_at', 'updated_at', 'completed' ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_user(self,value):
        if not isinstance(value, User):
            raise serializers.ValidationError("Invalid user")
        return value