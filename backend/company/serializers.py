from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'description',
            'get_absolute_url'
        )

    # creates a company
    def create(self, validated_data):
        name = validated_data.get('name')
        desc = validated_data.get('description')
        slug = name.lower()
        user = self.context.get('request').user

        company = Company.objects.create(name=name, description=desc, slug=slug, user=user)
        return company

