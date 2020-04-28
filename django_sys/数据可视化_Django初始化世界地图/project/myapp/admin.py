from django.contrib import admin

# Register your models here.
from .models import Grades, Students


class StudentsInfo(admin.TabularInline):  # StackedInline
    model = Students
    extra = 2

@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表页
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    # 过滤字段
    list_filter = ['gname']
    search_fields = ['gname']
    # 分页
    list_per_page = 5
    # 修改页
    # fields = []
    fieldsets = [
        ("num", {"fields": ['ggirlnum', 'gboynum']}),
        ("base", {"fields": ['gname', 'gdate', 'isDelete']}),
    ]

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):

    # 列表页
    list_display = ['pk', 'sname', 'sgender', 'sage', 'scontend', 'isDelete']
    # 过滤字段
    list_filter = ['sname']
    search_fields = ['sname']
    # 分页
    list_per_page = 5


# admin.site.register(Grades, GradesAdmin)
# admin.site.register(Students, StudentsAdmin)