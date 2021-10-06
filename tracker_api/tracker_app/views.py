from django.http.response import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import * 
from django.shortcuts import redirect, render
from requests.api import get, head
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
import requests
import json
from rest_framework import viewsets
from .models import User
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login
from .permissions import *
from rest_framework.decorators import action

# imports for Token Authentications
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import renderers

login_url="https://channeli.in/oauth/authorise/?client_id=JnuJPM5FzaNL9lNfA6rHKUzwiuupkcjhzFDYlB1F&redirect_uri=http://localhost:8000/tracker_app/login1/&state=RANDOM_STATE_STRING"


def oauth_redirect(req):
    url = f"https://channeli.in/oauth/authorise/?client_id=JnuJPM5FzaNL9lNfA6rHKUzwiuupkcjhzFDYlB1F&redirect_uri=http://localhost:8000/tracker_app/login1/&state=RANDOM_STATE_STRING"
    return HttpResponseRedirect(url)

def login1(request):
        print("hello")
        code=request.GET.get('code')
        # code = request.query_params.get('code')
        data = {
            'client_id' : 'JnuJPM5FzaNL9lNfA6rHKUzwiuupkcjhzFDYlB1F',
            'client_secret':'QAus2sQdnLINdZdNbufezRfP4Tu0g04Y7cB3zAIRQ81VGIQFVIpIsuOQMBZ6iJsoPyej9nLk0evIbPbsdDStLqOqoJEyNrqSL9kQfqebbOLMsf05LkkmIPw2uwdjE6IZ',
            'grant_type':'authorization_code',
            'redirect_uri':'http://localhost:8000/tracker_app/login1/',
            'code':code
        }
        r= requests.post("https://channeli.in/open_auth/token/",data=data)
        auth_response=json.loads(r.content)
        print("hello")
        # return JsonResponse(auth_response) 
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
                user=User.objects.get(username=username)
                login(request=request,user=user)
                auth_token = Token.objects.get_or_create(user=user)
                admin = user.is_admin
                return redirect(f"http://localhost:3000/token/?token={auth_token}&admin={admin}&username={user.username}")
                # return Response(UserSerializer(User.objects.get(username=username)).data)
            else:
                user=User.objects.get(username=username)
                login(request=request,user=user)
                auth_token = Token.objects.get_or_create(user=user)
                admin = user.is_admin
                return redirect(f"http://localhost:3000/token/?token={auth_token}&admin={admin}&username={user.username}")
                # return Response(UserSerializer(User.objects.get(username=username)).data)
        return Response({'error':"Not a member of IMG"})

class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[UserPermissions]

    @action(methods=['GET'], detail = False, url_path='projects',url_name='user-projects')
    def user_projects(self, request):
        projects = ProjectSerializer(request.user.project.all(), many = True)
        return Response(projects.data)

    @action(methods=['GET'], detail = False, url_path='lists',url_name='user-lists')
    def user_lists(self,request):
        list_data=[]
        for project in request.user.project.all():
            list_data.append(ListSerializer(project.project_lists.all(), many = True).data,)
        return Response(list_data)

    @action(methods=['GET'], detail = False, url_path='cards',url_name='user-cards')
    def user_cards(self,request):
        # change
        
        card = CardSerializer(request.user.card.all(), many = True)
        return Response(card.data)

class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset=project.objects.all()
    serializer_class=ProjectSerializer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[ProjectPermissions]

    @action(methods=['GET'], detail = False, url_path='(?P<pk>[^/.]+)/lists',url_name='user-lists')
    def project_lists(self,request,pk):
        list_data=[]
        for project in request.user.project.all():
            if project.project_name==pk:
                list_data.append(ListSerializer(project.project_lists.all(), many = True).data,)
        return Response(list_data)

    @action(methods=['GET'], detail = False, url_path='(?P<pk>[^/.]+)/(?P<pk1>[^/.]+)/cards',url_name='user-cards')
    def project_list_cards(self,request,pk,pk1):
        card_data=[]
        for card in request.user.assignee_card.all():
            if card.project_card.project_name==pk and card.list_card.list_name==pk1:
                card_data.append(CardSerializer(card).data)
        return Response(card_data)

# class ListsModelViewSet(viewsets.ModelViewSet):
'''included in project_lists'''
#     queryset=lists.objects.all()
#     serializer_class=ListSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[ListPermissions]

    # @action(methods=['GET'], detail = False, url_path='lists',url_name='user-lists')
    # def list(self,request):
    #     list_data = ListSerializer(request.user.project.all().project_lists.all(), many = True)
    #     return HttpResponse(list_data.data)

class CardsModelViewSet(viewsets.ModelViewSet):
    queryset=card.objects.all()
    serializer_class=CardSerializer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[CardPermissions]

    @action(methods=['GET'], detail = False, url_path='(?P<pk>[^/.]+)/(?P<pk1>[^/.]+)/(?P<pk2>[^/.]+)/checklist',url_name='user-cards')
    def card_checklist(self,request,pk,pk1,pk2):
        checklist_data=[]
        card1=card.objects.get(card_name=pk2)
        for checklist in request.user.card1.assignee_checklist.all():
            if card1.project_card.project_name==pk and card1.list_card.list_name==pk1:
                checklist_data.append(ChecklistSerializer(checklist).data)
        return Response(checklist_data)

class ChecklistModelViewSet(viewsets.ModelViewSet):
    queryset=checklist.objects.all()
    serializer_class=ChecklistSerializer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[ChecklistPermissions]

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)