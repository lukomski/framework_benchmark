from django.contrib.auth.models import User, Group
from rest_framework import serializers
from fwbm.serializers.collision import *
from fwbm.serializers.blog import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']