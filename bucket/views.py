from django.shortcuts import render

def get_bucket_page(request):
    return render(request, 'index.html')