from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField( max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name
    


