from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Created at",
                                      db_comment="Дата и время создания.")


class Category(models.Model):
    """ Категория выполнения """
    title = models.CharField(max_length=100, unique=True, verbose_name='Category', db_comment='Название категории.')

    def __str__(self):
        return self.title


class Task(TimeStamp):
    """ Задача для выполнения """
    title = models.CharField(max_length=255, unique_for_date='created_at',
                             db_comment='Название задачи.Уникально для даты.')
    description = models.TextField(verbose_name='Description', db_comment='Описание задачи.')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='Categories')
    status = models.CharField(max_length=15, choices=[('new', 'New'),
                                                      ('in progress', 'In progress'),
                                                      ('pending', 'Pending'),
                                                      ('blocked', 'Blocked'),
                                                      ('done', 'Done')],
                              verbose_name='Status',
                              db_comment='Статус задачи.Выбор из: New, In progress, Pending, Blocked, Done')
    deadline = models.DateTimeField(verbose_name='Deadline', db_comment='Дата и время дедлайн.')

    def __str__(self):
        return self.title


class SubTask(TimeStamp):
    """ Отдельная часть основной задачи (Task) """
    title = models.CharField(max_length=255, verbose_name='Title', db_comment='Название подзадачи.')
    description = models.TextField(verbose_name='Description', db_comment='Описание подзадачи.')
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Task', db_comment='Основная задача. Один ко многим.')
    status = models.CharField(max_length=15, choices=[('new', 'New'),
                                                      ('in progress', 'In progress'),
                                                      ('pending', 'Pending'),
                                                      ('blocked', 'Blocked'),
                                                      ('done', 'Done')],
                              verbose_name='Status',
                              db_comment='Статус подзадачи. Выбор из: New, In progress, Pending, Blocked, Done')
    deadline = models.DateTimeField(auto_now=False, verbose_name='Deadline', db_comment='Дата и время дедлайн.')

    def __str__(self):
        return self.title

