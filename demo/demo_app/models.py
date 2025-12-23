from django.db import models

# Create your models here.





class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)

    def dictionary(self):
        output = {self.username: {"email": self.email, "password": self.password}}
        return output


class NotesDemo(models.Model):
    """
    This is the database model for django to make the database with
    """
    label = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    content = models.CharField(max_length=150)
    date = models.DateField()
    email = models.ForeignKey(Users, on_delete=models.CASCADE)

    def relevant_info(self):
        """
        this is to get the label and the content from the note
        :return: label and content
        """
        output = f"The label is {self.label}\n"
        output += f"The content is:\n{self.content}"
        return output

    def author(self):
        """
        This is to get the author of the note
        :return: a string of the name and surname concatenated
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
