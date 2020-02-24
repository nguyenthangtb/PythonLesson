from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers

#models
from .models import Post
from .models import User

from rest_framework import filters

# Định nghĩa model cần serialize và các trường. ở đây mình để là all.
# Có rất nhiều API class mà rest đã viết sẵn. ở đây mình chỉ dùng 2 class để thao tác CRUD với database. 
class PostListSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
    
        if 'django' not in value.lower():
        	raise serializers.ValidationError("Blog post is not about Django")
        return value
    class Meta:
        model = Post
        fields = '__all__'


# API get detail, update, delete
class PostDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'id'
    #permission_classes = permissions.IsAuthenticated


# API get list and create
class PostListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):
    search_fields  = ['title']
    filter_backends = (filters.SearchFilter,)

    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


#Users
# Có rất nhiều API class mà rest đã viết sẵn. ở đây mình chỉ dùng 2 class để thao tác CRUD với database. 
#CORS_ORIGIN_ALLOW_ALL = True
class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


# API get detail, update, delete
class UserDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'
    #permission_classes = permissions.IsAuthenticated


# API get list and create
class UserListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserListSerializer

   