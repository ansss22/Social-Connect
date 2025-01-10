from django.db import models

class Faculty(models.Model) :
    nom=models.CharField(max_length=42)
    def __str__(self):
        return self.nom

class Person(models.Model):
    name = models.CharField(max_length=30)
    prenom = models.CharField(max_length=32)
    date_naissance = models.DateField()
    email = models.EmailField(unique=True)
    tlf = models.CharField(max_length=20)
    password = models.CharField(max_length=302)
    Amis = models.ManyToManyField('self', symmetrical=True, blank=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Message(models.Model):
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")
    auteur = models.ForeignKey('Person', on_delete=models.CASCADE)  
    def __str__(self):
        return self.contenu
class Campus(models.Model) :
    nom=models.CharField(max_length=42)
    adresse=models.CharField(max_length=60)
    def __str__(self):
        return self.nom
class Job(models.Model) :
    titre=models.CharField(max_length=42)
    def __str__(self):
        return self.titre
class Cursus(models.Model) :
    titre=models.CharField(max_length=42)
    def __str__(self):
        return self.titre
class Student(Person):
    annee=models.IntegerField()
    cursus=models.ForeignKey('Cursus',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Employee(Person):
    office=models.CharField(max_length=42)
    campus=models.ForeignKey('Campus',on_delete=models.CASCADE)
    job=models.ForeignKey('Job',on_delete=models.CASCADE)
    def __str__(self):
        return self.name