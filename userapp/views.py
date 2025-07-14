from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics,status,permissions,viewsets
from django.contrib.auth import get_user_model
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# Create your views here.

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializers = LoginSerializer(data=request.data)
        try:
            if serializers.is_valid():

                user = serializers.validated_data['user']
                refresh_token = RefreshToken.for_user(user)

                return Response({
                    'refresh_token':str(refresh_token),
                    'access_token':str(refresh_token.access_token)
                })
            
            return Response({'serialier_error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        serializers = UserProfileSerializer(request.user)

        return Response({
            'users':serializers.data,
        },status=status.HTTP_200_OK)
    
class AllUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        users = User.objects.filter(faculty='software')
        serializers = UserProfileSerializer(users,many=True)

        return Response({
            'users':serializers.data
        },status=status.HTTP_200_OK)
    

class WheelSpecificationViewset(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    queryset = WheelSpecificationForm.objects.select_related('fields').filter(formNumber="WHEEL-2025-005")
    serializer_class = WheelSpecificationFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = WheelSpecificationFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = serializer.data.copy()
        data.pop('fields')

        return Response({
            "success": True,
            "message": "Wheel specification submitted successfully.", 
            "data":data,
            "status": "Saved" 
        })
    
class BogieCheckSheetViewset(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    queryset = BogieForm.objects.select_related('bogieDetails','bogieChecksheet','bmbcChecksheet').all()
    serializer_class = BogieFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = BogieFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = serializer.data.copy()

        data.pop('bogieDetails')
        data.pop('bogieChecksheet')
        data.pop('bmbcChecksheet')

        return Response({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": data,
            "status": "Saved" 
        })