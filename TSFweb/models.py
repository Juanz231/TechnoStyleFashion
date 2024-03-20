from django.db import models

class User(models.Model):
    name: str = models.CharField(max_length=255)
    phoneNumber: int = models.IntegerField()
    emailAddress: str = models.CharField(max_length=255)
    address: str = models.CharField(max_length=255)
    
    def login():
        return
    
    def go_to_menu():
        return
    
    def sign_in():
        return

class Search(models.Model):
    productoSearch: str = models.CharField(max_length=255)
    menu: list = models.JSONField(default=list)
    
    def go_to_menu():
        return
    
    def go_to_shop():
        return
    
    def get_product():
        return
    
class Shops(models.Model):
    nameShop: str = models.CharField(max_length=255)
    phoneNumberShop: int = models.IntegerField()
    address: str = models.CharField(max_length=255)
    
    def product_verification():
        return
    
    def product():
        return
    
class ShoppingCart(models.Model):
    shopsSelect: list = models.JSONField(default=list)
    bill: str = models.CharField(max_length=255)
    products: list = models.JSONField(default=list)
    postalCode: str = models.CharField(max_length=255)
    address: str = models.CharField(max_length=255)
    
    def pay():
        return
    
    def add_shop():
        return
    
    def delay_shop():
        return
    
    def change_address():
        return
    
    def schedule_sale():
        return
    
class Simulations(models.Model):
    avatar = models.CharField(max_length=255)
    products: list = models.JSONField(default=list)
    
    def add_product():
        return
    
    def set_avatar():
        return
    
    def bill_simulation():
        return
    
class Pays(models.Model):
    paypal: str = models.CharField(max_length=255)
    creditCard: int = models.IntegerField()
    
    def pay_verification():
        return
    
    def add_card():
        return
    
class Delivery(models.Model):
    addressUser: str = models.CharField(max_length=255)
    nameUser: str = models.CharField(max_length=255)
    
    def transport():
        return
    
    def pick_it_up():
        return

# Create your models here.
