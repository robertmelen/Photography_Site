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


#def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    #context = super().get_context_data(**kwargs)
    # Add in a QuerySet of all the books

    #context['galley_pics'] = Albums.album_images.all()
