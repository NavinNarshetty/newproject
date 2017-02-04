from django.contrib import admin

# Register your models here.
from .forms import SignupForm
from .models import Signup 

class SignupAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', "timestamp" ,"updated"]
    form =SignupForm
    # class meta:
        # model=Signup


admin.site.register(Signup , SignupAdmin)
