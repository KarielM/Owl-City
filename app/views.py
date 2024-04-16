from django.shortcuts import render
from app.OwlCityDataclass import song_list
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def create_home_view(request:HttpRequest) -> HttpResponse:
    return render (request, 'base.html', {'songDict': song_list})

def create_details_view(request:HttpRequest, albumTitle) ->HttpResponse:
    return render (request,'details.html', {'Album': song_list[albumTitle]})