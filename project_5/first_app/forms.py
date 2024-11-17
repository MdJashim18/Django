from django import forms 
from django.core import validators
class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total length must be within 70 charecters",required=False,widget=forms.Textarea(attrs = {'id' : 'text_area','class' : 'class1 class2' , 'placeholder' : 'Enter Your Name'}) )
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    Appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL , widget=forms.CheckboxSelectMultiple)
    # file = forms.FileField()

# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname)<10:
#     #         raise forms.ValidationError("Enter a name with at least 10 charecters")
#     #     return valname
#     # def clean_email(self):
#     #     valEmail = self.cleaned_data['email']
#     #     if '.com' not in valEmail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valEmail

#     def clean(self):
#         clean_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname)<10:
#             raise forms.ValidationError("Enter a name with at least 10 charecters")
    
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")


class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput , validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 charecters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid Email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message='Age must be at most 34'),validators.MinValueValidator(24,message='Age must be at least 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='File Extention must be ended with "pdf"')])


class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_compass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_compass!=val_pass:
            raise forms.ValidationError('Password does not matched')
        if len(val_name)<15:
            raise forms.ValidationError('Name must be at least 15 charecter')
        