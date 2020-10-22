from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Function for displaying the users profile

    Args:
        request: HTTP request object

    Returns:
        This returns the users profile and if the user updates the
        profile then they will let them know they have been successful
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Function for displaying the order history

    Args:
        request: HTTP request object
        order_number: order number passed into the function

    Returns:
        This returns the order history which will display the previous
        order from a exsisting customer when logged in. This will display
        the information relating to the order and can be clicked on to
        see further details.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


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
