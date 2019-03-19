from django.core.exceptions import ValidationError
import magic
from django.utils.translation import ugettext as _


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
