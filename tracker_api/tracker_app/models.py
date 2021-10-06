from django.db import models
from django.db.models.base import Model
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import related
from ckeditor.fields import RichTextField 
import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(AbstractUser):
    username=models.CharField(primary_key=True,max_length=10,unique=True)
    fullname=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    is_admin=models.BooleanField(default=False)

    class Meta:
        db_table='User'

    def __str__(self):
        return self.username

class project(models.Model):
    project_name=models.CharField(primary_key=True,max_length=100, unique=True)
    wiki=RichTextField()     
    is_complete=models.BooleanField(default=False)
    creator=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="created_projects")
    members=models.ManyToManyField(User,related_name='project') 

    class Meta:
        db_table='project'

    def __str__(self):
        return self.project_name

class lists(models.Model):
    list_name=models.CharField(primary_key=True,max_length=100, unique=True)
    project_list=models.ForeignKey(to=project,on_delete=models.CASCADE,related_name="project_lists")
    color=models.CharField(max_length=50)

    class Meta:
        db_table='lists'
        UniqueConstraint(fields=['list_name','project_list'],name='unique_list')

    def __str__(self):
        return self.list_name

class checklist(models.Model):
    checklist=models.CharField(primary_key=True,max_length=100, unique=True)
    is_complete=models.BooleanField(default=False)

    class Meta:
        db_table='checklist'

    def __str__(self):
        return self.checklist

class card(models.Model):
    card_name=models.CharField(primary_key=True,max_length=100, unique=True)
    list_card=models.ForeignKey(to=lists,on_delete=models.CASCADE,related_name="list_cards")
    project_card=models.ForeignKey(to=project,on_delete=models.CASCADE,related_name="project_cards")
    start_date = models.DateTimeField(default=datetime.datetime.now())
    due_date = models.DateTimeField(default=datetime.datetime.now())
    is_complete = models.BooleanField(default=False)
    assignee=models.ManyToManyField(User,related_name='assignee_card')
    asignee_checklist=models.ManyToManyField(checklist,blank=True)
    color=models.CharField(max_length=50)

    class Meta:
        db_table='card'
        UniqueConstraint(fields=['card_name','list_card','project_card'],name='unique_card')

    def __str__(self):
        return self.card_name

class card_comment(models.Model):
    card=models.ForeignKey(to=card,on_delete=models.CASCADE)
    text=RichTextField()

    class Meta:
        db_table='card_comment'

    def __str__(self):
        return self.text