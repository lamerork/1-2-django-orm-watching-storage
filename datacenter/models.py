from django.db import models
import django


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
    
    def get_duration(self):

        if self.leaved_at == None:
            interval = django.utils.timezone.now() - self.entered_at
        else:
            interval = self.leaved_at - self.entered_at
        return int(interval.total_seconds())
    
    def format_duration(self):
     
        seconds = self.get_duration()

        return f'{seconds// 3600}:{(seconds % 3600) // 60}'
    
    def is_long(self, minutes=60):

        seconds = self.get_duration()

        if seconds >= minutes * 60:
            return True
        return False