from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from . models import Media, Category, Albums


# Create your views here.


class HomeView(TemplateView):

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutView(TemplateView):

    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ContactView(TemplateView):

    template_name = "main/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(ListView):

    template_name = "main/index.html"
    model = Media

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['main_images'] = Media.objects.filter(visable=True)
        context ['image_categories'] = Category.objects.filter(visable=True)
        #context['image_categories'] =
        return context


class SelectView(ListView):

    template_name = "main/select.html"
    model = Media

    def get_queryset(self):

        # Also, the self keyword is not needed here either -> self.category
        category = get_object_or_404(Category, slug=self.kwargs['slug'])  # updated
        return Media.objects.filter(categories__title=category)  # updated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


    #def get_queryset(self):
        #self.publisher = get_object_or_404(Media, name=self.kwargs['pk'])
        #return Media.objects.filter(categories__title=self.publisher)


class GallerySelectView(ListView):

    template_name = "main/gallery_select.html"
    model = Media

    def get_queryset(self):
        # Also, the self keyword is not needed here either -> self.category
        category = get_object_or_404(Category, slug=self.kwargs['slug'])  # updated
        return Media.objects.filter(categories__title=category)  # updated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['main_images'] = Media.objects.filter(visable=True)
        return context


    #def get_queryset(self):
        #self.publisher = get_object_or_404(Media, name=self.kwargs['pk'])
        #return Media.objects.filter(categories__title=self.publisher)




class GalleryView(ListView):

    template_name = "main/gallery.html"
    model = Albums


    #def get_queryset(self, *args, **kwargs):
        #return get_object_or_404(Albums.album_pictures.filter(self.kwargs['slug']))


#class GalleryDetail(ListView):

    #template_name = "main/gallery_detail.html"
    #model = Media

    #def get_queryset(self):
        # Also, the self keyword is not needed here either -> self.category
        #gallery = get_object_or_404(Media, gallery=self.kwargs['gallery'])  # updated

        #return Media.objects.filter(gallery=gallery)  # updated


class GalleryDetailView(ListView):

    template_name = "main/gallery-detail.html"
    model = Media

    def get_queryset(self):

        gallery = get_object_or_404(Albums, slug=self.kwargs['slug'])
        print(gallery)
        return Media.objects.filter(album_pictures=gallery)

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)

        #context['all_album_images'] = Media.objects.filter(gallery=self.gallery)
        #return context