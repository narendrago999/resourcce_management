from django.db import models
from resource.models import Details
from accounts.models import Account
class Assigned(models.Model):
    detail_id = models.CharField( max_length=50)
    assign_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.detail_id
class addAssigned(models.Model):
    user = models.ForeignKey(Account,null=True, on_delete=models.CASCADE)
    resource = models.ForeignKey(Details, on_delete=models.CASCADE)
    assigned = models.ForeignKey(Assigned, on_delete=models.CASCADE, null=True) 


class addBillable(models.Model):
    user = models.ForeignKey(Account,null=True, on_delete=models.CASCADE)
    resource = models.ForeignKey(Details, on_delete=models.CASCADE) 

   
    