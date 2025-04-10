from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Snippet
from .serializers import *

class SnippetOverviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        snippets = Snippet.objects.filter(created_by=request.user)
        serializer = SnippetOverviewSerializer(snippets, many=True, context={'request': request})
        return Response({
            'total_snippets': snippets.count(),
            'snippets': serializer.data
        })


class SnippetCreateAPIView(CreateAPIView):
    serializer_class = SnippetCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
