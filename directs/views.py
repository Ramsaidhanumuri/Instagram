from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from directs.models import Message
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=user, reciepient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
        
    context = {
        'directs':directs,
        'active_direct':active_direct,
        'messages':messages,
    }

    return render(request, 'inbox.html', context)

@login_required
def Directs(request, username):
    user = request.user
    messages = Message.get_message(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, reciepient__username=username)
    directs.update(is_read=True)

    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0
        
    context = {
    'directs':directs,
    'active_direct':active_direct,
    'messages':messages,
    }

    return render(request, 'directs.html', context)

def SendMessage(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == 'POST':
        to_user = User.objects.get(username=to_user_username)
        Message.send_message(from_user, to_user, body)
        return redirect('inbox')

@login_required
def UserSearch(request):
    query = request.GET.get('q')
    context = {}

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Pagination
        paginat = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = Paginator.get_page(paginat, page_number)

        context = {
            'users': users_paginator
        }

    return render(request, 'search.html', context)