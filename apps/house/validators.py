from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

ENIValidator = validators.RegexValidator(
    r'^\d{10}$',
    message=_(
        "The UNI code must consist of 10 digits ***",
    ),
    code="invalid_eni"
)


def validate_youtube_url(request_text):
    if "youtube.com" not in request_text and "youtu.be" not in request_text:
        raise ValidationError(
            "Введите действительный YouTube URL"
        )
