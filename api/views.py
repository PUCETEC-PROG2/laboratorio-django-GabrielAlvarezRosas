from rest_framework import viewsets
from rest_framework.response import Response
from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer    

    requiered_scopes = ['write']

    #def get_permissions(self):
     #   if self.request.method in ['GET', 'POST', 'PUT', 'DELETE']

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer    

    requiered_scopes = ['write']