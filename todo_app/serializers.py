from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class RegistrationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ['username','email','password']
        
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = "__all__"

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    todo_id = serializers.SerializerMethodField('get_todo_id')

    class Meta:
        model = Todo
        fields = ['todo_id','user','title','description','created_at','due_date','priority','completed','category']
        
    def get_user(self, obj):
        return obj.user.id if obj.user else None
    
    def get_todo_id(self, obj):
        return obj.id