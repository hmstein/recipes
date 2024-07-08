from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from data.models import Recipe
from .serializers import RecipeSerializer



#@api_view(['GET'])
#def get(request):
#    recipes = Recipe.objects.all()
#    serializer = RecipeSerializer(recipes, many=True)
#    return Response(serializer.data)

class RecipeViewSet(viewsets.ModelViewSet):
   queryset = Recipe.objects.all()
   serializer_class = RecipeSerializer
   authentication_classes = (TokenAuthentication, )
   permission_classes = (IsAuthenticatedOrReadOnly, )