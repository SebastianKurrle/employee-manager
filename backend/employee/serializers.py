from rest_framework.serializers import ModelSerializer
from .models import Employee
from company.models import Company


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'birthday',
            'department',
            'salary_per_hour',
            'hours_per_week',
            'image',
            'company',
            'get_image'
        )

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        birthday = validated_data.get('birthday')
        department = validated_data.get('department')
        salary_per_hour = validated_data.get('salary_per_hour')
        hours_per_week = validated_data.get('hours_per_week')
        image = validated_data.get('image')
        company = validated_data.get('company')

        # creates the employee and checks
        employee = Employee.objects.create(first_name=first_name, last_name=last_name, birthday=birthday,
                                           department=department, salary_per_hour=salary_per_hour,
                                           hours_per_week=hours_per_week,
                                           company=company)

        if image is not None:
            employee.image = image
            employee.save()

        return employee

