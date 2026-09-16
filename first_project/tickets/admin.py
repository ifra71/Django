from django.contrib import admin

from .models import Comment, Document, Profile, Project, Task, User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Document)
admin.site.register(Comment)
