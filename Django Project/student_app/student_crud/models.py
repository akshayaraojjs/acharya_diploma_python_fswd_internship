from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ]
    
    BRANCH_CHOICES = [
        ('CS', 'Computer Science'),
        ('IS', 'Information Science'),
        ('EC', 'Electronics & Communication'),
        ('EE', 'Electrical & Electronics'),
        ('ME', 'Mechanical'),
        ('CV', 'Civil'),
    ]

    COURSE_CHOICES = [
        ('JFSWD', 'Java Full Stack Web Development'),
        ('PFSWD', 'Python Full Stack Web Development'),
        ('MERN', 'MERN Stack Web Development'),
        ('MEAN', 'MEAN Stack Web Development'),
    ]

    # CharField => varchar(50) 
    name = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=20, unique=True)
    # IntegerField => int
    age = models.IntegerField()
    phone = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    sem = models.IntegerField()
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    def __str__(self):
        return self.name