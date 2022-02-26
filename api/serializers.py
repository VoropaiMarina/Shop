from rest_framework import serializers

from ..main.models import Notebook


class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = ('diagonal', 'display_type')