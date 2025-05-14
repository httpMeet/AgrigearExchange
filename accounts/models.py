from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .managers  import CustomUserManager
from django.utils import timezone
from locations.models import district_master, state_master

# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True,unique=True)
    ROLE_CHOICES = (
        ('FARMER', 'FARMER'),
        ('Equipment Owner','Equipment Owner')
    )
    username = None
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(_("email"), unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    role = models.CharField(choices=ROLE_CHOICES, blank=True, default='ADMIN', max_length=20) 
    address = models.CharField(max_length=255,blank=True,null=True)
    district = models.ForeignKey(district_master,to_field='district_name',null=True,blank=True,on_delete=models.PROTECT,related_name="district")
    state = models.ForeignKey(state_master,to_field='state_name',null=True,blank=True,on_delete=models.PROTECT,related_name="state")

    profile_image = models.ImageField(null=True, blank=True, upload_to="profile_images/",default="profile_images/default.png")
    
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'address']
    USERNAME_FIELD = "email"
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_user = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


