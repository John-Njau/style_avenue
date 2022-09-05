from django.urls import path, include
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'expenses', views.ExpenseListApiView)
# router.register('<int:id>', views.ExpenseDetailApiView)


urlpatterns = [
    path('', views.ExpenseListApiView.as_view(), name='expenses'),
    path('<int:id>', views.ExpenseDetailApiView.as_view(), name='expense'),
    # path('', include(router.urls)),
]