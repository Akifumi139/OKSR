from django.db import models


class Message(models.Model):
    purchase_date = models.CharField(max_length=255)
    medicine_name = models.CharField(max_length=510)
    pharmacy_name = models.CharField(max_length=255)

    def __str__(self):
        return u"{0},{1},{2} ".format(self.purchase_date[:],self.medicine_name[:],self.pharmacy_name[:])
