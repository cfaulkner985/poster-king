from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Configuration file for the checkout app"""
    name = 'checkout'

    def ready(self):
        import checkout.signals
