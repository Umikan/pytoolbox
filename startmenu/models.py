from django.db import models


class AppInfo(models.Model):
    name = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "AppInfo"
