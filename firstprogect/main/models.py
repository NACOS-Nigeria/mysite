from django.db import models


class Client(models.Model):
    Person = models.CharField("Имя", max_length=45)
    Number = models.IntegerField()
    text = models.TextField("Отзыв")

    def __str__(self):
        return f"Отзыв клиента!: {self.Person}"

    class Meta:
        verbose_name = "Отызыв клиента "
        verbose_name_plural = "Отзывы клиентов"


class Client_road(models.Model):
    date = models.CharField("Дата:", max_length=45)
    point_A = models.CharField("Откуда:", max_length=45)
    point_B = models.CharField("Куда:", max_length=45)
    thing = models.CharField("Что перевозим:", max_length=45)
    telephone = models.CharField("Номер", max_length=45)
    name = models.CharField("Имя", max_length=45)
    time_to_call = models.CharField("Перезвонить:", max_length=45)


    def __str__(self):
        return f"Новая заявка на moving! : {self.name}"

    class Meta:
        verbose_name = "Заявка с описанием "
        verbose_name_plural = "Заявки с описанием"


class Client_contact(models.Model):
    name = models.CharField("Имя:", max_length=45)
    email = models.CharField("E-mail:", max_length=45)
    text = models.TextField("Текст сообщения:")

    def __str__(self):
        return f"Новое E-mail сообщение! : {self.name}"

    class Meta:
        verbose_name = "Письма-Email "
        verbose_name_plural = "Письма-Email"