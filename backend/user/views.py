from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from django.contrib.auth.models import User


# check if the username in lowercase exists
def check_lower_username_exists(username):
    users = User.objects.all()
    for user in users:
        if user.username.lower() == username:
            return True

    return False


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info' : {
            'id' : user.id,
            'username': user.username
        },

        'token' : token
    })


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username').lower()

    if check_lower_username_exists(username):
        return Response({'error' : 'This username already exists'}, status=400)

    serializer.save()
    return Response(status=200)


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username
            }
        })

    return Response({'error': 'not authenticated'}, status=40)
