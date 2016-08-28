from .models import Message
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_destroy(self, instance):
        instance.delete()
        content = { 'success': True }
        return Response(content, status=status.HTTP_200_OK)
