from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, default=None)
    no_of_guests = models.IntegerField(default=0)
    bookingdate = models.DateTimeField()

    class Meta:
        db_table = "booking"

class MenuItem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    class Meta:
        db_table = "menu"

    
