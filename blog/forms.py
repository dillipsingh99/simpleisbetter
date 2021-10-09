from django import forms
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from nepali_datetime_field.models import NepaliDateField


class CommentForm(forms.Form):
    comment = forms.CharField(widget=CKEditorUploadingWidget())

    

        