from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MunicipalPortal 
from .serializers import *

@api_view(['GET'])
def customers_list(request):
    """
 List municipal portal.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = MunicipalPortal.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = MunicipalPortalSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        
        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/municipalportal/?page=' + str(nextPage), 'prevlink': '/api/municipalportal/?page=' + str(previousPage)})