from django.db import models

# Create your models here.
class Teachers(models.Model):
    tittle=models.CharField(verbose_name="Имя учителя",max_length=3)
    subject=models.CharField(max_length=30,verbose_name="Предмет")
    image=models.ImageField(upload_to='media/photo/teachers/%d')
    description=models.CharField(verbose_name="Краткое описание о учителя",max_length=30)
    def __str__(self) -> str:
        return self.tittle
class Cours(models.Model):
    name=models.CharField(verbose_name="Название курса ",max_length=30)
    image=models.ImageField(verbose_name="Загрузите фото предмета",upload_to='media/photo/cours/%d')
    on_time=models.CharField(verbose_name="Время курса ",max_length=30)
    price=models.CharField(verbose_name="Курс стоить",max_length=30)
    def __str__(self) -> str:
        return self.name
    