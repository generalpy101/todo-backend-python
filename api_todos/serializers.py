from dataclasses import field
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault
from .models import Todo, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TodoSerializer(ModelSerializer):
    tags = TagSerializer(many=True,required = False,read_only = True)

    class Meta:
        model = Todo
        fields = '__all__'
        #depth = 1

    def to_internal_value(self, data):
        for tag_name in data.get('tags', []):
            Tag.objects.get_or_create(name=tag_name)
        return super().to_internal_value(data)

    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user
        tags_list = self.context.get("request").data.get("tags",[])
        validated_data["tags"] = []
        for tag in tags_list:
            t = Tag.objects.get(name=tag)
            validated_data["tags"].append(t.id)
            
        return super().create(validated_data)
