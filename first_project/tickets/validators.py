from django.core.exceptions import ValidationError


def validate_file_size(file):
    if file.size > 5 * 1024 * 1024:
        raise ValidationError("File size must be 5MB OR less ")
