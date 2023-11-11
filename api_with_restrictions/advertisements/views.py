from django_filters import DateFromToRangeFilter, FilterSet
from django_filters import rest_framework

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    # filterset_fields = ['creator', 'status']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", 'destroy']:
            # print('jas')
            return [IsOwner()]
        return []
