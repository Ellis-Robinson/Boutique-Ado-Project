from django.shortcuts import render

def index(request):
    ''' loads home index page '''
    
    return render(request, 'home/index.html')