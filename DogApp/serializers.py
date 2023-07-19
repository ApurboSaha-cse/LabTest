from rest_framework import serializers
from .models import DogShop

class DogShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogShop
        fields = [
            'id',
            'name',
            'price',
            'breed'
            'description',
        ]


