from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    serializer_by_action = {}

    def get_serializer_by_action(self):
        return self.serializer_by_action.get(self.action)

    def get_serializer_class(self):
        return self.get_serializer_by_action() or super().get_serializer_class()
