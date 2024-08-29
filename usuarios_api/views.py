
from rest_framework.decorators import api_view
from rest_framework.response import Response
from usuarios_api.serializers import UserSerializer,LoginSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from usuarios_api.models import UserProfile
from django.contrib.auth import authenticate


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = UserProfile.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({ 'token': token.key, 'user': user.username})
        else:
            return Response({'error': 'Las credenciales son incorrectas...'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def profile(request):
    return Response({})
