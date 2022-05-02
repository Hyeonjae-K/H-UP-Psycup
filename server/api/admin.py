from django.contrib import admin
import nested_admin

from api.models import Test, Question, Answer, Result


class ResultInline(nested_admin.NestedStackedInline):
    model = Result
    extra = 1


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    extra = 1


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]


class TestAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'thumbnail', 'create_date']})
    ]
    inlines = [QuestionInline, ResultInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
