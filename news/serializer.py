from attr import field
from rest_framework import serializers
from .models import Articles

class ArticlesSerialize(serializers.ModelSerializer):
    class Meta:
        model = Articles
        field = ('title', 'cat')
