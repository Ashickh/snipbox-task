from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Snippet
from rest_framework.exceptions import PermissionDenied
from .serializers import *
from rest_framework import status

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


class SnippetDetailAPIView(RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to view this snippet.")
        return obj


class SnippetUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to update this snippet.")
        return obj

    def get_serializer_context(self):
        return {'request': self.request}



class SnippetDeleteAPIView(DestroyAPIView):
    queryset = Snippet.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to delete this snippet.")
        return obj

    def delete(self, request, *args, **kwargs):
        snippet = self.get_object()
        snippet.delete()

        remaining_snippets = Snippet.objects.filter(created_by=request.user)
        data = SnippetDetailSerializer(remaining_snippets, many=True).data
        return Response(data, status=status.HTTP_200_OK)
