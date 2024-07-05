from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework import serializers
from .models import Movie
from django.db.models import Avg
from genres.serializer import GenreSerializer
from actors.serializers import ActorSerializer


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


class MovieDetailSerializer(ModelSerializer):
    # adicionando campos fora do MODEL, geralmente campo calculado
    rate = serializers.SerializerMethodField(read_only=True)

    # Quando temos tabelas com muitos relacionamentos alguns campos relacionais não trazem os dados dos objetos,
    # eles apenas retornam o seu respectivo ID. Para sanar este problema podemos utilizar SERIALIZERS
    # dinamicos para quando estivermos fazendo requisição GET tenhamos acesso a atributos como
    # name, description etc..
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)  # aqui vai vir mais de 1 objeto por isso many True

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        # aggregate serve para fazer um novo campo, por padrao ele coloca o nome do campo como stars__avg
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
