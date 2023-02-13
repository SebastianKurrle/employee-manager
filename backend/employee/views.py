from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from company.models import Company
from .models import Employee


class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    # to create an employee
    def post(self, request):
        self.check_permissions(request)

        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(status=200)

    # gets all employees from one company
    def get(self, request, comp_id):
        company = Company.objects.get(id=comp_id)
        employees = Employee.objects.filter(company=company)
        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data, status=200)

class EmployeeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # updates an employee
    def put(self, request, emp_id, comp_id):
        employee = Employee.objects.get(id=emp_id)
        company = Company.objects.get(id=comp_id)

        data = {
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'department': request.data['department'],
            'salary_per_hour': request.data['salary_per_hour'],
            'hours_per_week': request.data['hours_per_week'],
            'birthday': request.data['birthday'],
            'image': request.data['image'],
            'company': company.id
        }
        if employee.company != company:
            return Response(status=403)

        serializer = EmployeeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.update(employee, serializer.validated_data)
        return Response(status=200)

    # gets a single employee with an id
    def get(self, request, comp_id, emp_id):
        employee = Employee.objects.get(id=emp_id)
        company = Company.objects.get(id=comp_id)
        serializer = EmployeeSerializer(employee)

        if employee.company != company:
            return Response(status=403)

        return Response(serializer.data)
