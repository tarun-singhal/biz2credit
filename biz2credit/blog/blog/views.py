"""
TODO:
1. move httpbasic auth into settings.py file
2. set api url in settings.py
3. 
"""
from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
from django.views.generic import CreateView
from .forms import StoryForm
from django.contrib import messages
from .tables import table
from django_tables2 import RequestConfig
from datetime import datetime

def home(request):
    response = requests.get('http://localhost:5000/api/v1/story', auth=HTTPBasicAuth('admin', 'SuperSecretPwd'))
    userdata = response.json()
    print(userdata)
    return render(request, 'core/home.html', {
        "data": userdata 
    })


def blog_list(request):
    # filter = ProductFilter(request.GET, queryset=table)
    table.paginate(page=request.GET.get('page', 1), per_page=5)
    RequestConfig(request, paginate={"per_page": 5}).configure(table)
    return render(request, 'core/blog_list.html', {'blogList': table})

def blog_vote(request):
    pass

"""
Create Blog Form
"""
def create_blog(request):
    messages.success(request, "")
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            headers = {
                "content-type": "application/json"
            }
            story_status = 'Published' if data['status'] == '1' else 'Draft'
            data = {
                "title": data['title'], 
                "content": data['content'],
                "email": data['email'],
                "status": story_status,
                "created_time": datetime.now().isoformat(),
                "updated_time": datetime.now().isoformat()
            }

            resp = requests.post("http://localhost:5000/api/v1/story", headers= headers, json=data, auth=HTTPBasicAuth('admin', 'SuperSecretPwd'))
            res = resp.json()
            if 'resp' in res:
                form = StoryForm()
                messages.success(request, "Story created successfully !")
            else:
                messages.error(request, "Error Found, Please check log...")
    else:
        form = StoryForm()
    return render(request, 'core/blog.html', {'form': form})    