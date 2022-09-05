from django.urls import path, include
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'Incomes', views.IncomeListApiView)
# router.register('<int:id>', views.IncomeDetailApiView)


urlpatterns = [
    path('', views.IncomeListApiView.as_view(), name='incomes'),
    path('<int:id>', views.IncomeDetailApiView.as_view(), name='income'),
    # path('', include(router.urls)),
]