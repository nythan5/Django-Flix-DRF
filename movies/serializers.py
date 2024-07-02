from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers
from .models import Movie
from django.db.models import Avg


class MovieSerializer(ModelSerializer):
    # adicionando campos fora do MODEL, geralmente campo calculado
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    # django entende que funçoes que iniciam com VALIDATE,
    # sao funcoes que devem ser executadas para realizar validacoes.

    def validate_release_date(self, value):
        if value.year < 1990:
            raise ValidationError(
                'A data de lançamento não pode ser anterior a 1990')
        return value

    def validate_resume(self, value):
        if len(200) > 200:
            raise ValidationError(
                'O resumo nao deve ser maior do que 20 carácteres')
        return value

    def get_rate(self, obj):
        # aggregate serve para fazer um novo campo, por padrao ele coloca o nome do campo como stars__avg
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
