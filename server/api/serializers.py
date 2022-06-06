from rest_framework import serializers

from api.models import Test, Question, Answer, Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class TestDetailSerializer(serializers.ModelSerializer):
    contents = QuestionSerializer(
        many=True, read_only=True, source='questions')
    # results = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = '__all__'


class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = '__all__'
