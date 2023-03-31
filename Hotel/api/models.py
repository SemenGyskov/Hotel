from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование страны')


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование сервиса')
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Cервисы'


class Excursions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование экскурсии')
    place = models.CharField(max_length=100, verbose_name='Место экскурсии')
    time = models.CharField(max_length=100, verbose_name='Время экскурсии', choices=(('1','1 час'),('2','2 часа'),('3','3 часа'),))
    cost = models.IntegerField(verbose_name='Стоимость экскурcии')
    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'


class Tour(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование тура')
    country = models.CharField(max_length=100, verbose_name='Страна')
    time_live = models.CharField(max_length=100, verbose_name='Время проживания', choices=(('1','1 Неделя'), ('2','2 Недели'), ('3','3 Недели')))
    services = models.ManyToManyField(Service, verbose_name='Cервис')
    people = models.IntegerField(choices=(('1', '1 человек'), ('2', '2 человек'), ('3', '3 человек'), ('4', '4 человек'),), verbose_name='Количество человек')
    hotel = models.CharField(max_length=100,verbose_name='Звёзд у отеля', choices=(('3', '★★★'),('4', '★★★★'),('5', '★★★★★'),))
    excursions = models.ManyToManyField(Excursions,verbose_name='Экскурсии')
    cost = models.IntegerField(default=0, verbose_name='Стоимость тура')
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class MyOffice(models.Model):
    tours = models.ManyToManyField(Tour, verbose_name='Тур')
    cost = models.IntegerField(default=0, verbose_name='Стоимость')
    time = models.IntegerField(verbose_name='Время поездки', choices=(('1','6 часов'),('2','12 часов'),('3','18 часов')))
    class Meta:
        verbose_name = 'Личный кабинет'
        verbose_name_plural = 'Личные кабинеты'