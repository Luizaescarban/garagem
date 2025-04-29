from rest_framework.viewsets import ModelViewSet

from core.models import Acessorio
from core.serializers import AcessorioSerizalizer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerizalizer
