from rest_framework import serializers

from api.models import Test, Question, Answer, Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('result', 'lower', 'upper')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer', 'score')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question', 'answers')


class ContentSerializer(serializers.ModelSerializer):
    contents = QuestionSerializer(
        many=True, read_only=True, source='questions')
    results = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('id', 'contents', 'results')


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'description', 'create_date')
