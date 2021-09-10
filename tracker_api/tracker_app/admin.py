from django.contrib import admin
from .models import User,project,lists,checklist,card,card_comment

# Register your models here.
admin.site.register(User)
admin.site.register(project)
admin.site.register(lists)
admin.site.register(checklist)
admin.site.register(card)
admin.site.register(card_comment)