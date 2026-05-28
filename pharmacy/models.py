from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)   # 👈 ADD THIS

    def __str__(self):
        return f"{self.name} ({self.location})"


# Pharmacy Table
class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Medicine Table
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Stock Table
class Stock(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.medicine.name} at {self.pharmacy.name}"

