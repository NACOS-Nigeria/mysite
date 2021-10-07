from django.db import models


class Onemodel(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return f"Новость : {self.title}"

    class Meta:
        verbose_name = "Новости и акции"
        verbose_name_plural = "Новости и акции"


class AddCallForm(models.Model):
    name = models.CharField("Имя", max_length=40)
    fone = models.CharField("Телефон", max_length=250)

    def __str__(self):
        return f"Заявка от клиента : {self.name}"

    class Meta:
        verbose_name = "Заявка перезвонить"
        verbose_name_plural = "Заявки перезвонить"
