from django.contrib import admin
from . models import Media, Category, Albums, Profile

admin.site.register(Media)
admin.site.register(Category)
admin.site.register(Albums)
admin.site.register(Profile)




#@admin.register(Media)
#class MediaAdmin(admin.ModelAdmin):
    #list_display  = ('image', 'categories', 'order',)

