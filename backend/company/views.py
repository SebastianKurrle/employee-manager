from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanySerializer
from .models import Company

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

