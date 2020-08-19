from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

import magic


class MimetypeValidator(object):
    def __init__(self, mimetypes, message=None, code='file-type'):
        self.mimetypes = mimetypes
        self.message = message
        self.code = code

    def __call__(self, value):
        try:
            mime = magic.from_buffer(value.read(1024), mime=True)
            if not mime in self.mimetypes:
                if not self.message:
                    raise ValidationError(_('%s is not an acceptable file type') % value, code=self.code)
                else:
                    raise ValidationError(_(self.message), code=self.code)
        except AttributeError as e:
            raise ValidationError('This value could not be validated for file type' % value, code='file-type')


class FileSizeValidator(object):
    """
    Validates file size in bytes
    """

    def __init__(self, size):
        self.size = size

    def __call__(self, value):
        if value.size > self.size:
            raise ValidationError(_('File size must be less than %s kb') % (self.size / 1024), code='file-size')


alpha = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ-]+$",
    _('ALPHA_REQUIRED'),
)


alpha_space = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ- ]+$",
    _('ALPHA_SPACE_REQUIRED'),
)


alpha_space_quote = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ- ']+$",
    _('ALPHA_SPACE_QUOTE_REQUIRED'),
)

alphanum = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ0-9-]+$",
    _('ALPHANUM_REQUIRED'),
)

# todo: use PhoneField when possible instead
phone_number = validators.RegexValidator(
    r"^[\d\(\)\s.\-+]+$",
    _('PHONE_NUMBER_REQUIRED')
)

alphanum_underscore = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ0-9-_]+$",
    _('ALPHANUM_UNDERSCORE_REQUIRED'),
)

alphanum_space = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ0-9- ]+$",
    _('ALPHANUM_SPACE_REQUIRED'),
)


alphanum_space_quote = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ0-9- ']+$",
    _('ALPHANUM_SPACE_QUOTE_REQUIRED'),
)

alphanum_space_quote_underscore = validators.RegexValidator(
    r"^[a-zA-ZÀ-ÿ0-9-_ ']+$",
    _('ALPHANUM_SPACE_QUOTE_UNDERSCORE_REQUIRED'),
)

# street, city
location_name = validators.RegexValidator(
    r"^([a-zA-ZÀ-ÿ0-9 ']|[-_.,])+$",
    _('LOCATION_NAME_VALIDATION'),
)

#  use positive look ahead to see if at least one case letter exists (lemonway restriction)
company_name = validators.RegexValidator(
    r"^(?=.*[a-zA-ZÀ-ÿ])([a-zA-ZÀ-ÿ0-9 ']|[\"!@#$%.,-_])+$",
    _('COMPANY_NAME_VALIDATION'),
)

# https://en.wikipedia.org/wiki/VAT_identification_number
company_idcode = validators.RegexValidator(
    r"^[a-zA-Z0-9 ]+$",
    _('COMPANY_IDCODE_VALIDATION'),
)


url_no_unsafe_chars = validators.RegexValidator(
    r"^[^\s\\<>\{\}]+$",
    _('SAFE_VALIDATION'),
)

no_unsafe_chars = validators.RegexValidator(
    r"^[^\\/&<>\{\}]+$",
    _('SAFE_VALIDATION'),
)

filename = validators.RegexValidator(
    r"^[^<>:;,?\"*|]+$",
    _('FILENAME_VALIDATION'),
)


# currencies [\u20A0-\u20CF]+
safe_text = validators.RegexValidator(
    r"^([\u20A0-\u20CF]|[a-zA-ZÀ-ÿ\d\s]|['\"`~*.,;\\\/\?\!:@&=+,\-_\(\)\[\]])+$",
    _('SAFETEXT_VALIDATION'),
)

# subset of safe_text
safe_text_title = validators.RegexValidator(
    r"^([\u20A0-\u20CF]|[a-zA-ZÀ-ÿ\d ]|['\".,\?\!:@=+,\-_\(\)\[\]])+$",
    _('SAFETEXT_VALIDATION'),
)
