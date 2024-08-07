from rest_framework import serializers
from api.models import Items

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'