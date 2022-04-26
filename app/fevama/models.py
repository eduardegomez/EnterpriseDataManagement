from django.db import models

# Create your models here.

# DeleteDevices Manager
class ContactManager(models.Manager):
    def create_contact(self, nombre, email):
        contact = self.create(nombre=nombre, email=email)
        return contact

# Contacto Model
class Contact(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    objects = ContactManager()