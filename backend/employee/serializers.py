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
            'get_image'
        )

    def create(self, validated_data):
        fist_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        birthday = validated_data.get('birthday')
        department = validated_data.get('department')
        salary_per_hour = validated_data.get('salary_per_hour')
        hours_per_week = validated_data.get('hours_per_week')
        image = validated_data.get('image')
        comp_id = validated_data.get('comp_id')
        company = Company.objects.get(id=comp_id)

        # creates the employee
        employee = Employee.objects.create(fist_name=fist_name, last_name=last_name, birthday=birthday,
        department=department, salary_per_hour=salary_per_hour, hours_per_week=hours_per_week,
        image=image, company=company)

        return employee

