from django.contrib import admin
from .models import RegData
from .models import Enquiry
from .models import AdminReg
# Register your models here
@admin.register(RegData)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','lname','email','contact','password']

@admin.register(Enquiry)
class QueryAdmin(admin.ModelAdmin):
    list_display=['id','name','lname','email','contact','enquiry','password']

#=========================== Admin Database ====================================#
@admin.register(AdminReg)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','lname','email','contact','password']