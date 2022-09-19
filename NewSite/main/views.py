from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.urls import reverse
from . models import Media, Category, Albums
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




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



#thi sCBV is for the main index slidshow and is view for the partial gallery select which
#worked well with the template ajax so no need to change this too much

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


#slug=None is optional paramater that deals with page refresh after HTMX view for Gallery

def GalleryView(request):
    objects_list = Albums.objects.all()
    return render(request, 'main/gallery.html', {'objects_list': objects_list})


def Gallery_Detail(request, slug):
    pics = get_object_or_404(Albums, slug=slug)
    gallery_images = Media.objects.filter(album_pictures=pics)

    return render(request, 'main/gallery-detail.html', {'pics': gallery_images, 'pics_two': pics})






#View function that handles gallery back button to refresh to main gallery page
#as seen here https://rajasimon.io/blog/htmx-server-side-redirect/

def gallery_back(request):
    response = HttpResponse("Okay")

    response["HX-Redirect"] = reverse("main:gallery")
    return response





















  # if request.htmx:
  #       try:
  #           slug = request.GET.get('slug')
  #           pics = get_object_or_404(Albums, slug=slug)
  #           pictures = Media.objects.filter(album_pictures=pics)
  #           page = request.GET.get('page', 1)
  #           paginator = Paginator(pictures, 2)
  #
  #           try:
  #               pics = paginator.page(page)
  #           except PageNotAnInteger:
  #               pics = paginator.page(1)
  #           except EmptyPage:
  #               pics  = paginator.page(paginator.num_pages)
  #
  #           context = {'pics': pictures,
  #                      'description': Albums.objects.filter(slug=slug)}
  #           return render(request, 'main/htmx-partials/gallery-detail.html', context=context)
  #       except:
  #           #this pass fixes getting a error 404 on refresh
  #           pass

