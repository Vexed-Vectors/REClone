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
from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from .models import *
#from user_profile.models import *
#from events.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from itertools import chain
from django.core.files.base import ContentFile
from io import BytesIO
import urllib.request
from PIL import Image
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.core.mail import send_mass_mail
import json
import datetime
#import html2markdown
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from difflib import SequenceMatcher
from django.utils import timezone
from datetime import timedelta


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

def list_blogs(request):
    search = SearchForm(request.POST or None)
    if request.method == 'POST':
        if search.is_valid():
            key_req = search.cleaned_data
            key = key_req.get('key')
            return HttpResponseRedirect(reverse('blog:search_blog', args=(key,)))
            # search_blog function chahiye to return search results
    posts = Posts.objects.all().order_by('-created_at')
        # paginator = Paginator(posts, 5)
        # page = request.GET.get('page')
        # page_obj = paginator.get_page(page)
        # try:
        #     posts_list = paginator.page(page)
        # except PageNotAnInteger:
        #     posts_list = paginator.page(1)
        # except EmptyPage:
        #     if request.is_ajax():
        #         return HttpResponse('')
        #     posts_list = paginator.page(paginator.num_pages)
    p_count=posts.count()
    replys=Reply.objects.all()

    taggings_recent = Taggings.objects.all().order_by('-updated_at')
    tags_recent =  Tags.objects.all().order_by('-updated_at')
    tags_popular = []
    check =[]

    for tag in tags_recent:
        tagging = Taggings.object.filter(tag=tag)
        count = tagging.count()
        tags_popular.append([count,tag])
        if count>0:
            check.append(tag)
    tags_popular.sort(key=lambda x: x[0], reverse=True)
    tags_recent_record = []
    tags_popular_record = []

    if tags_recent.count()>10:
        limit=10
    else:
        limit=tags_recent.count()

    for i in range(limit):
        tags_popular_record.append(tags_popular[i][1])
    count=0
        
    while len(tags_recent_record)< len(taggings_recent) and len(tags_recent_record) < len(check) and len(tags_recent_record)<10:
        if taggings_recent[count].tag not in tags_recent_record:
            tags_recent_record.append(taggings_recent[count].tag)
        count+=1
        #profiles = Profile.objects.all()

    


    args = {'form_search':search, ''' 'profile':profiles,''' 'posts':posts, 'replys':replys,'tags':tags_recent, 'taggings':taggings_recent,'tags_recent':tags_recent_record, 'tags_popular':tags_popular_record, 'p_count':p_count,}
    return render(request, 'blogs/blogs.html', args)
    

    
