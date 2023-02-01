from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from app.models import User
from app.serializers.userSerializers import UserSerializer
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

class UserView(ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        result = map_user_objects(queryset)
        return Response(result)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = User.objects.create(**serializer.data)
        
        """send email"""
        subject = "Successfully registered!"
        body = request.data
        message = '\n'.join(str(i) for i in body.values())
        
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [serializer.data.get("email_id")], fail_silently=True)
        except BadHeaderError:
            return HttpResponse("Invalid header found.")

        return Response(transform_singal(obj))

    def edit(self, request, pk):
        row = User.objects.get(pk=pk)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        row.name = serializer.data.get("name")
        row.dob = serializer.data.get("dob")
        row.email_id = serializer.data.get("email_id")
        row.phone_no = serializer.data.get("phone_no")
        row.save()
        return Response("Updated!")


    def retrieve(self, request, pk):
        row = self.queryset.get(pk=pk)
        row = transform_singal(row)
        return Response(row)


    def destroy(self, request, pk):
        row = User.objects.get(pk=pk)
        row.delete()
        return Response("Successfully deleted!")


def transform_singal(instance):
    data_dict = {}
    data_dict["id"] = instance.id
    data_dict["name"] = instance.name
    data_dict["dob"] = instance.dob
    data_dict["email_id"] = instance.email_id
    data_dict["phone_no"] = instance.phone_no
    return data_dict


def map_user_objects(data):
    return map(transform_singal, data)

