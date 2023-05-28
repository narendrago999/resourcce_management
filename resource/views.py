from django.shortcuts import render
from resource.models import Details
from assign.models import addAssigned, addBillable
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def Resource(request):
    user = request.user
    Course = Details.objects.all()
    assigned = addAssigned.objects.filter(user=user)
    billable = addBillable.objects.filter(user=user)
    data = {
        'data':Course,
        'assigned': assigned,
        'billable': billable    
    }

    return render(request, 'resources.html', data)

def availableResource(request):
    Course = Details.objects.all()
    assigned = addAssigned.objects.all()
    billable = addBillable.objects.all()
    data = {
        'data':Course,
        'assigned': assigned,
        'billable': billable    
    }

    return render(request, "index.html", data)

