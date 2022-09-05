from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'description', 'category', 'id']
        read_only_fields = ('id',)

        