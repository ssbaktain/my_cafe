from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu # 모델 설정
        fields = ('item','size','temp','price','sajin') # 필드 설정