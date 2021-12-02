from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    ''' loads view for all products '''
    products = Product.objects.all()
    query = None
    categories = None
    if request.GET:
        if 'category' in reuqest.GET:
            categories = request.get['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.filter(category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You did't enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': queries,
        'current_categories': categories,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    ''' loads view for products detials '''
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)