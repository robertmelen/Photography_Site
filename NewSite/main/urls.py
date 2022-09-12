from django.urls import path, include

from . import views


app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("about", views.AboutView.as_view(), name="about"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("select/<slug:slug>", views.SelectView.as_view(), name="select"),
    path("gallery_select/<slug:slug>", views.GallerySelectView.as_view(), name="gallery_select"),
    path("gallery", views.GalleryView, name="gallery"),
    #path("gallery-detail/<slug:slug>", views.GalleryDetailView, name="gallery_detail"),



]