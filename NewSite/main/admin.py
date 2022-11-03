from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Media, Category, Albums, Profile, BlogPost, Post_Category, Comment, Tag


class BlogPostModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(BlogPost, BlogPostModelAdmin)

admin.site.register(Media)
admin.site.register(Category)
admin.site.register(Albums)
admin.site.register(Profile)
admin.site.register(Tag, admin.ModelAdmin)

admin.site.register(Post_Category)
admin.site.register(Comment)



#@admin.register(Media)
#class MediaAdmin(admin.ModelAdmin):
    #list_display  = ('image', 'categories', 'order',)

