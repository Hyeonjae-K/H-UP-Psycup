from django.contrib import admin

from api.models import Test, Question, Answer, Result

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
