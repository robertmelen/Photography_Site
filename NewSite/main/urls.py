from django.urls import path, include
from django.urls import re_path
from . import views


app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("about", views.AboutView.as_view(), name="about"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("select/<slug:slug>", views.SelectView.as_view(), name="select"),
    path("gallery_select/<slug:slug>", views.GallerySelectView.as_view(), name="gallery_select"),
    path("gallery/<slug:slug>", views.Gallery_Detail, name="gallery-detail"),
    path("gallery/", views.GalleryView, name="gallery"),
    path("blog-posts/", views.BlogList, name="blog-posts"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path("category/<int:pk>", views.category_detail, name='category_detail'),

    #path("gallery-detail/<slug:slug>", views.GalleryDetailView.as_view(), name="gallery_detail"),



]