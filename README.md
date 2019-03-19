#  Django Validators

Django validators provides validator function that can be used with Django form fields and Django rest framework 
serializer fields

### Installation

Install `django-validators` using `pip`

`pip install django-validators`

### Types of validators

#### File validators

- **Mime type validator** `djangovalidators.validators.MimetypeValidator`

    This validator is used to check mime type/ content type of the uploaded file. This validator checks file header 
    information to check mime type on `FileField`
    
    example
    
    ```python
    from djangovalidators.validators import MimetypeValidator
    
    # with django forms
    class DemoForm(forms.Form):
        CONTENT_TYPES = ('image/png', 'application/pdf', 'image/jpeg', 'image/jpg', 'image/tiff',)
        file_object = forms.FileField(validators=[MimetypeValidator(CONTENT_TYPES)])
        
    # with django serializers
    class DemoSerializer(serializers.Serializer):
        CONTENT_TYPES = ('image/png', 'application/pdf', 'image/jpeg', 'image/jpg', 'image/tiff',)
        FILE_SIZE_IN_BYTES = 1024 * 1024 * 5  # ~5 Mib
        file_object = serializers.FileField(validators=[MimetypeValidator(CONTENT_TYPES)])
    ```

- **File size validator** `djangovalidators.validators.FileSizeValidator`

    This validator is useful for validating file size in `FileField`
    
    example
    
    ```python
    from djangovalidators.validators import FileSizeValidator
  
    # with django forms
    class DemoForm(forms.Form):
        FILE_SIZE_IN_BYTES = 1024 * 1024 * 5  # ~5 Mib
        file_object = forms.FileField(validators=[FileSizeValidator(FILE_SIZE_IN_BYTES)])
        
    # with django serializers
    class DemoSerializer(serializers.Serializer):
        FILE_SIZE_IN_BYTES = 1024 * 1024 * 5  # ~5 Mib
        file_object = serializers.FileField(validators=[FileSizeValidator(FILE_SIZE_IN_BYTES)])
    ```