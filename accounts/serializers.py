# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    
    
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    
   
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        
        fields = ('email', 'username', 'password', 'confirm_password')

    def validate(self, data):
       
        
        if data['password'] != data['confirm_password']:
            
            raise serializers.ValidationError({"confirm_password": "As senhas não coincidem."})
        
        data.pop('confirm_password') 
        
        return data 
    
    def create(self, validated_data):
        
        
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'], 
            password=validated_data['password']  
        )
        return user