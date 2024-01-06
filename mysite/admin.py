from django.contrib import admin
from mysite.models import Post, Episode
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')
    

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('post',  'episode')    

admin.site.register(Post, PostAdmin)
admin.site.register(Episode, EpisodeAdmin)