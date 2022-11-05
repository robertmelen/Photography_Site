from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.urls import reverse
from . models import Media, Category, Albums, BlogPost, Post_Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .forms import CommentForm




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
    paginator = Paginator(objects_list, 12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'main/gallery.html', {'objects_list': objects_list, 'posts': posts})


def Gallery_Detail(request, slug):
    pics = get_object_or_404(Albums, slug=slug)
    gallery_images = Media.objects.filter(album_pictures=pics)

    return render(request, 'main/gallery-detail.html', {'pics': gallery_images, 'pics_two': pics})


def BlogList(request, slug=None, blog_category=None):
    categories = Post_Category.objects.all()
    object_list = BlogPost.objects.all()
    if slug:
        tag = get_object_or_404(Tag, slug=slug)
        object_list = object_list.filter(status="published", tags__slug=tag)
    elif blog_category:
        category = get_object_or_404(Post_Category, slug=blog_category)
        object_list = object_list.filter(status="published", blog_category__slug=category)


    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'main/blog-posts.html', {'posts': posts, 'page': page, 'categories': categories, 'slug': slug })

def post_detail(request, year, month, day, post):
    post = get_object_or_404(BlogPost, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()
    return render(request, "main/post-detail.html", {'post': post, 'new_comment': new_comment,
                                                     'comment_form': comment_form,})




def category_detail(request, pk):
    category = get_object_or_404(Post_Category, pk=pk)
    return render(request, 'main/category-detail.html', {'category':category})



def list_posts_by_tag(request, tag_id):
    tag = get_object_or_404(BlogPost, id=tag_id)
    posts = BlogPost.objects.filter(status="published", tags=tag)
    context = {
        "tag_name": tag.name,
        "posts": posts
    }
    return render(request, "blog-posts", context)















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

