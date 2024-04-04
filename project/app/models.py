from django.db import models

# Create your models here.
class DeparmentModel(models.Model):
    Dep_name=models.CharField(max_length=500, verbose_name='Name')
    Description=models.TextField(max_length=500, verbose_name='Desc')
    def __str__(self):                     #in-build magic method for overloading
        return (self.Dep_name)
    

class StudentModel(models.Model):
    stu_name=models.CharField(max_length=500)
    stu_class=models.CharField(max_length=500)
    stu_email=models.EmailField()
    stu_mobile=models.IntegerField()
    # stu_deparment=models.ForeignKey(DeparmentModel, on_delete=models.CASCADE,null=True)
    stu_deparment=models.ForeignKey(DeparmentModel, on_delete=models.PROTECT,null=True)

    # class Meta:

    def __str__(self):                     #in-build magic method for overloading
        return (self.stu_name)