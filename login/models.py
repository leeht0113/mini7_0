from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 추가적인 사용자 프로필 필드를 여기에 추가할 수 있습니다.
