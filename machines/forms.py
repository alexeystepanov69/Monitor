from django import forms
from django.forms import widgets
from django.forms.models import inlineformset_factory, modelformset_factory
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from .models import Reason, ClassifiedInterval, Equipment
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Code

class ReasonForm(forms.ModelForm):

    class Meta:
        model = Reason
        exclude = ['']


class EquipmentDetailForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Equipment
        fields = ['model']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }

    def save(self, commit=True):
        """
        prevent form from saving object
        :param commit:
        :return:
        """
        return self.instance


class ClassifiedIntervalForm(forms.ModelForm):
    class Meta:
        model = ClassifiedInterval
        fields = ['user_classification']

    def __init__(self, *args, **kwargs):
        super(ClassifiedIntervalForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            # self.fields['start'].widget.attrs['readonly'] = True
            if self.instance.automated_classification.is_working:
                self.fields['user_classification'].widget.attrs['class'] = 'hidden'


ClassifiedIntervalFormSet = modelformset_factory(ClassifiedInterval, form=ClassifiedIntervalForm,
                                                 extra=0, can_delete=False)

# Регистрация пользователей
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    phone=forms.CharField(label="Телефон",max_length=12)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        if cd['first_name'] =='' or cd['last_name'] =='' or  cd['email'] =='':
            raise forms.ValidationError('Все поля обязательны для заполнения!')
        if cd['email'] !='':
            cd['username']=cd['email']
        return cd['password2']


#Создание пользователя неактивным(становится активным после подтверждения кода безопасности)
@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.is_active = False

	#Редактирование профиля
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone',)

# Подтверждение кода безопасности
class CodeForm(forms.ModelForm):
    user_id=forms.CharField()
    class Meta:
        model = Code
        fields = ('code',)

#Подтверждение кода безопасности через телефон
class PhoneCodeForm(forms.Form):
    user_id=forms.CharField()