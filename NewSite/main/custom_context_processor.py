from .models import Profile, Category, BlogPost


def user_info(request):
   user = request.user
   current_user = Profile.objects.get(user=user)
   return {'user': current_user }

def post_info(request):
  popular_posts = BlogPost.objects.filter(status='published').order_by('-created')[0:3]
  return {'popular_posts': popular_posts}


