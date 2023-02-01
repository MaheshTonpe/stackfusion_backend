from rest_framework import serializers
from app.models import User
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    # def validate_email_id(self):
    #     email = self.validated_data.get("email_id")
    #     if "@" not in email or "." not in email:
    #         raise serializers.ValidationError("Invalid email")
    #     return email

    def validate_dob(self, dob):
        dob = self.initial_data.get("dob")
        current_date = datetime.now()
        formated_dob = datetime.strptime(dob, "%Y-%m-%d")
        diff = current_date - formated_dob
        
        REQUIRED_AGE_ABOVE_18 = 365 * 18
        
        if diff.days < REQUIRED_AGE_ABOVE_18:
            raise serializers.ValidationError("Invalid date of birth!")
        return dob


    def validate_phone_no(self, phone_no):
        phone_no = self.initial_data.get("phone_no")
        if len(str(phone_no)) != 10 or not str(phone_no).isdigit():
            raise serializers.ValidationError("Invalid phone number!")
        return phone_no

    class Meta:
        model = User 
        fields = "__all__"

    