from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
import json
from .models import Posts
from .serializers import PostsSerializer



# Create your views here.

def homepage(request):
    return HttpResponse('HELO')

# class postslistViewSet(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer

# def PostsList(request):
#     if request.method == 'GET':
#         posts = Posts.objects.all()
#         serializer = PostsSerializer(instance = posts, many=True)
     
#         return JsonResponse(serializer.data, safe=False  ) # safe --> allows non dict objects to be serialized

# class postslistViewSet(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer

class PostsView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        posts = Posts.objects.all()  
        serializers = PostsSerializer(posts, many=True)  
        return Response({'status': 'success', "posts":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = PostsSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
