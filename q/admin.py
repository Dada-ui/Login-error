from django.contrib import admin
from q.models import *

# Register your models here.

class Login_modeladmin(admin.ModelAdmin):
    list_display=['id','username','password']
    
admin.site.register(Login_model,Login_modeladmin)


class Register_modeladmin(admin.ModelAdmin):
    list_display=['id','fname','mname','lname','username','phone','rephone','email','reemail','password','repassword','gender','city']
    
admin.site.register(Register_model,Register_modeladmin)


class Contact_modeladmin(admin.ModelAdmin):
    list_display=['id','username','email','phone','desc']
    
admin.site.register(Contact_model,Contact_modeladmin)