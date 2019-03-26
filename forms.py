from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone
from initiatives.models import Initi, Stages, Challenges, Risks, MainStage
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='كلمة المرور ')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'off'}), label='البريد الإلكتروني ', required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='اسم مدير المشروع ', required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='اسم المستخدم ', required=True,)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(user.password)  # set password properly before commit
        if commit:
            user.save()
        return user


class UpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete': 'off'}), label='البريد الإلكتروني ',
                             required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='اسم مدير المشروع ',
                                 required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='اسم المستخدم ',
                               required=True, )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']

        labels = {
            "first_name": "اسم مدير المشروع",
            "username": "اسم المستخدم ",
            "email": "البريد الإلكتروني",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'get'
            self.helper.add_input(Submit('submit', 'Save person'))


class InitiativeForm(forms.ModelForm):
    mub_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='اسم المشروع ',
                               required=True, )
    class Meta:
        model = Initi
        fields = ['mub_name', 'leader']
        labels = {
            "mub_name": "اسم المشروع ",
            "leader": "مدير المشروع  ",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Save person'))


class InitiativeUpdateForm(forms.ModelForm):

    class Meta:
        model = Initi
        fields = ['mub_name', 'leader']
        labels = {
            "mub_name": "اسم المشروع ",
            "leader": "مدير المشروع  ",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'get'
            self.helper.add_input(Submit('submit', 'Save person'))


class UpdateStage(forms.ModelForm):
    stage = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='المرحلة ', required=True)
    ratio = forms.IntegerField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='الوزن ', required=True)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'autocomplete': 'off'}),label='تاريخ الانتهاء ', required=True)

    class Meta:
        model = Stages
        fields = ['stage', 'ratio', 'end_date']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'get'
            self.helper.add_input(Submit('submit', 'Save person'))


class UpdateChallenge(forms.ModelForm):
    challenge = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='التحدي ', required=True)
    owner = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='المالك ', required=True)
    status = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='الحالة ', required=True)
    info = forms.CharField(label='التفاصيل ', required=True)

    class Meta:
        model = Challenges
        fields = ['challenge', 'owner', 'status', 'info']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'get'
            self.helper.add_input(Submit('submit', 'Save person'))


class UpdateRisks(forms.ModelForm):
    RELEVANCE_CHOICES = (
        (10, ("10")),
        (20, ("20")),
        (30,("30")),
        (40, ("40")),
        (50,("50")),
        (60, ("60")),
        (70, ("70")),
        (80, ("80")),
        (90, ("90")),
        (100, ("100")),
    )

    RELEVANCE2_CHOICES = (
        ("منخفض", ("منخفض")),
        ("متوسط",("متوسط")),
        ("عالي", ("عالي"))
    )

    risk = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='الخطر ', required=True)
    owner_risk = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='المالك ', required=True)
    probability = forms.ChoiceField(choices=RELEVANCE_CHOICES, required=True, label='الاحتمالية ')
    influence = forms.ChoiceField(choices=RELEVANCE2_CHOICES, label='التأثير ', required=True)
    plan = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='خطة العمل ', required=True)

    class Meta:
        model = Risks
        fields = ['risk', 'owner_risk', 'probability', 'influence', 'plan']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'get'
            self.helper.add_input(Submit('submit', 'Save person'))


class StageForm(forms.ModelForm):
        progress_num = forms.IntegerField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='الإنجاز الكلي ', required=True)
        info = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='خطة العمل ', required=True)
        final_rate = forms.FloatField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='تقدم المرحلة ', required=True)

        class Meta:
            model = MainStage
            fields = ['report', 'stage', 'end_date', 'ratio', 'progress_num', 'info', 'final_rate']
            helper = FormHelper()
            helper.form_tag = False

        def __init__(self, *args, **kwargs):
            super(StageForm, self).__init__(*args, **kwargs)
            self.fields['stage'].widget.attrs['readonly'] = True
            self.fields['stage'].label = 'المرحلة'
            self.fields['report'].widget.attrs['readonly'] = True
            self.fields['report'].label = 'التقرير'
            self.fields['ratio'].widget.attrs['readonly'] = True
            self.fields['ratio'].label = 'وزن المرحلة '
            self.fields['end_date'].widget.attrs['readonly'] = True
            self.fields['end_date'].label = 'تاريخ الإنتهاء '
            self.fields['progress_num'].widget.attrs['onchange'] = 'myfunc()'


class UpdateStageForm(forms.ModelForm):

    progress_num = forms.IntegerField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='الإنجاز الكلي ', required=True)
    final_rate = forms.FloatField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='تقدم المرحلة ', required=True)
    info = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='خطة العمل ', required=True)

    class Meta:
        model = MainStage
        fields = ['report', 'stage', 'ratio', 'end_date', 'progress_num', 'final_rate', 'info']
        helper = FormHelper()
        helper.form_tag = False

    def __init__(self, *args, **kwargs):
        super(UpdateStageForm, self).__init__(*args, **kwargs)
        self.fields['stage'].disabled = True
        self.fields['stage'].label = 'المرحلة'
        self.fields['report'].disabled = True
        self.fields['report'].label = 'التقرير'
        self.fields['ratio'].disabled = True
        self.fields['ratio'].label = 'التقرير'
        self.fields['ratio'].label = 'وزن المرحلة '
        self.fields['ratio'].disabled = True
        self.fields['end_date'].label = 'تاريخ الإنتهاء '
        self.fields['progress_num'].widget.attrs['onchange'] = 'myfunc()'


