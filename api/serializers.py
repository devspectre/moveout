from rest_framework import serializers
from .models import Moveout

class MoveoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Moveout
		fields = '__all__'