from rest_framework.serializers import ModelSerializer

from core.models import Acessorio


class AcessorioSerizalizer(ModelSerializer):
    class Meta:
        model: Acessorio
        fields = "__all__"
