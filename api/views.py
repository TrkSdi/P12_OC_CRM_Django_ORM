from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import CustomUser
from api.serializers import UserSerializer

@api_view(['GET'])
def getUser(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)