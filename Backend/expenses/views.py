from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ExpenseSerializer

from .models import Expense

from rest_framework import permissions

from .permissions import IsOwner

# Create your views here.
class ExpenseListApiView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)


class ExpenseDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = "id"

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)