from rest_framework import serializers
from .models import Review

# index
class ReviewListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = ('id', 'title', )


# comment index
class CommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('article',)


# detail
class ArticleSerializer(serializers.ModelSerializer):
  commens = CommentSerializer(many=True, read_only=True)
  comment_count = serializers.IntegerField(source='comments.count', read_only=True)

  class Meta:
    model = Article
    fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comment_count', )