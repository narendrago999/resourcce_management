from django.urls import path
from .views import *
urlpatterns = [
    path('assign/<int:id>', Assign, name="Assign"),
    path('billable/<int:id>', billable, name="billable"),
    path('assign-remove/<int:id>', AssignRemove, name="AssignRemove"),
    path('billed-remove/<int:id>', billRemove, name="billRemove"),
]
