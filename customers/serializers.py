from rest_framework import serializers
from .models import MunicipalPortal

...
class MunicipalPortalSerializer(serializers.ModelSerializer):

    class Meta:
        model = MunicipalPortal 
        fields = ('pk','name', 'link', 'createdAt')