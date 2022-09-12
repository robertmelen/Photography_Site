from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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



#
# def GalleryDetailView(request):
#     pass





def GalleryView(request):

    if request.htmx:
        slug = request.GET.get('slug')
        pics = get_object_or_404(Albums, slug=slug)

        context = {'pictures': Media.objects.filter(album_pictures=pics),
                   'description': Albums.objects.filter(slug=slug)}
        return render(request, 'main/gallery-detail.html', context=context)

    context = {'objects_list': Albums.objects.all()}
    return render(request, 'main/gallery.html', context=context)
# class GalleryDetailView(DetailView):
#
#     template_name = "main/gallery-detail.html"
#
#     def get(self, request, *args, **kwargs):
#         pictures = get_object_or_404(Albums, slug=kwargs['slug'])
#         pictures_all = Media.objects.filter(album_pictures=pictures)
#         print(pictures_all)
#         context = {'gallery_pics': pictures_all}
#         return render(request, 'main/gallery-detail.html', context)








    #WORKING QUERYSEWTR FILTER
    #def get_queryset(self):

        #gallery = get_object_or_404(Albums, slug=self.kwargs['slug'])
        #print(gallery)
        #return Media.objects.filter(album_pictures=gallery)







    #def get_context_data(self, **kwargs):
        #context = super(GalleryDetailView, self).get_context_data(**kwargs)
        #context['object_list'] =
        #print(context['object_list'])
            #Media.objects.filter(gallery=self.gallery)
        #return context



#FUNCTION BASED TEST DIDNT WORK
#def gallery_list(request, slug):
    #image_list = get_object_or_404(Albums, slug=slug)
    #images = Media.objects.filter(album_pictures=image_list)

    #return render(request, 'main/gallery-detail.html',
                  #{'images': images})