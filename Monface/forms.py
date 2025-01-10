from django import forms 
from Monface.models import Person, Student, Employee

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Entrez votre adresse email',
            'style': '''
                width: 100%;
                padding: 14px;
                border: 2px solid #e8e8e8;
                border-radius: 25px;
                font-size: 14px;
                margin-bottom: 4px;
                outline: none;
                transition: border-color 0.3s ease;
            '''
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Créez un mot de passe',
            'style': '''
                width: 100%;
                padding: 14px;
                border: 2px solid #e8e8e8;
                border-radius: 25px;
                font-size: 14px;
                margin-bottom: 4px;
                outline: none;
                transition: border-color 0.3s ease;
            '''
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            Result = Person.objects.filter(password=password, email=email)
            if len(Result) != 1:
                raise forms.ValidationError("Adresse ou mot de pas incorrects.")
        return cleaned_data

class StudentProfilForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('Amis',)
        labels = {  
            'date_naissance': '',
            'name': '',
            'prenom': '',
            'email': '',
            'tlf': '',
            'password': '',
            'faculty': 'Faculty ',
            'annee': '',
            'cursus': 'Cursus ',
        }
        widgets = {
            'date_naissance': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Nom',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            "prenom": forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Prenom',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Email',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            "tlf": forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Numero de telephone',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
                'password': forms.PasswordInput(attrs={
                    'class': 'form-input',
                    'placeholder': 'Entre votre Mot de passe',
                    'style': '''
                        width: 100%;
                        padding: 14px;
                        border: 2px solid #e8e8e8;
                        border-radius: 25px;
                        font-size: 14px;
                        margin-bottom: 4px;
                        outline: none;
                        transition: border-color 0.3s ease;
                    '''
                }),
                'faculty': forms.Select(attrs={
                    'class': 'form-input',
                    'style': '''
                        width: 88%;
                        padding: 14px;
                        border: 2px solid #e8e8e8;
                        border-radius: 25px;
                        font-size: 14px;
                        margin-bottom: 4px;
                        outline: none;
                        transition: border-color 0.3s ease;
                    '''
                }),
                "annee" : forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder': 'Annee',
                    'style': '''
                        width: 100%;
                        padding: 14px;
                        border: 2px solid #e8e8e8;
                        border-radius: 25px;
                        font-size: 14px;
                        margin-bottom: 4px;
                        outline: none;
                        transition: border-color 0.3s ease;
                    '''
                }),
                'cursus': forms.Select(attrs={
                    'class': 'form-input',
                    'style': '''
                        width: 88%;
                        padding: 14px;
                        border: 2px solid #e8e8e8;
                        border-radius: 25px;
                        font-size: 14px;
                        margin-bottom: 4px;
                        outline: none;
                        transition: border-color 0.3s ease;
                    '''
                }),
                
        }

class EmployeeProfilForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('Amis',)
        labels = {  
            'date_naissance': '',
            'name': '',
            'prenom': '',
            'email': '',
            'tlf': '',
            'password': '',
            'faculty': 'Faculty ',
            'office': '',
            'campus': 'Campus ',
            'job': 'Job ',
        }
        fields = ['name', 'prenom', 'date_naissance', 'email', 'tlf', 'faculty', 'password', 'office', 'campus', 'job']
        widgets = {
            'date_naissance': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Nom',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            "prenom": forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Prenom',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Email',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            "tlf": forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Numero de telephone',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            'faculty': forms.Select(attrs={
                'class': 'form-input',
                'style': '''
                    width: 88%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Mot de passe',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            'office': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Entre votre Bureau',
                'style': '''
                    width: 100%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            'campus': forms.Select(attrs={
                'class': 'form-input',
                'style': '''
                    width: 86%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),
            'job': forms.Select(attrs={
                'class': 'form-input',
                'style': '''
                    width: 92%;
                    padding: 14px;
                    border: 2px solid #e8e8e8;
                    border-radius: 25px;
                    font-size: 14px;
                    margin-bottom: 4px;
                    outline: none;
                    transition: border-color 0.3s ease;
                '''
            }),

            
        }

