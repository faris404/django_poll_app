from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to Pollster admin"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ('Date info', {"fields": ['pub_date'], "classes":['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)