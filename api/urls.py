from django.urls import path
from .views import *

urlpatterns = [
    path('snippets/overview/', SnippetOverviewAPIView.as_view(), name='snippet-overview'),
    path('snippets/create/', SnippetCreateAPIView.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/', SnippetDetailAPIView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/update/', SnippetUpdateAPIView.as_view(), name='snippet-update'),
    path('snippets/<int:pk>/delete/', SnippetDeleteAPIView.as_view(), name='snippet-delete'),
]
