# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from .models import Friend
import json

from django.http import HttpRequest, JsonResponse


# Create your views here.
# def clear(Friend):
#
def index(request):
    return render(request, 'index.html')


def telegram(request):
    return render(request, 'teleg.html')


def friends(a):
    friendlist = Friend.objects.all()
    return render(a, 'friends.html', {'friendlist': friendlist})


def icount(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    friend.count += 1
    friend.save()
    # s = request.META['HTTP_REFERER']
    s = friend.link
    if s.startswith('http://') or s.startswith('https://'):
        return redirect(s)
    return redirect('http://' + friend.link)


def addfriend(request):
    d = request.POST
    print(d)
    name = d['name']
    link = d['vklink']

    Friend.objects.create(name=name, link=link)

    print(d)
    s = request.META['HTTP_REFERER']
    return redirect(s)


def jsonfriends(request):
    friends = Friend.objects.all()
    a = []
    dd = {}
    for i in friends:
        dd = {'name': i.name, 'link': i.link}
        a.append(dd)
    d = {'friend': a}
    return JsonResponse(json.dumps(d, ensure_ascii=False),safe=False)
