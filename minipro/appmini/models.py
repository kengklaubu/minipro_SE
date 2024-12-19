from django.db import models

class Bike(models.Model):
    model_name = models.CharField(max_length=100)  # ชื่อรุ่นจักรยาน
    quantity = models.PositiveIntegerField()  # จำนวนจักรยาน
    available = models.BooleanField(default=True)  # สถานะการจอง

    def __str__(self):
        return f"{self.model_name} - {'Available' if self.available else 'Unavailable'}"
