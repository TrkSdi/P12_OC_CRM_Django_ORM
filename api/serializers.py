from rest_framework import serializers
from user.models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'role',]