from django.urls import path
from .views import employee_list, add_employee, edit_employee, delete_employee
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', employee_list, name = 'employee_list'),
    path('add/', add_employee, name = 'add_employee'),
    path('edit/<int:employee_id>/', edit_employee, name = 'edit_employee'),
    path('delete/<int:employee_id>/', delete_employee, name = 'delete_employee'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)