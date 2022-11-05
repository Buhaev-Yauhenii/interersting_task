"""
Serializers for user API
"""
from django.contrib.auth import (get_user_model, authenticate)
from django.utils.translation import gettext as _
import json
from rest_framework import serializers
from django.db.models import F
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    """serializer for model User"""
    category_for_change = serializers.CharField(max_length = 255, required=False, allow_blank=True)
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name', 'balance', 'categories','category_for_change']
        extra_kwargs = {
                'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """create and return user with encrypted data"""
        validated_data['categories'] = "Здоровье и фитнес, Машина"
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Method for updateing user data"""
        
        password = validated_data.pop('password', None)
        categories = validated_data.pop('categories',None)
        category_for_change_from_validated_data = validated_data.pop('category_for_change', None)
        user = super().update(instance, validated_data)
        all_categories = [cat.strip() for cat in user.categories.split(',')]

        if password:
            user.set_password(password)
            user.save()
        if category_for_change_from_validated_data:    
            all_categories[all_categories.index(category_for_change_from_validated_data)] = categories
            User.objects.filter(email=user.email).update(categories= ','.join(all_categories))
        if not category_for_change_from_validated_data and categories:
            # new_categories = user.categories + f', {categories}'
            User.objects.filter(email=user.email).update(categories= new_categories)
        
            
           
            
            

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
