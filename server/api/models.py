from django.db import models
from django.utils import timezone


class Test(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    thumbnail = models.ImageField(
        upload_to='thumbnails/', null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions',
                             on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='question_images/', null=True, blank=True)
    question = models.CharField(max_length=256)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='answer_images/', null=True, blank=True)
    answer = models.CharField(max_length=64, null=True, blank=True)
    score = models.IntegerField()

    def __str__(self):
        return self.answer


class Result(models.Model):
    test = models.ForeignKey(Test, related_name='results',
                             on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='result_images/', null=True, blank=True)
    result = models.CharField(max_length=256)
    lower = models.IntegerField()
    upper = models.IntegerField()

    def __str__(self):
        return self.result
