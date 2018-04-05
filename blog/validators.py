from django.core.exceptions import ValidationError


def validate_justin(value):
    if 'justin' not in value:
        raise ValidationError('Not justin')
    return value

