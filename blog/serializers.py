from rest_framework import serializers
from .models import Post, Category, Tag, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'slug']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'short_description',
                  'thumbnail', 'slug', 'category', 'tags', 'created_at']

    def create(self, validated_data):
        category = validated_data.pop('category')
        tags = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        cate = Category.objects.filter(name=category['name'])
        if cate:
            cat = cate[0]
            post.category.add(*cat)
        else:
            newcat = Category.objects.create(name=category['name'])
            post.category.add(*newcat)
            print(newcat)

        for tag in tags:
            if Tag.objects.filter(name=tag['name']):
                print(tag)
                return post.tags.add(*tag)
            else:
                newtag = Tag.objects.create(name=tag['name'])

        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
