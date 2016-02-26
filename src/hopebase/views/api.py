from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework import generics

from hopebase import serializers, permissions
from hopebase.models import UserProfile


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [getattr(permissions, p) for p in settings.PROFILE_PERMS]
    required_scopes = ['update-profile']
    model = UserProfile
    serializer_class = serializers.UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
