from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils import timezone
import uuid
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**fields):
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user  = self.model(email=email,**fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**fields):
        fields.setdefault('is_staff',True)
        fields.setdefault('is_superuser',True)

        return self.create_user(email,password,**fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email       = models.EmailField(unique=True)
    student_id  = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20)
    faculty     = models.CharField(max_length=50)
    age         = models.PositiveIntegerField()
    file       = models.FileField(null=True,upload_to='uploads')
    is_staff    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','faculty','age','file']

    def __str__(self):
        return self.email


class WheelSpecification(models.Model):
    treadDiameterNew = models.CharField(max_length=100)
    lastShopIssueSize = models.CharField(max_length=100)
    condemningDia = models.CharField(max_length=100)
    wheelGauge = models.CharField(max_length=100)
    variationSameAxle = models.CharField(max_length=100)
    variationSameBogie = models.CharField(max_length=100)
    variationSameCoach = models.CharField(max_length=100)
    wheelProfile = models.CharField(max_length=100)
    intermediateWWP = models.CharField(max_length=100)
    bearingSeatDiameter = models.CharField(max_length=100)
    rollerBearingOuterDia = models.CharField(max_length=100)
    rollerBearingBoreDia = models.CharField(max_length=100)
    rollerBearingWidth = models.CharField(max_length=100)
    axleBoxHousingBoreDia = models.CharField(max_length=100)
    wheelDiscWidth = models.CharField(max_length=100)

class WheelSpecificationForm(models.Model):
    formNumber = models.CharField(max_length=100,unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.OneToOneField(WheelSpecification,on_delete=models.CASCADE)

class BoggieDetails(models.Model):
    bogieNo = models.CharField(max_length=100)
    makerYearBuilt = models.CharField(max_length=100)
    incomingDivAndDate = models.CharField(max_length=100)
    deficitComponents = models.CharField(max_length=100,default=None)
    dateOfIOH = models.DateField()

class BogieCheckSheet(models.Model):
    bogieFrameCondition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolsterSuspensionBracket = models.CharField(max_length=100)
    lowerSpringSeat = models.CharField(max_length=100)
    axleGuide = models.CharField(max_length=100)

class BmbcChecksheet(models.Model):
    cylinderBody = models.CharField(max_length=100)
    pistonTrunnion = models.CharField(max_length=100)
    adjustingTube = models.CharField(max_length=100)
    plungerSpring = models.CharField(max_length=100)

class BogieForm(models.Model):
    formNumber = models.CharField(max_length=100,unique=True)
    inspectionBy  = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bogieDetails = models.OneToOneField(BoggieDetails,on_delete=models.CASCADE)
    bogieChecksheet = models.OneToOneField(BogieCheckSheet,on_delete=models.CASCADE)
    bmbcChecksheet = models.OneToOneField(BmbcChecksheet,on_delete=models.CASCADE)

