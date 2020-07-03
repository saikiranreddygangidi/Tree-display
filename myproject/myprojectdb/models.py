from django.db import models
class Program(models.Model):

    program = models.CharField(max_length=300)
    def __str__(self):
	    return self.program
class Subprogram(models.Model):
    subprogram = models.CharField(max_length=300)
    program = models.ForeignKey(Program, default="software", on_delete=models.SET_DEFAULT)
    def __str__(self):
	    return self.subprogram

class Course(models.Model):
    course = models.CharField(max_length=300)
    img = models.ImageField(upload_to="pics")
    subprogram = models.ForeignKey(Subprogram, default="front-end", on_delete=models.SET_DEFAULT)
    def __str__(self):
	    return self.course