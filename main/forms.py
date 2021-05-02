from django import forms
from django.core.mail import send_mail
import logging
from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm
)
from django.contrib.auth.forms import UsernameField
from . import models


logger = logging.getLogger(__name__)


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = models.User
        fields = ("email",)
        field_classes = {"email": UsernameField}

    def send_mail(self):
        logger.info(
            f"Sending signup email for email={self.cleaned_data['email']}"

        )
        message = f"Welcome {self.cleaned_data['email']}"
        send_mail(
            "Welcome to BookTime",
            message,
            "site@booktime.domain",
            [self.cleaned_data["email"]],
            fail_silently=True,
        )


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(max_length=600, widget=forms.Textarea)

    def send_mail(self):
        logger.info("Sending email to customer service")
        message = f"From: {self.cleaned_data['name']}\n{self.cleaned_data['message']}"
        send_mail(
            "Site message",
            message,
            'site@booktime.domain',
            ['customerservice@booktime.domain'],
            fail_silently=False
        )
