from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class UserLogin (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

# Um die Vorlage-Datei für die Tabelle zu erstellen wird unter hostart\migrations
# eine Vorlage-Datei mit den Feldern die hier geschrieben sind erstellt
# der Befehl dazu ist "python manage.py makemigrations" aber Du must vorher
# nach "WPage01\mywebsites" sein!

# Wenn danach der Befehl "python manage.py migrate" geschrieben wird
# geht jetzt django hin und erstellt aus der Votlagendatei "0001_initial.py"
# die Tabelle "UserLogin" mit den Feldern
