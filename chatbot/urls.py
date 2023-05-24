from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('history', views.history_view, name='history-view'),
    path('delete/<record_id>', views.delete_record, name='delete-record'),
]
