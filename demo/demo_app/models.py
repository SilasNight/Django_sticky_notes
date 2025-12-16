from django.db import models

# Create your models here.


class NotesDemo(models.Model):
    label = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    content = models.CharField(max_length=150)
    date = models.DateField()

    def relevant_info(self):
        output = f"The label is {self.label}\n"
        output += f"The content is:\n{self.content}"
        return output

    def author(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
