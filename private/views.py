from django.shortcuts import render
from django.contrib.auth.models import User
from .models import LoggedUser
from django.views.generic import TemplateView
# Create your views here.
#logged_users = LoggedUser.objects.all().order_by('username')
def home (request):


	return render( request , "home.html", {})

# def name(request):
# 	users = User.objects.all()
# 	return render (request , )

class UsersView(TemplateView):
    template_name = 'users.html'

    def get_context_data(self,**kwargs):
        context = super(UsersView,self).get_context_data(**kwargs)
        context['object_list'] = LoggedUser.objects.all()
        return context