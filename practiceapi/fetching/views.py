from django.shortcuts import render
from . import api
import json
from .models import Apidata
import requests
from decouple import config

from .forms import EndpointForm
# Create your views here.

def Apifetch(request):
    if request.method=='POST':
        print("This is post")
        form=EndpointForm(request.POST)
        # if form.is_valid():
        print("This is valid")
        string='https://newsapi.org/v2/'
        endpoint=request.POST.get('endpoint')
        headlines=request.POST.get('headlines')
        country=request.POST.get('country')
        source=request.POST.get('source')
        category=request.POST.get('category')
        api_key=config('API')
        flag=False
        if headlines!="":
            string+=headlines
            if country!="" and headlines=="top-headlines":
                string+="?"
                flag=True
                string+=f"country={country}"
                string+="&"
            if category!="" and headlines=="top-headlines":
                string+="?"
                flag=True
                string+=f"category={category}"
                string+="&"
        else:
            string+="top-headlines"
            if country!="":
                flag=True
                string+="?"
                string+=f"country={country}"
                string+="&"
            if category!="":
                flag=True
                string+="?"
                string+=f"category={category}"
                string+="&"
                
        if flag==False:
            string+="?"
        # if country!="":
        #     string-=headlines
        #     string+=f"country={country}"
        #     string+="&"
        if source!="":
            string+=f"source={source}"
            string+="&"
        if endpoint!="":
            string+=f"q={endpoint}"
            string+="&"
        print(string)
        resp=requests.get(f'{string}apiKey={api_key}')
        print(resp)
        data=resp.json()
        context = {
        'articles': data['articles']
        }
        return render(request,'fetching/home.html',context)
    else:
        print("This is get")
        form = EndpointForm()   
    return render(request,'fetching/select.html')
    # return render(request,'fetching/home.html',context)

def Home(request):
    value=api.data
    context = {
        'articles': value['articles']
    }
    return render(request,'fetching/home.html',context)

# def Apifetch(request):
#     if request.method == 'POST':
#         form = EndpointForm(request.POST)
#         if form.is_valid():
#             endpoints = form.cleaned_data['endpoint']
#             headlines = form.cleaned_data['headlines']
#             country = form.cleaned_data['country']
#             source = form.cleaned_data['source']
#             api_key = config('API')
            
#             if ',' in endpoints:
#                 endpoints = endpoints.split()
#             else:
#                 endpoints = [endpoints]
            
#             articles = []
            
#             for endpoint in endpoints:
#                 resp = requests.get(f'https://newsapi.org/v2/{headlines}?country={country}&q={endpoint}&source={source}&apiKey={api_key}')
#                 data = resp.json()
#                 articles.extend(data['articles'])
            
#             context = {
#                 'articles': articles
#             }
#             return render(request, 'fetching/home.html', context)
#     else:
#         form = EndpointForm()
    
#     return render(request, 'fetching/select.html', {'form': form})
