from django.shortcuts import render
from .models import Transactions
from rest_framework.response import Response
from .serializers import TransactionsSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view()
def get_transactions(request):
    queryset=Transactions.objects.all()
    serializer=TransactionsSerializer(queryset,many=True)
    return Response({
        "data":serializer.data
    })
