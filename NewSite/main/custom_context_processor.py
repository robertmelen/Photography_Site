from .models import Profile


def about_us_pic(request):
   user = request.user
   current_user = Profile.objects.get(user=user)
   pic = current_user.image
   return {'pic': pic }