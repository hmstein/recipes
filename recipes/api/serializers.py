from rest_framework import serializers
from data.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    ingredients = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'steps', 'ingredients', 'blurb', 'credits', 'created']