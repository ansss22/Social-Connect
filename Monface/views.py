from django.shortcuts import render, redirect
from Monface.forms import EmployeeProfilForm, LoginForm, StudentProfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from Monface.models import Person, Student, Employee, Message

def login(request):
    if len(request.POST) > 0 :
        form=LoginForm(request.POST)
        if form.is_valid() :
            user_email=form.cleaned_data['email']
            logged_user=Person.objects.get(email=user_email)
            request.session['logged_user_id']=logged_user.id
            return redirect('/welcome')
        else :
            return render(request,'login.html',{'form':form}) 
    else : 
        loginform=LoginForm()
        return render(request,'login.html',{'form':loginform})

from django.shortcuts import render, redirect
from .forms import StudentProfilForm, EmployeeProfilForm

def register(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        if not user_type:
            return render(request, "user_profile.html", {"error": "Veuillez sélectionner un type d'utilisateur"})

        studentForm = StudentProfilForm(request.POST)
        employeeForm = EmployeeProfilForm(request.POST)

        if user_type == "student" and studentForm.is_valid():
            studentForm.save()  # Enregistrer les données de l'étudiant
            return redirect("/login/")
        elif user_type == "employee" and employeeForm.is_valid():
            employeeForm.save()  # Enregistrer les données de l'employé
            return redirect("/login/")
        else:
            return render(request, "user_profile.html", {
                "studentForm": studentForm,
                "employeeForm": employeeForm,
                "error": "Formulaire invalide"
            })
    else:
        studentForm = StudentProfilForm()
        employeeForm = EmployeeProfilForm()
        return render(request, "user_profile.html", {
            "studentForm": studentForm,
            "employeeForm": employeeForm,
        })

def index(request):
    return render(request ,'index.html')

def logout(request):
    auth_logout(request)  
    return redirect('/login')  # Redirection vers la page de connexion

def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        if len(Student.objects.filter(id=logged_user_id))==1 :
             return Student.objects.get(id=logged_user_id)
        elif len(Employee.objects.filter(id=logged_user_id))==1 :
            return Employee.objects.get(id=logged_user_id)
        else :
            return None 
    else :
        return None 
    
def welcome(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        statut_message = ""

        # Vérifiez si l'utilisateur est un étudiant
        if isinstance(logged_user, Student):
            if logged_user.annee == 1:
                statut_message = f"Étudiant en 1ère année {logged_user.cursus.titre}"
            elif logged_user.annee == 2:
                statut_message = f"Étudiant en 2ème année {logged_user.cursus.titre}"
            elif logged_user.annee == 3:
                statut_message = f"Étudiant en 3ème année {logged_user.cursus.titre}"
            else:
                statut_message = f"Étudiant en {logged_user.annee}ème année {logged_user.cursus.titre}"

        # Vérifiez si l'utilisateur est un employé
        elif isinstance(logged_user, Employee):
            statut_message = f"Employé(e) en tant que {logged_user.job.titre} au campus {logged_user.campus.nom}"

        # Publier un message
        if request.method == "POST" and request.POST.get("message"):
            contenu = request.POST.get("message")
            Message.objects.create(contenu=contenu, auteur=logged_user)

        # Récupérer les messages des amis et de l'utilisateur connecté
        amis = logged_user.Amis.all()
        messages = Message.objects.filter(auteur__in=list(amis) + [logged_user]).order_by("-date_publication")


        return render(request, 'welcome.html', {
            'logged_user': logged_user,
            'statut_message': statut_message,
            'messages': messages,
            'amis': amis,
           
        })
    else:
        return redirect('/login')
def add_friend(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user and request.method == "POST":
        ami_id = request.POST.get("ami_id")
        if ami_id:
            try:
                friend = Person.objects.get(id=ami_id)
                logged_user.Amis.add(friend)  # Ajoute l'ami
                return redirect('/welcome')  # Redirection vers la page d'accueil
            except Person.DoesNotExist:
                return redirect('/welcome')  # L'ami n'existe pas
    return redirect('/login')  # Si non connecté, redirection vers login

def profil(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        statut_message = ""  # Vous pouvez définir le statut ici si nécessaire
                # Vérifiez si l'utilisateur est un étudiant
        if isinstance(logged_user, Student):
            if logged_user.annee == 1:
                statut_message = f"Étudiant en 1ère année {logged_user.cursus.titre}"
            elif logged_user.annee == 2:
                statut_message = f"Étudiant en 2ème année {logged_user.cursus.titre}"
            elif logged_user.annee == 3:
                statut_message = f"Étudiant en 3ème année {logged_user.cursus.titre}"
            else:
                statut_message = f"Étudiant en {logged_user.annee}ème année {logged_user.cursus.titre}"

        # Vérifiez si l'utilisateur est un employé
        elif isinstance(logged_user, Employee):
            statut_message = f"Employé(e) en tant que {logged_user.job.titre} au campus {logged_user.campus.nom}"
        # Récupérer les messages
        messages = logged_user.message_set.all().order_by("-date_publication")
        return render(request, 'voir_profile.html', {
            'person': logged_user,
            'messages': messages,
            'logged_user': logged_user,
            'statut_message': statut_message,  # Passer le statut
        })
    else:
        return redirect('/login')

def modifier(request):
    logged_user = get_logged_user_from_request(request)
    if not logged_user:
        return redirect('/login')

    statut_message = ""  # Vous pouvez définir le statut ici si nécessaire
            # Vérifiez si l'utilisateur est un étudiant
    if isinstance(logged_user, Student):
        if logged_user.annee == 1:
                statut_message = f"Étudiant en 1ère année {logged_user.cursus.titre}"
        elif logged_user.annee == 2:
                statut_message = f"Étudiant en 2ème année {logged_user.cursus.titre}"
        elif logged_user.annee == 3:
                statut_message = f"Étudiant en 3ème année {logged_user.cursus.titre}"
        else:
                statut_message = f"Étudiant en {logged_user.annee}ème année {logged_user.cursus.titre}"

        # Vérifiez si l'utilisateur est un employé
    elif isinstance(logged_user, Employee):
            statut_message = f"Employé(e) en tant que {logged_user.job.titre} au campus {logged_user.campus.nom}"
    if isinstance(logged_user, Student):
        form = StudentProfilForm(instance=logged_user)
    elif isinstance(logged_user, Employee):
        form = EmployeeProfilForm(instance=logged_user)
    else:
        return redirect('/login')

    if request.method == 'POST':
        if isinstance(logged_user, Student):
            form = StudentProfilForm(request.POST, instance=logged_user)
        elif isinstance(logged_user, Employee):
            form = EmployeeProfilForm(request.POST, instance=logged_user)

        if form.is_valid():
            form.save()  # Save the updated user data
            return redirect('/welcome')

    return render(request, 'modifier_profile.html', {
        'form': form,
        'logged_user': logged_user,
        'statut_message': statut_message,  # Passer le statut
    })

def ajouter(request):
    logged_user = get_logged_user_from_request(request)
    if not logged_user:
        return redirect('/login')

    statut_message = ""  # Vous pouvez définir le statut ici si nécessaire
            # Vérifiez si l'utilisateur est un étudiant
    if isinstance(logged_user, Student):
        if logged_user.annee == 1:
                statut_message = f"Étudiant en 1ère année {logged_user.cursus.titre}"
        elif logged_user.annee == 2:
                statut_message = f"Étudiant en 2ème année {logged_user.cursus.titre}"
        elif logged_user.annee == 3:
                statut_message = f"Étudiant en 3ème année {logged_user.cursus.titre}"
        else:
                statut_message = f"Étudiant en {logged_user.annee}ème année {logged_user.cursus.titre}"

        # Vérifiez si l'utilisateur est un employé
    elif isinstance(logged_user, Employee):
            statut_message = f"Employé(e) en tant que {logged_user.job.titre} au campus {logged_user.campus.nom}"
    if request.method == "POST":
        ami_id = request.POST.get("ami_id")
        if ami_id:
            try:
                ami = Person.objects.get(id=ami_id)
                logged_user.Amis.add(ami)
            except Person.DoesNotExist:
                pass

    amis = logged_user.Amis.all()
    personnes = Person.objects.exclude(id__in=amis).exclude(id=logged_user.id)

    return render(request, 'ajout_ami.html', {
        'logged_user': logged_user,
        'amis': amis,
        'personnes': personnes,
        'statut_message': statut_message,  # Passer le statut
    })
