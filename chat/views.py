from django.shortcuts import render, redirect

# Create your views here.

def ChatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    return render(request, "chat/ChatPage.html", context={})

