from django.shortcuts import render, redirect,get_object_or_404
from .models import Assigned, addAssigned, addBillable
from django.http import HttpResponse
from resource.models import Details
from django.contrib import messages

def _Assigned_id(request):
    assign = request.session.session_key
    if not assign:
        assign = request.session.create()
    return assign


def Assign(request, id):
    
    # already_assigned = Assigned.objects.filter(detail_id=id)
    # already_billed = Billable.objects.filter(detail_id=id)
    current_user = request.user
    if current_user.is_authenticated:
        resource = Details.objects.get(id=id)
        try:
            assign_re = Assigned.objects.get(detail_id=_Assigned_id(request))
        except Assigned.DoesNotExist:
            assign_re= Assigned.objects.create(detail_id=_Assigned_id(request))
        assign_re.save()
        try:
            assign_resource_billed = addBillable.objects.filter(resource=resource, user=current_user)
            print(assign_resource_billed)
            if assign_resource_billed.exists():
                messages.error(request, "already billed")
                return redirect('/resources')
            assign_resource = addAssigned.objects.get(resource=resource, user=current_user)
            assign_resource.save()
            messages.error(request, "already Assigned")
        except addAssigned.DoesNotExist:
            assign_resource = addAssigned.objects.create(
                resource=resource,
                user=current_user,
                assigned=assign_re,
            )
            messages.success(request, "Resource Assigned Successfully")
            assign_resource.save()
        return redirect('/resources')
    # else:
    #     resource = Details.objects.get(id=id)
    #     try:
    #         assign_re = Assigned.objects.get(detail_id=_Assigned_id(request))
    #     except Assigned.DoesNotExist:
    #         assign_re= Assigned.objects.create(detail_id=_Assigned_id(request))
    #     assign_re.save()
    #     try:
    #         assign_resource = addAssigned.objects.get(resource=resource, assigned=assign_re)
    #     except addAssigned.DoesNotExist:
    #         assign_resource = addAssigned.objects.create(
    #             resource=resource,
    #             user=current_user,
    #             assigned=assign_re,
    #         )
    #         assign_resource.save()
    #     return redirect("/resources")
    # if already_assigned or already_billed:
    #     return render(request,"already_assigned.html")
    # else:
    #     resource = Details.objects.get(id=id)
        # assign = Assigned.objects.create(detail_id=id)
        # assign.save()
    #     data = addAssigned.objects.create(resource=resource, assigned=assign)
    #     data.save()

def AssignRemove(request,id):
    assign = Assigned.objects.get(detail_id=_Assigned_id(request))
    resource = get_object_or_404(Details, id=id)
    assigned_resource = addAssigned.objects.get(resource=resource, assigned=assign)
    assigned_resource.delete()
    messages.success(request, "Resource Removed Successfully")
    return redirect('/resources')

def billable(request, id):
    current_user = request.user
    if current_user.is_authenticated:
        resource = Details.objects.get(id=id)
        try:
            assign_resource = addAssigned.objects.filter(resource=resource, user=current_user)
            if assign_resource.exists():
                assign_resource_bill = addBillable.objects.create(
                resource=resource,
                user=current_user,
                )
                assign_resource_bill.save()
                messages.success(request, "Resource Billed Successfully")
                assign = Assigned.objects.get(detail_id=_Assigned_id(request))
                resource = get_object_or_404(Details, id=id)
                assigned_resource = addAssigned.objects.get(resource=resource, assigned=assign)
                assigned_resource.delete()
        except addAssigned.DoesNotExist:
           messages.error(request, 'You must assign Resource First')
        return redirect('/resources')
    else:
        return redirect('login')
    # already_billed = Billable.objects.filter(detail_id=id)
    # if already_billed:
    #     return render(request,"already_billed.html")
    # else:
    #     assign = Assigned.objects.filter(detail_id=id)
    #     if assign:
    #         resource = Details.objects.get(id=id)
    #         billed = Billable.objects.create(detail_id=id)
    #         billed.save()
    #         data = addBillable.objects.create(resource=resource, Billed=billed)
    #         data.save()
    #         assign = Assigned.objects.get(detail_id=id)
    #         assign.delete()
    #     else:
    #         return redirect("/")
    # return redirect('/')

def billRemove(request,id):
    current_user= request.user
    resource = get_object_or_404(Details, id=id)
    assigned_resource = addBillable.objects.get(resource=resource, user=current_user)
    assigned_resource.delete()
    messages.success(request, "Resource Removed Successfully")
    return redirect('/resources')

    # billed = Billable.objects.get(detail_id=id)
    # billed.delete()
    # return redirect('/')
