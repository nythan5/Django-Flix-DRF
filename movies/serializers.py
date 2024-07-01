from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Movie


class MovieSerializer(ModelSerializer):
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
