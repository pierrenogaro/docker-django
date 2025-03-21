from django.shortcuts import render
def home_page(request):
    return render(request, 'website/home.html')

def other_page(request):
    return render(request, 'website/other_page.html')