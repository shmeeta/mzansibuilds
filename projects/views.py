from django.shortcuts import render

# Create your views here.
def starting_page(request): 
    return render(request, "projects/index.html")

def projects(request): 
    pass

def project_detail(request):
    pass