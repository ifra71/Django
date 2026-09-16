from django.db import models

from .validators import validate_file_size


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    profile = models.OneToOneField("Profile", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to="profile_pictures/")
    role = models.CharField(
        max_length=150,
        choices=[("Manager", "Manager"), ("QA", "QA"), ("Developer", "Developer")],
    )
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.role


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    team_members = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=200,
        choices=[
            ("Open", "Open"),
            ("Review", "Review"),
            ("Working", "Working"),
            ("Awaiting releease", "Awaiting Release"),
            ("waiting QA", "Waiting Qa"),
        ],
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    assignee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Document(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to="documents/", validators=[validate_file_size])
    version = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateField()

    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
