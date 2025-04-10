from rest_framework import serializers
from .models import Snippet

class SnippetOverviewSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='snippet-detail', lookup_field='pk')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'detail_url']
