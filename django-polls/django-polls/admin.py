from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3
        


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["publication_date", "question_text"]   # --> this will make publication_date appear above question_text
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["publication_date"]}),
    ]
    inlines = [ChoiceInline]

    list_display = ("question_text", "publication_date", "was_published_recently")
    list_filter = ["publication_date"]
    search_fields = ["question_text"]
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)  


