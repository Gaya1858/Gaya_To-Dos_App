
""" django models will help build database models which model the characteristics of the data in
the database. We use the django's built-in User model as the creator of the todos. """
from django.db import models
from django.contrib.auth.models import User


"""
    class Tdo inherits from the Model class. The Model class allows us to interact witht the datebase,
    create a tabel, retrieve and make chnages to datat in the databse.
"""
class Todo(models.Model):
    """
        :param: TYPE_CHOICES and type- whether the todos list is for personal, public or official
        :param: RATE_CHOICES and rate- important or not
        :param: title - name of the person
        :param: memo
    """

    TYPE_CHOICES =(
        ("PERSONAL", "Personal"),
        ("PUBLIC", "Public"),
        ("OFFICIAL","Official"),
    )
    RATE_CHOICE =(("IMPORTANT","Important"),("HAVE_TIME","HaveTime"), )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="PERSONAL")
    rate = models.CharField(max_length=12, choices=RATE_CHOICE, default="HAVE_TIME")
    memo = models.TextField(blank=True)

    #set current time
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    #user who posted this
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    """
        this dunder str method returns title
    """
    def __str__(self):
        return self.title

