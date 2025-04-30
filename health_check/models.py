from django.db import models
from django.contrib.auth.models import User

class DeliveringValue(models.Model):
    
    COLOR_CHOICES = [
        ('red-stable', 'Red - Stable'),
        ('red-improving', 'Red - Improving'),
        ('red-worse', 'Red - Getting Worse'),
        ('yellow-stable', 'Yellow - Stable'),
        ('yellow-improving', 'Yellow - Improving'),
        ('yellow-worse', 'Yellow - Getting Worse'),
        ('green-stable', 'Green - Stable'),
        ('green-improving', 'Green - Improving'),
        ('green-worse', 'Green - Getting Worse'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    color_status = models.CharField(max_length=20, choices=COLOR_CHOICES)
    reason = models.TextField()
    improvement = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

