"""Profile Forms"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    """
    class Meta:
        """Get UserProfile model, choose fields to display"""

        model = UserProfile
        exclude = ('user', 'active_subscription', 'subscription')


class UpdateUserForm(UserChangeForm):
    """
    Form for editing user information.

    """

    password = None

    class Meta:
        """Get User model, choose fields to display"""

        model = User
        fields = ["username", "first_name", "last_name"]
        help_texts = {"username": None}
