from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Location(models.Model):
    local = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return f"Location : {self.local}"

    class Meta:
        verbose_name_plural = "Location"


class Data(models.Model):
    name = models.CharField(max_length=64)
    area = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    capacity = models.IntegerField()
    occupied = models.IntegerField(null=True)

    def __str__(self):
        return f"Name : {self.name}| {self.area} | Status : {self.occupied}/{self.capacity}"

    class Meta:
        verbose_name_plural = "Data"

class Hospital(models.Model):
    hID = models.CharField(max_length=6, null=True)
    name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=120, null=False)
    contact = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f"Name: {self.name} | Address: {self.address}"
    
    class Meta:
        verbose_name_plural = "Hospital"

class Slot(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=False)
    timing1 = models.CharField(max_length=15, null=False)
    max_appointments1 = models.IntegerField(null=False)
    book1 = models.IntegerField(null=False, default=0)
    timing2 = models.CharField(max_length=15, null=True)
    max_appointments2 = models.IntegerField(null=True)
    book2 = models.IntegerField(null=False, default=0)
    timing3 = models.CharField(max_length=15, null=True)
    max_appointments3 = models.IntegerField(null=True)  
    book3 = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f"Hospital {self.hospital} | Timings : {self.timing1} | {self.timing2} | {self.timing3}"

class Doctor(models.Model):
    doctor = models.CharField(max_length=64, null=False)
    spec = models.CharField(max_length=64, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=False)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=False)
    fees = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    def __str__(self):
        return f"Name: {self.doctor} | Type: {self.spec} | {self.slot} | Fees: {self.fees}"

class Volunteer(models.Model):
    first = models.CharField(max_length=32, null=False)
    last = models.CharField(max_length=32, null=False)
    organization = models.CharField(max_length=64, null=False)
    contact = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=20, null=True)
    def __str__(self):
        return f"Name: {self.first} {self.last} | Contact: {self.contact}"

    class Meta:
        verbose_name_plural = "Volunteer"

class Appointment(models.Model):
      patient = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
      doc = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
      slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=False)
      hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=False)
      CONF = [
          ("Yes", "Yes"),
          ("No", "No")
      ]
      confirmation = models.CharField(max_length=3, choices=CONF, null=False, default="No")
      timings = models.CharField(max_length=15, null=False, default="-")  
      complete = models.BooleanField(null=False, default=False)
      def __str__(self):
          return f"Name: {self.patient} | Timing: {self.timings} | Confirmation: {self.confirmation}"

class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    phone = models.CharField(max_length=10, null=False)

    def __str__(self):
        return f"User: {self.user} | Phone: {self.phone}"