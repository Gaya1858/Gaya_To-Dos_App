from rest_framework import serializers
from todo.models import Todo

"""
    We extend DRF's Modelserializer into a Todoserializer class. Modelserializer provides an API
    to create serializers from your models.
"""


class TodoSerializer(serializers.ModelSerializer):
    # autopopulated by app. User can't manipulate
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    """
        Class Meta: we specity our database model Todo and the fielss we want to expose
        REST Framework magically transforms our data into JSON, exposing these field from our Todo model.
    """

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'completed']
