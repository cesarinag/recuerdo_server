from django.db import models
from django.contrib.auth import get_user_model

class Haiku(models.Model):
    five1 = models.CharField(max_length=15)
    seven = models.CharField(max_length=21)
    five2 = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tkes place of 'User'
    owner = models.ForeignKey(get_user_model(), related_name='haiku', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.five1}, {self.seven}, {self.five2}"


    def as_dict(self):
        return {
        'id': self.id,
        'five1': self.five1,
        'seven': self.seven,
        'five2': self.five2
        }
