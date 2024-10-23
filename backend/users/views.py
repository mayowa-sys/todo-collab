from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permisson_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'user': serializer.data,
            'message': 'User Created Successfully'
        }, headers=headers
        )

    def perform_create(self, serializer):
        return serializer.save()
    
    @action(detail=False, methods=['get', 'put'], permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        profile = request.user.profile
        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK) 
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED) 
    
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def token_verify(selfl, request):
        token = request.data.get('token')
        if not token:
            return Response({'detail': "Token is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            TokenVerifyView.as_view()(request)
            return Response({'detail': 'Token is valid'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)