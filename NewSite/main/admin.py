from django.contrib import admin
from . models import Media, Category, Albums, Profile, BlogPost

admin.site.register(Media)
admin.site.register(Category)
admin.site.register(Albums)
admin.site.register(Profile)
admin.site.register(BlogPost)



#@admin.register(Media)
#class MediaAdmin(admin.ModelAdmin):
    #list_display  = ('image', 'categories', 'order',)

