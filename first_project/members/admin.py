
from django.contrib import admin
from .models import Members, PremiumMembers, Course, Student

# admin.site.register(Members)
# admin.site.register(Course)
# admin.site.register(Student)


def make_18(modeladmin, request, queryset):
    queryset.update(age=18)

    
def delete_members(modeladmin, request, queryset):
    queryset.delete()

def count_members(modeladmin, request, queryset):
    print(queryset.count())

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):

    fields = ["name", "phone_number", "email", "age","nickname"]
    list_display = ["name", "email", "age","nickname"]
    list_filter = ["age"]
    search_fields = ["name", "email"]

    actions =[make_18, delete_members, count_members]


@admin.register(PremiumMembers)
class PremiumMembersAdmin(admin.ModelAdmin):
     list_display = ["name", "email", "age", "nickname"]
