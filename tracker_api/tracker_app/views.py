from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView
from .serializers import * 

from django.http.response import HttpResponse,JsonResponse
import json
from django.shortcuts import redirect, render
import requests
from requests.api import get, head
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.contrib.auth import login

from typing import List
from django.shortcuts import render
from django.http import HttpResponse, response
import requests
import json
from rest_framework import viewsets
from .models import User
# from requests.api import request
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import *

login_url="https://channeli.in/oauth/authorise/?client_id=JnuJPM5FzaNL9lNfA6rHKUzwiuupkcjhzFDYlB1F&redirect_uri=http://127.0.0.1:8000/tracker_app/user_login/&state=RANDOM_STATE_STRING"

# user
class LoginClass(APIView):
    def get(self,request):
        code=request.GET.get('code')
        # code = request.query_params.get('code')
        data = {
            'client_id' : 'JnuJPM5FzaNL9lNfA6rHKUzwiuupkcjhzFDYlB1F',
            'client_secret':'QAus2sQdnLINdZdNbufezRfP4Tu0g04Y7cB3zAIRQ81VGIQFVIpIsuOQMBZ6iJsoPyej9nLk0evIbPbsdDStLqOqoJEyNrqSL9kQfqebbOLMsf05LkkmIPw2uwdjE6IZ',
            'grant_type':'authorization_code',
            'redirect_uri':'http://127.0.0.1:8000/tracker_app/user_login/',
            'code':code
        }
        r= requests.post("https://channeli.in/open_auth/token/",data=data)
        auth_response=json.loads(r.content)

        token_request = requests.get(url = "https://channeli.in/open_auth/get_user_data/", headers={"Authorization": f"{auth_response['token_type']} {auth_response['access_token']}"})
        token_response = json.loads(token_request.content)
        # return JsonResponse(token_response)
        username=token_response.get('username')
        fullname=token_response['person']['fullName']
        role = token_response['person']['roles'][1]['role']
        email = token_response['contactInformation']['instituteWebmailAddress']
        if str(role)=='Maintainer':
            if User.objects.filter(username=username).count()==0:
                User.objects.create(username=username, fullname=fullname, email = email)
                login(request, User.objects.get(username=username))
                return Response(UserSerializer(User.objects.get(username=username)).data)
            else:
                login(request, User.objects.get(username=username))
                return Response(UserSerializer(User.objects.get(username=username)).data)
        return Response({'error':"Not a member of IMG"})

class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[UserPermissions]

class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset=project.objects.all()
    serializer_class=ProjectSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[ProjectPermissions]

class ListsModelViewSet(viewsets.ModelViewSet):
    queryset=lists.objects.all()
    serializer_class=ListSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[ListPermissions]

class CardsModelViewSet(viewsets.ModelViewSet):
    queryset=card.objects.all()
    serializer_class=CardSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[CardPermissions]