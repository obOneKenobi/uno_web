# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Web

# create a serializer class
class WebSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Web
        fields = ('id', 'title','description','completed')