from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_cate(request):
    if request.method =='POST':
        category_form=forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('show_tasks')
    else:
        category_form = forms.CategoryForm()

    return render (request,'add_cate.html',{'form':category_form})
