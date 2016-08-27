from .models import Message
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # using a special response on delete as per project spec
        content = { 'success': True }
        return Response(content, status=status.HTTP_200_OK)
