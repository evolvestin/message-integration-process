from django.db import models


class Mail(models.Model):
    mail = models.CharField(max_length=255,  blank=False,  help_text='Адрес электронной почты для почтового аккаунта')
    password = models.CharField(max_length=255, blank=False, help_text='Пароль для почтового аккаунта')
    type = models.CharField(max_length=255, blank=False, help_text='Тип почтового сервиса IMAP (mail.ru, ya.ru)')
    last_message_id = models.CharField(max_length=255, blank=False, help_text='ID последнего обработанного сообщения')

    def __str__(self):
        return self.mail


class Message(models.Model):
    id = models.AutoField(primary_key=True, help_text='Уникальный автоинкрементный идентификатор сообщения')
    uid = models.IntegerField(unique=True, help_text='Уникальный идентификатор сообщения')
    subject = models.CharField(max_length=255, blank=False, help_text='Тема сообщения')
    content = models.TextField(blank=False, help_text='Содержимое сообщения')
    sent_date = models.DateTimeField(blank=False, help_text='Дата и время отправки сообщения')
    receiving_date = models.DateTimeField(null=True, blank=True, help_text='Дата и время получения сообщения')
    attached_file_link_list = models.JSONField(default=list, help_text='Список прикрепленных файлов в формате JSON')
    mail = models.ForeignKey(
        Mail,
        related_name='messages',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Связь с почтовым аккаунтом, которому принадлежит это сообщение'
    )

    def __str__(self):
        return self.subject


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/', help_text='Файл, прикрепленный к сообщению')
    message = models.ForeignKey(
        Message,
        related_name='attachments',
        on_delete=models.CASCADE,
        help_text='Связь с сообщением, к которому прикреплен файл'
    )

    def __str__(self):
        return self.message
