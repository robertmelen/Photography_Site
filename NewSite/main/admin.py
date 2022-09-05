from django.contrib import admin
from . models import Media, Category, Albums

admin.site.register(Media)
admin.site.register(Category)
admin.site.register(Albums)




#@admin.register(Media)
#class MediaAdmin(admin.ModelAdmin):
    #list_display  = ('image', 'categories', 'order',)

