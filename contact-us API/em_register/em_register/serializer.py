from rest_framework import serializers
from .models import em_register
class em_registerSerilaizer(serializers.ModelSerializer):
  class Meta:
    model=em_register
    fields=['id','your_name','your_email','subject','message']

def create(self, validated_data):
        Em_register = em_register.objects.create_user(validated_data['your_name'], validated_data['your_email'], validated_data['subject'],validated_data['message'])

        return Em_register