from django.shortcuts import render

# Create your views here.
def mmain(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'view/about.html')
def category(request):
    return render(request, 'view/category.html')
def contact(request):
    return render(request, 'view/contact.html')
def search_result(request):
    return render(request, 'view/search-result.html')
def single_post(request):
    return render(request, 'view/single-post.html')
def Politics_keyword1(request):
    return render(request, 'view/Politics-keyword1.html')
