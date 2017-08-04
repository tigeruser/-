from django.contrib import admin
from models import Article

# Register your models here.
class Aadmin(admin.ModelAdmin):
    list_display = ('id','title','content','pubtime')


admin.site.register(Article,Aadmin)
