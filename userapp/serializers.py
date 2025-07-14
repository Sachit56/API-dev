from rest_framework import serializers
from django.contrib.auth import authenticate,get_user_model
from .models import *


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True
    )

    class Meta:
        model = User
        fields = ['email','first_name','last_name','faculty','age','email','password','file']

    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists.')
        return value

    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password,**validated_data)
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email','password']

    def validate(self,data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email,password=password)

            if not user:
                raise ValueError('No User exists')
        else:
            raise serializers.ValidationError('Include you valid Email and Password')
        
        data['user'] = user

        return data
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['student_id','email','first_name','last_name','faculty','age','file']
        read_only_fields = ['email','faculty']


class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class WheelSpecificationFormSerializer(serializers.ModelSerializer):
    fields = WheelSpecificationSerializer()

    class Meta:
        model = WheelSpecificationForm
        fields = ['formNumber','submittedBy','submittedDate','fields']

    def create(self,validate_data):
        fields_data = validate_data.pop('fields')
        field_instance = WheelSpecification.objects.create(**fields_data)
        wheel_form = WheelSpecificationForm.objects.create(fields = field_instance,**validate_data)
        return wheel_form
    

class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoggieDetails
        fields = '__all__'

class BogieCheckSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieCheckSheet
        fields = '__all__'

class BmbcCheckSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmbcChecksheet
        fields = '__all__'

class BogieFormSerializer(serializers.ModelSerializer):
    bogieDetails = BogieDetailsSerializer()
    bogieChecksheet = BogieCheckSheetSerializer()
    bmbcChecksheet = BmbcCheckSheetSerializer()

    class Meta:
        model = BogieForm
        fields = ['formNumber','inspectionBy','inspectionDate','bogieDetails','bogieChecksheet','bmbcChecksheet']

    def create(self,validated_data):
        bogieDetails_data = validated_data.pop('bogieDetails')
        bogieChecksheet_data = validated_data.pop('bogieChecksheet')
        bmbcChecksheet_data = validated_data.pop('bmbcChecksheet')

        bogie_details = BoggieDetails.objects.create(**bogieDetails_data)
        bogie_checksheet = BogieCheckSheet.objects.create(**bogieChecksheet_data)
        bmbc_checksheet = BmbcChecksheet.objects.create(**bmbcChecksheet_data)

        bogie_form = BogieForm.objects.create(bogieDetails = bogie_details,bogieChecksheet = bogie_checksheet,bmbcChecksheet = bmbc_checksheet,**validated_data)

        return bogie_form