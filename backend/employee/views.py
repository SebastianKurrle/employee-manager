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
