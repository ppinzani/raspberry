from django.db import models


# Create your models here.
class LogMessage(models.Model):

    fecha = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=False)

    class Meta:
        verbose_name = "Log Message"
        verbose_name_plural = "Log Messages"

    def __str__(self):
        return "Log Message %s" % self.id
