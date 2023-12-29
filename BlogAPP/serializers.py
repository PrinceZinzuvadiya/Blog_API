from rest_framework import serializers
from .models import blogs

class blogserializers(serializers.ModelSerializer):
    class Meta:
        model=blogs
        fields='__all__'
        