from rest_framework.response import Response
from rest_framework.decorators import api_view
from data.models import Recipe
from .serializers import RecipeSerializer

@api_view(['GET'])
def getData(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)