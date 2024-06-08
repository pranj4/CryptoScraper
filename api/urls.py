from django.urls import path
from . import views
urlpatterns = [
    path('name',views.index),
    path('scraping_status/<str:job_id>', views.scraping_status, name='index'),
    path('start_scraping',views.start_scraping,name='start_scraping'),
]