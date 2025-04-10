from django.urls import path
from .views import *

urlpatterns = [
    path('snippets/overview/', SnippetOverviewAPIView.as_view(), name='snippet-overview'),
    path('snippets/create/', SnippetCreateAPIView.as_view(), name='snippet-create'),
]
