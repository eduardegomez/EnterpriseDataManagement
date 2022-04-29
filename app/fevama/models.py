from django.db import models

# Create your models here.

# ---------- START EMPRESA ----------------- # 
# Empresa Manager
class EmpresaManager(models.Manager):
    def create_empresa(self, name, CIF):
        empresa = self.create(name=name, CIF=CIF)
        return empresa

# Empresa Model
class Empresa(models.Model):
    name = models.CharField(max_length=200)
    cif = models.CharField(max_length=200)

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
    def create_contact(self, name, email):
        contact = self.create(name=name, email=email)
        return contact

# Contacto Model
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
    data = models.FloatField(default=0.0, blank=True, null=True)

    objects = EconomicDataManager()
# ---------- END ECONOMIC DATA ----------------- # 

