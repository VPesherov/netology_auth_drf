from django_filters import DateFromToRangeFilter, FilterSet

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    ### ???
    created_at = DateFromToRangeFilter(field_name='created_at')

    filterset_fields = ['creator', 'status', 'created_at']

    #     permission_classes = [IsOwner]

    def get_permissions(self):
        # print(self.action)
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", 'destroy']:
            # print('jas')
            return [IsOwner()]
        return []
