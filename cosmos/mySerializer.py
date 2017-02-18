from django.core.serializers.python import Serializer


#Module to override build-in serializer so we don't expose model metadata
class MySerialiser(Serializer):
    def end_object(self, obj):
        self._current['id'] = obj._get_pk_val()
        self.objects.append(self._current)