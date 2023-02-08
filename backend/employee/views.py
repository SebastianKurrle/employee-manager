from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated


class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    # to create an employee
    def post(self, request):
        self.check_permissions(request)

        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(status=200)
