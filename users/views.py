from django.shortcuts import render

def get_users_page(request):
    return render(request, 'users/index.html')
