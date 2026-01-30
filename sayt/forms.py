from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, EmailInput
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from django.contrib.auth.models import User



from .models import Contact,Profile

class CustomUserRegistrationForm(UserCreationForm):
    # Qo'shimcha maydonlar
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form__input',
        'placeholder': 'Email manzilingiz'
    }))

    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Ism va familiya'
    }))

    class Meta:
        model = User
        # Username bu yerda bo'lishi shart!
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Foydalanuvchi nomi'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Parol maydonlariga stil berish
        self.fields['password1'].widget.attrs.update({
            'class': 'form__input',
            'placeholder': 'Parol yarating'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form__input',
            'placeholder': 'Parolni tasdiqlang'
        })

    # MUHIM: full_name ma'lumotini ism va familiyaga ajratib saqlash
    def save(self, commit=True):
        user = super().save(commit=False)
        # Ism va familiyani ajratamiz (masalan: "Ali Valiyev" -> first_name="Ali", last_name="Valiyev")
        full_name = self.cleaned_data.get('full_name')
        name_parts = full_name.split(' ', 1)

        user.first_name = name_parts[0]
        if len(name_parts) > 1:
            user.last_name = name_parts[1]

        if commit:
            user.save()
        return user





class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'full_name', 'username', 'phone', 'email']

        widgets = {
            'avatar': forms.FileInput(attrs={
                'id': 'file',
                'accept': 'image/*',
                'onchange': 'loadFile(event)',
                'style': 'display: none;'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Ism va Familiya'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Username'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Telefon raqam'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form__input',
                'placeholder': 'Email manzil'
            }),
        }



class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label="Eski parol",
        widget=forms.PasswordInput(),
        strip=False,
    )
    new_password1 = forms.CharField(
        label="Yangi parol",
        widget=forms.PasswordInput(),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Yangi parolni tasdiqlash",
        widget=forms.PasswordInput(),
        strip=False,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        # Orbit/Bootstrap ko‘rinishi
        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "autocomplete": "off",
            })

        self.fields["old_password"].widget.attrs.update({"autocomplete": "current-password"})
        self.fields["new_password1"].widget.attrs.update({"autocomplete": "new-password"})
        self.fields["new_password2"].widget.attrs.update({"autocomplete": "new-password"})

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError("Eski parol noto‘g‘ri.")
        return old_password

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("new_password1")
        p2 = cleaned.get("new_password2")

        if p1 and p2 and p1 != p2:
            self.add_error("new_password2", "Yangi parollar mos kelmadi.")

        if p1:
            try:
                password_validation.validate_password(p1, self.user)
            except ValidationError as e:
                self.add_error("new_password1", e)

        return cleaned

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data["new_password1"])
        if commit:
            self.user.save(update_fields=["password"])
        return self.user





class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # HTML'dagi textarea name='message' bo'lgani uchun fields'ga 'message'ni ham qo'shdim
        fields = ['full_name', 'email', 'message']

        labels = {
            'full_name': 'Ismingiz',
            'email': 'Email',
            'message': 'Xabar',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form__input',
                'placeholder': 'Ism familiya'
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'class': 'form__input',
                'placeholder': 'example@mail.com'
            }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'class': 'form__input',
                'rows': '4',
                'placeholder': 'Loyihangiz haqida yozing...'
            }),
        }

