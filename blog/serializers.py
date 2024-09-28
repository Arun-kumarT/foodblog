from rest_framework import serializers
from blog.models import Category,Post,Comment
from fuzzywuzzy import fuzz
# class CategorySerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)

#     class Meta:
#         fields=["name"]
        
#     def create(self,validated_data):
#         return Category.objects.create(**validated_data)
    
#     def update(self,instance, validated_data):
#         instance.name=validated_data.get("name",instance.name)
#         instance.save()
#         return instance


class CategorySerializer(serializers.ModelSerializer):
    profile_len=serializers.SerializerMethodField()
    profile_fuzz=serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name',"profile_len","profile_fuzz"]
    def get_profile_len(self,obj):
        return len(obj.profile)
    def get_profile_fuzz(self,obj):
        return fuzz.ratio(obj.profile,"Arun")

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'comments', 'created_at', 'updated_at']
