from datetime import date
from django.db import models

# Create your models here.

# ---------- START EMPRESA ----------------- # 
# Empresa Manager
class EmpresaManager(models.Manager):
    def create_empresa(self, name, cif, cnae, phone, aux):
        empresa = self.create(name=name, cif=cif, cnae=cnae, phone=phone, aux=aux)
        return empresa

# Empresa Model
class Empresa(models.Model):
    name = models.CharField(max_length=200)
    cif = models.CharField(max_length=200)
    cnae = models.CharField(max_length=200, default="-")
    phone = models.IntegerField(default=0)
    aux = models.CharField(max_length=2000, default="-")

    objects = EmpresaManager()
# ---------- END EMPRESA ----------------- # 

# ---------- START CONTACTS ----------------- # 

# TypeOfContact Manager
class TypeOfContactManager(models.Manager):
    def create_typeofcontact(self, name):
        typeofcontact = self.create(name=name)
        return typeofcontact

# TypeOfContact Model
class TypeOfContact(models.Model):
    name = models.CharField(max_length=200)

    objects = TypeOfContactManager()

# Contact Manager
class ContactManager(models.Manager):
    def create_contact(self, name, email, type, empresa):
        contact = self.create(name=name, email=email, type=type, empresa=empresa)
        return contact

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    type = models.ForeignKey(TypeOfContact, on_delete=models.CASCADE, default=0)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)

    objects = ContactManager()

# ---------- END CONTACTS ----------------- # 

# ---------- START ECONOMIC DATA ----------------- # 
# EconomicData Manager
class EconomicDataManager(models.Manager):
    def create_economicdata(self, empresa, year, workers, data):
        economicData = self.create(empresa=empresa, year=year, workers=workers, data=data)
        return economicData

# EconomicData Model
class EconomicData(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    year = models.IntegerField(default=0)
    workers = models.IntegerField(default=0)
    data = models.IntegerField(default=0)

    objects = EconomicDataManager()
# ---------- END ECONOMIC DATA ----------------- # 

# ---------- START LINE ----------------- #
# Line Manager
class LineManager(models.Manager):
    def create_line(self, line):
        line = self.create(line=line)
        return line

# Line Model
class Line(models.Model):
    line = models.CharField(max_length=200)

    objects = LineManager()
# ---------- END LINE ----------------- #

# ---------- START ACT ----------------- #
# Act Manager
class ActManager(models.Manager):
    def create_act(self, name):
        act = self.create(name=name)
        return act

# Act Model
class Act(models.Model):
    name = models.CharField(max_length=200)

    objects = ActManager()
# ---------- END ACT ----------------- #

# ---------- START ORGANISM ----------------- #
# Organism Manager
class OrganismManager(models.Manager):
    def create_organism(self, name):
        organism = self.create(name=name)
        return organism

# Organism Model
class Organism(models.Model):
    name = models.CharField(max_length=200)

    objects = OrganismManager()
# ---------- END ORGANISM ----------------- #

# ---------- START ANNOUNCEMENT ----------------- #
# Announcement Manager
class AnnouncementManager(models.Manager):
    def create_announcement(self, year):
        announcement = self.create(year=year)
        return announcement

# Announcement Model
class Announcement(models.Model):
    year = models.CharField(max_length=200)

    objects = AnnouncementManager()
# ---------- END ANNOUNCEMENT ----------------- #

# ---------- START SITUATION ----------------- #
# Situation Manager
class SituationManager(models.Manager):
    def create_situation(self, situation):
        situation_obj = self.create(situation=situation)
        return situation_obj

# Situation Model
class Situation(models.Model):
    situation = models.CharField(max_length=200)

    objects = SituationManager()
# ---------- END SITUATION ----------------- #

# ---------- START APPLICANT ----------------- #
# Applicant Manager
class ApplicantManager(models.Manager):
    def create_applicant(self, name):
        applicant = self.create(name=name)
        return applicant

# Applicant Model
class Applicant(models.Model):
    name = models.CharField(max_length=200)

    objects = ApplicantManager()
# ---------- END APPLICANT----------------- #

# ---------- START ASSISTANCE ----------------- # 
# Assistance Manager
class AssistanceManager(models.Manager):
    def create_assistance(self, line, act, organism, announcement, situation, applicant, management, requested, applied, date, payment):
        assistance = self.create(line=line, act=act, organism=organism, announcement=announcement, situation=situation, applicant=applicant, management=management, requested=requested, applied=applied, date=date, payment=payment)
        return assistance

# Assistance Model
class Assistance(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE, default=0)
    act = models.ForeignKey(Act, on_delete=models.CASCADE, default=0)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE, default=0)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, default=0)
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE, default=0)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, default=0)
    
    management = models.CharField(max_length=200)
    requested = models.IntegerField(default=0)
    applied = models.IntegerField(default=0)
    date = models.CharField(max_length=200)
    project_check = models.IntegerField(default=0)
    payment = models.CharField(max_length=200)
    
    objects = AssistanceManager()
# ---------- END ASSISTANCE ----------------- #

# ---------- START PROJECT ----------------- # 
# Porject Manager
class ProjectManager(models.Manager):
    def create_project(self, empresa, project_name):
        project = self.create(empresa=empresa, project_name=project_name)
        return project

# Project Model
class Project(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    project_name = models.CharField(max_length=200, default="None")
    invoice_check = models.CharField(max_length=200, default=0)

    objects = ProjectManager()
# ---------- END PROJECT ----------------- # 

# ---------- START INVOICE ----------------- # 
# Invoice Manager
class InvoiceManager(models.Manager):
    def create_invoice(self, number, invoice, year, amount, date, project):
        invoice = self.create(number=number, invoice=invoice, year=year, amount=amount, date=date, project=project)
        return invoice

# Invoice Model
class Invoice(models.Model):
    number = models.IntegerField(default=0)
    invoice = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    date = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)

    objects = InvoiceManager()
# ---------- END INVOICE ----------------- # 

# --- START CONFIGURATION PARAMETERS ----- # 
# ConfigParameters Manager
class ConfigParametersManager(models.Manager):
    def create_configParameter(self, address, value):
        parameter = self.create(address=address, value=value)
        return parameter

    @staticmethod
    def update_config_parameter(pAddress,pValue):
        configParameter = ConfigParameters.objects.filter(address=pAddress).first()
        if configParameter:
            configParameter.value = pValue
            configParameter.save(update_fields=["value"])
        return configParameter

# ConfigParameters Model
class ConfigParameters(models.Model):
    address = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    objects = ConfigParametersManager()
# --- END CONFIGURATION PARAMETERS ----- # 