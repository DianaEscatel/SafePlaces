from django.urls import path
import views
from .views import get_all_places, get_place, update_place, delete_place, create_place
urlpatterns = [
    path('spapp/', get_all_places, name='get_all_places'),
    path('spapp/<int:place_id>/', get_place, name='get_place'),
    path('spapp/update/<int:place_id>/', update_place, name='update_place'),
    path('spapp/delete/<int:place_id>/', delete_place, name=delete_place),
    path('spapp/create/', create_place, name=create_place),
]