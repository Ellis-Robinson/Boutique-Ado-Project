from django.shortcuts import render

def shopping_bag(request):
    ''' loads page with users shopping bag '''
    
    return render(request, 'bag/bag.html')
