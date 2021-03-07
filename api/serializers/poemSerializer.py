from rest_framework import serializers
from api.models.poems.models import Poems

class PoemSerializer(serializers.ModelSerializer):
    def create(self, validated_data):    
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        return instance
    class Meta:
        model = Poems
        fields ='__all__'