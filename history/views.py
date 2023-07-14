from django.http import JsonResponse
from .models import History
from .serializers import HistorySerializer
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def history(request):
    if request.method == 'GET':
        history = History.objects.all()
        serializer = HistorySerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer=HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return redirect('history')


