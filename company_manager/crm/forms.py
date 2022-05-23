from django.forms import ModelForm, ValidationError
from crm.models import Employee, Company
from django.contrib.auth.models import User
from django.forms import CharField
from django.contrib.auth.forms import UserCreationForm


class CompanyForm(ModelForm):
    def clean_identification_number(self):
        identification_number = self.cleaned_data["identification_number"]

        if len(identification_number) != 8:
            raise ValidationError("Identification number has incorrect length!")
        return identification_number

    class Meta:
        model = Company
        fields = ["name", "status", "phone_number", "email", "identification_number"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ("department", "phone_number")


class RegisterUserForm(UserCreationForm):
    username = CharField(label="Email")

    class Meta:
        model = User
        fields = ("Username", "password1", "password2")
