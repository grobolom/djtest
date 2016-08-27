from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('message_text')
