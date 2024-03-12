from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.models import Token


# Create your views here.


class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
        
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            
            token, created = Token.objects.get_or_create(user=account)
            print('token is', token)
            token_key = token.key

            data = {
                'response': "REGISTRATION SUCCESSFUL",
                'username': account.username,
                'token': token_key
            }
        else:
            data = serializer.errors
        return Response(data)

    
class Logout(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': "success",
            'message': "Listed all categories successfully",
            'response_code': status.HTTP_200_OK,
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response({
                'status': "success",
                'message': "Created category successfully",
                'response_code': status.HTTP_201_CREATED,
                'category_id': data.id,
                'name': data.name,
                'description': data.description,
                'category': data.name
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
class CategoryRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Category.objects.filter(pk=pk)
    
    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': "success",
            'message': "Updated category successfully",
            'response_code': status.HTTP_200_OK,
            'data': serializer.data
        })

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({
            'status': "success",
            'message': "Deleted todo successfully",
            'response_code': status.HTTP_204_NO_CONTENT,
        })
    
    
        

class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user) 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  
            return Response({
                'status': "success",
                'message': "Created new todo successfully",
                'response_code': status.HTTP_201_CREATED,
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Todo.objects.all()
    serializer_class = TodoSerializer    
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user) 
    
    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user = request.user)
        return Response({
            'status': "success",
            'message': "Updated todo successfully",
            'response_code': status.HTTP_200_OK,
            'data': serializer.data
        })

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({
            'status': "success",
            'message': "Deleted todo successfully",
            'response_code': status.HTTP_204_NO_CONTENT,
        })
