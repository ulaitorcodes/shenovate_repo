from rest_framework import serializers
from .models import Membership

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        fields = [
            "full_name",
            "email", 
            "phone", 
            "address", 
            "area_of_interest", 
            "hdyhau", 
            "why"
        ]

        extra_kwargs = {
            "full_name" : {"required" : True},
            "email" : {"required" : True}, 
            "phone" : {"required" : True}, 
            "address" : {"required" : True}, 
            "area_of_interest" : {"required" : True}, 
            "hdyhau" : {"required" : True}, 
            "why" : {"required" : True},
        }