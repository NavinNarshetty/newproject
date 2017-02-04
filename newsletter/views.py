from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import Signup

from .forms import SignupForm ,ContactForm
# Create your views here.
def home(request):
    title ="Sign Up Now"

    # if request.user.is_authenticated():
        # title="My title %s" %(request.user)
    form=SignupForm(request.POST or None)

    context={
        "title":title,
        "form":form,
    }
    if form.is_valid():
        instance= form.save(commit=False)
        full_name=form.cleaned_data.get("full_name")
        if not full_name:
            full_name= "navin narshetty"
        instance.full_name=full_name
        instance.save()
        context={
            "title":"Thankyou"
        }

    if request.user.is_authenticated() and request.user.is_staff:
        # print Signup.objects.all()
        # i=1
        # for instance in Signup.objects.all():
            # print i
            # print instance.full_name
            # i +=1
        queryset = Signup.objects.all()
        context ={
            "queryset": queryset
        }
    return render( request , "home.html", context)

def contact(request):
    title ="Contact us"
    title_align_center=False
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form_email=form.cleaned_data.get("email")
        form_full_name=form.cleaned_data.get("full_name")
        form_message=form.cleaned_data.get("message")
        # print email , full_name,message
        subject= "Site contact form "
        from_email= settings.EMAIL_HOST_USER
        to_email=['navinnarshetty@gmail.com' , 'naveennashetty92@gmail.com']
        contact_message =" %s :%s via %s" %(
            form_full_name,
            form_message,
            form_email)

        send_mail(subject ,
            contact_message ,
            from_email ,
            to_email , 
            fail_silently=False)
    context ={
        "form":form,
        "title":title,
        "title_align_center":title_align_center,
    }


    return render(request , "forms.html" , context)