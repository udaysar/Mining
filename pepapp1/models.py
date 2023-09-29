from django.db import models

class Stocks(models.Model):
    name= models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

# class Businesses(models.Model):
#     name=models.CharField(max_length=100)
#     location=models.CharField(max_length=100)
#     description=models.TextField()


#     def __str__(self):
#         return self.name

# class Promotions(models.Model):
#     title=models.CharField(max_length=100)
#     description=models.TextField()
#     start_date=models.DateField
#     end_date=models.DateField()

#     def __str__(self):
#         return self.title

