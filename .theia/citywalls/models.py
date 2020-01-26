from django.db import models

# All models :
class User(models.Model):
       username = models.CharField(max_length=45)
       password = models.CharField(max_length=45)
       email = models.EmailField()
       balance = models.DecimalField(max_digits=6, decimal_places=2)
       firstname = models.CharField(max_length=56)
       lastname = models.CharField(max_length=45)
       cellphone = models.CharField(max_length=14)
       address = models.CharField(max_length=255)
       town = models.CharField(max_length=45)
       post_code = models.CharField(max_length=45)
       country = models.CharField(max_length=45)

class Product(models.Model):
       CATEGORIES = (
           ('TEXT', 'Text'),
           ('PERS', 'Person'),
           ('ENVI', 'Environment'),
           ('JOKE', 'Joke'),
           ('FUT', 'Futuristic')
           ('GRAF', 'Grafitti')
       )

       title = models.CharField(max_length=255)
       image = models.ImageField()
       description = models.CharField(max_length = 500)
       quantity = models.IntegerField()
       category = models.CharField(
           max_length=2,
           choices=CATEGORIES
       )
       date_posted = models.DateTimeField(auto_now_add=True, blank=True)

class Auction(models.Model):
       product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
       number_of_bids = models.IntegerField()
       time_starting = models.DateTimeField()
       time_ending = models.DateTimeField()

class Watchlist(models.Model):
       user_id = models.ForeignKey(User, on_delete=models.CASCADE)
       auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

class Bid(models.Model):
       user_id = models.ForeignKey(User, on_delete=models.CASCADE)
       auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
       bid_time = models.DateTimeField()

class Chat(models.Model):
       auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
       user_id = models.ForeignKey(User, on_delete=models.CASCADE)
       message = models.TextField()
       time_sent = models.DateTimeField()