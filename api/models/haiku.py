from django.db import models
from django.contrib.auth import get_user_model

class Haiku(models.Model):
    fiveone = models.CharField(max_length=18)
    seven = models.CharField(max_length=24)
    fivetwo = models.CharField(max_length=18)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tkes place of 'User'
    owner = models.ForeignKey(get_user_model(), related_name='haikus', on_delete=models.CASCADE)
    # objects = models.Manager()

    def __str__(self):
        return f"{self.fiveone}, {self.seven}, {self.fivetwo}"


    def as_dict(self):
        return {
        'id': self.id,
        'fiveone': self.fiveone,
        'seven': self.seven,
        'fivetwo': self.fivetwo
        }
