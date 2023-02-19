from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanySerializer
from .models import Company
from .permissons import IsOwner
from employee.models import Employee

class CompanyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.check_permissions(request)

        serializer = CompanySerializer(
            data=request.data,
            context = {
                'request' : request
            }
        )

        serializer.is_valid(raise_exception=True)

        # gets the slug to check if the name already exists
        slug = serializer.validated_data.get('name').lower()

        if Company.objects.filter(slug=slug, user=request.user).exists():
            return Response({'error' : 'This company name already exists'}, status=400)

        serializer.save()
        return Response(status=200)

    def get(self, request):
        companies = Company.objects.filter(user=request.user)
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)


class CompanyDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, comp_slug):
        self.check_permissions(request)

        # gets the company with the id
        company = Company.objects.filter(slug=comp_slug, user=request.user).first()
        if company == None:
            return Response(status=404)

        self.check_object_permissions(request, company)

        serializer = CompanySerializer(company)

        return Response(serializer.data)

    def delete(self, request, id):
        self.check_permissions(request)

        company = Company.objects.get(id=id)
        self.check_object_permissions(request, company)

        company.delete()
        return Response(status=204)


class CompanyCostsView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    # calculates the total costs from a company for the employees
    def get(self, request, comp_id):
        self.check_permissions(request)

        company = Company.objects.get(id=comp_id)

        self.check_object_permissions(request, company)

        employees = Employee.objects.filter(company=company)
        total_costs = sum(employee.get_absolute_salary() for employee in employees)

        return Response({'totalCosts': total_costs})
