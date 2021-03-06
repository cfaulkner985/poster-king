from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category


def all_products(request):
    """ Function to show all products, including sorting and search queries

    Args:
        request: HTTP request object

    Returns:
        This returns all of the products information which includes the
        the sorting of the products into the different categories. It also
        returns the search results where a user will search for a product
        and it will bring up the search results relationg to the keyword
        that was typed in
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Function to show individual products details

    Args:
        request: HTTP request object
        product_id: product id passed into the function

    Returns:
        This returns the product detail template which will display the
        individual information of a product when selected in the main
        products page
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def handler404(request, exception):
    """ Handler for 404 errors

    Args:
        request: HTTP request object
        exception: exception raised

    Returns:
        Rendered 404 html
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """ Handler for 500 errors

    Args:
        request: HTTP request object

    Returns:
        Rendered 500 html
    """
    return render(request, '500.html', status=500)
