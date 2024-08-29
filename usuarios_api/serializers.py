from rest_framework import serializers
from usuarios_api.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'is_student', 'is_teacher']
        extra_kwargs = {
           'password': {'write_only': True}
       }
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get( 'password')
        
        if not email or not password:
            raise serializers.ValidationError('Debe proporcionar ambos campos...')
        
        return data




