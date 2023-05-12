"""
Definition of models.
"""

from unittest.util import _MAX_LENGTH
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length = 20)
    reg_no = models.PositiveIntegerField(primary_key=True)
    password = models.CharField(max_length = 20)
   
    father_name = models.CharField(max_length = 20)
    mother_name = models.CharField(max_length = 20)
    contact = models.PositiveIntegerField()
    city = models.CharField(max_length = 50)
    
    def __str__(self):
        return str(self.reg_no)

class Subject(models.Model):  
    reg_no = models.ForeignKey(Registration, on_delete=models.CASCADE)
    MAX_CHOICES = 5

    # Define your choice options as a tuple of tuples
    CHOICES = (
        ('Data Structures', 'Data Structures'), ('Object Oriented Programming', 'Object Oriented Programming'), 
        ('Digital Systems Design','Digital Systems Design'), ('Computer Organization and Architechture','Computer Organization and Architechture'), ('Design and Analysis of Algorithms','Design and Analysis of Algorithms'), 
        ('Formal Languages and Automata Theory','Formal Languages and Automata Theory'), ('Embedded Systems','Embedded Systems'), ('Operating Systems', 'Operating Systems'), 
        ('Computer Networks','Computer Networks'), ('Software Engineering', 'Software Engineering'), ('Compiler Design','Compiler Design'),
        ('Parallel Computing Architecture and Programming','Parallel Computing Architecture and Programming'), ('Distributed Systems','Distributed Systems')
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

    def __str__(self):
        return str(self.selected_choices)

class GradeAttendance(models.Model):
    reg_no = models.ForeignKey(Registration, on_delete = models.CASCADE)
    CHOICES = (
        ('Data Structures', 'Data Structures'), ('Object Oriented Programming', 'Object Oriented Programming'), 
        ('Digital Systems Design','Digital Systems Design'), ('Computer Organization and Architechture','Computer Organization and Architechture'), ('Design and Analysis of Algorithms','Design and Analysis of Algorithms'), 
        ('Formal Languages and Automata Theory','Formal Languages and Automata Theory'), ('Embedded Systems','Embedded Systems'), ('Operating Systems', 'Operating Systems'), 
        ('Computer Networks','Computer Networks'), ('Software Engineering', 'Software Engineering'), ('Compiler Design','Compiler Design'),
        ('Parallel Computing Architecture and Programming','Parallel Computing Architecture and Programming'), ('Distributed Systems','Distributed Systems')
    )

    
    select_subject = models.CharField(choices=CHOICES, max_length=200)
    grade = models.CharField(max_length = 1)
    attendance = models.PositiveIntegerField()

    def __str__(self):
        return self.select_subject + '_' + str(self.reg_no)