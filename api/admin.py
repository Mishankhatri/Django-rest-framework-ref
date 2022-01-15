from django.contrib import admin
from .models import Singer, Song, Student
# Register your models here

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
    
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'gender']
    
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','title','singer','duration']






