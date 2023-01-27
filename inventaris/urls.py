from django.urls import path
from inventaris import views

urlpatterns = [
    path('category', views.category.Index.as_view()),
    path('category/<id>', views.category.DetailCategory.as_view()),
    path('inventory', views.inventory.Main.as_view()),
    path('inventory/<id>', views.inventory.DetailInventory.as_view()),
    path('staff', views.staff.Main.as_view()),
    path('staff/<id>', views.staff.DetailStaff.as_view()),
    path('maintenance', views.maintenance.Main.as_view()),
    path('maintenance/<id>', views.maintenance.DetailMaintenance.as_view())
]