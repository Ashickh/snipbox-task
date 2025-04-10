from rest_framework import serializers
from .models import Snippet

class SnippetOverviewSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='snippet-detail', lookup_field='pk')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'detail_url']


from .models import Snippet, Tag

class SnippetCreateSerializer(serializers.ModelSerializer):
    tag_titles = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Snippet
        fields = ['title', 'note', 'tag_titles']

    def create(self, validated_data):
        tag_titles = validated_data.pop('tag_titles', [])
        user = self.context['request'].user
        snippet = Snippet.objects.create(created_by=user, **validated_data)

        for title in tag_titles:
            tag, _ = Tag.objects.get_or_create(title=title)
            snippet.tags.add(tag)

        return snippet


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class SnippetDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'tags']


class SnippetUpdateSerializer(serializers.ModelSerializer):
    tag_titles = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Snippet
        fields = ['title', 'note', 'tag_titles']

    def update(self, instance, validated_data):
        tag_titles = validated_data.pop('tag_titles', [])
        instance.title = validated_data.get('title', instance.title)
        instance.note = validated_data.get('note', instance.note)
        instance.save()

        tags = []
        for title in tag_titles:
            tag, _ = Tag.objects.get_or_create(title=title)
            tags.append(tag)
        instance.tags.set(tags)

        return instance


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
