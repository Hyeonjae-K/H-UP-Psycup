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
        fields = ('question')


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'description', 'create_date')


class ContentSerializer(serializers.ModelSerializer):
    content = QuestionSerializer(many=True, read_only=True, source='questions')
    result = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('id', 'contents', 'results')
