from django.core.exceptions import ValidationError


def validate_author_email(value):
    if not '@' in value:
        raise ValidationError('Not a valid email')
    return value


def validate_kiran(value):
    if not 'kiran' in value:
        raise ValidationError('Not kiran')
    return value
