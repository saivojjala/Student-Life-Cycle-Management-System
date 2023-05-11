"""
Definition of models.
"""

from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length = 20)
    reg_no = models.PositiveIntegerField(primary_key=True)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.reg_no)

class Subject(models.Model):  
    reg_no = models.ForeignKey(Registration, on_delete=models.CASCADE)
    MAX_CHOICES = 5

    # Define your choice options as a tuple of tuples
    CHOICES = (
        ('option1', 'Data Structures'), ('option2', 'Object Oriented Programming'), 
        ('option3','Digital Systems Design'), ('option4','Design and Analysis of Algorithms'), 
        ('option5','Formal Languages and Automata Theory'), ('option6', 'Operating Systems'), 
        ('option7','Computer Networks'), ('option8', 'Software Engineering'), ('option9','Compiler Design')
    )

    choices = models.CharField(max_length=255)

    def get_choices(self):
        # parse the choices string and return a list of selected choices
        return self.choices.split(',')

    def set_choices(self, choices):
        # set the choices string by joining the selected choices with commas
        self.choices = ','.join(choices)

    # define a property for the selected choices
    selected_choices = property(get_choices, set_choices)
