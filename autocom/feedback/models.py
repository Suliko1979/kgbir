from django.db import models

class FeedBack(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=18)
    description = models.CharField(max_length=255, blank=True, null=True)
    call_time = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Данные клиента'
