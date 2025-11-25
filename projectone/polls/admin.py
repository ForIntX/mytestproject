from django.contrib import admin
from .models import Course,Category
from django.utils.text import slugify
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","date","slug","category_list","imageUrl")
    list_display_links =("title","slug",)
    list_filter = ("title","date","isActive",)
    search_fields = ("title","description","date",)
    #readonly_fields = ("slug",)
    
    

    def category_list(self,course):
        html = ""
        for category in course.categories.all():
            html += category.name + " | "

        return html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","isActive","Course_count",)
    readonly_fields = ("slug",)


    def Course_count(self,obj):
        return obj.course_set.count()
    


