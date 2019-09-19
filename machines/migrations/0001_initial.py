# Generated by Django 2.2.3 on 2019-09-19 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop', models.CharField(choices=[('6', 'цех 6'), ('7', 'цех 7'), ('8', 'цех 8'), ('9', 'цех 9'), ('11', 'цех 11'), ('14', 'цех 14'), ('20', 'цех 20'), ('26', 'цех 26')], max_length=20, verbose_name='Цех')),
                ('code', models.CharField(max_length=10, verbose_name='Инвентарный номер')),
                ('model', models.CharField(max_length=20, verbose_name='Модель')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('timetable', models.CharField(choices=[('8/5', '8 часов с выходными'), ('12/5', '12 часов с выходными'), ('24/5', 'круглосуточно с выходными'), ('24/7', 'круглосуточно без выходных')], max_length=30, verbose_name='Расписание')),
                ('xbee_mac', models.CharField(blank=True, max_length=25, null=True, verbose_name='MAC модема')),
                ('main_channel', models.CharField(blank=True, max_length=5, null=True, verbose_name='Канал')),
                ('idle_threshold', models.IntegerField(default=100, verbose_name='Порог включения')),
                ('no_load_threshold', models.IntegerField(default=110, verbose_name='Порог холостого хода')),
                ('allowed_idle_interval', models.IntegerField(default=15, verbose_name='Допустимый простой, мин')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='machines', verbose_name='Фото оборудования')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('login', models.CharField(max_length=30, verbose_name='Логин')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
                ('role', models.CharField(choices=[('administrator', 'Администратор'), ('operator', 'Рабочий'), ('master', 'Мастер'), ('manager', 'Руководитель')], max_length=20, verbose_name='Роль')),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('mac_address', models.CharField(max_length=25)),
                ('channel', models.CharField(max_length=5, null=True)),
                ('value', models.FloatField()),
                ('ip', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Код')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('is_working', models.BooleanField(default=False, verbose_name='Работа')),
                ('is_operator', models.BooleanField(default=False, verbose_name='Указывается оператором')),
            ],
        ),
        migrations.CreateModel(
            name='Semaphore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Семафор')),
                ('is_locked', models.BooleanField(default=False, verbose_name='Заблокировано')),
                ('locked_when', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Когда заблокировано')),
                ('alert_interval', models.IntegerField(default=15, verbose_name='Количество минут до предупреждения')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_holiday_short', models.BooleanField(auto_created=True, verbose_name='В предпразничные дни на смены час короче')),
                ('name', models.CharField(max_length=255, verbose_name='Название расписания:')),
            ],
        ),
        migrations.CreateModel(
            name='TimetableDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week_start', models.CharField(choices=[('Пн', 'Понедельник'), ('Вт', 'Вторник'), ('Ср', 'Среда'), ('Чт', 'Четверг'), ('Пт', 'Пятница'), ('Сб', 'Суббота'), ('Вс', 'Воскресенье')], max_length=14, verbose_name='С дня недели')),
                ('day_of_week_end', models.CharField(choices=[('Пн', 'Понедельник'), ('Вт', 'Вторник'), ('Ср', 'Среда'), ('Чт', 'Четверг'), ('Пт', 'Пятница'), ('Сб', 'Суббота'), ('Вс', 'Воскресенье')], max_length=14, verbose_name='По день недели')),
                ('start_time1', models.TimeField(verbose_name='Начало 1 смены')),
                ('end_time1', models.TimeField(verbose_name='Окончание 1 смены')),
                ('lunch_start1', models.TimeField(blank=True, null=True, verbose_name='Начало обеда 1 смены')),
                ('lunch_end1', models.TimeField(blank=True, null=True, verbose_name='Окончание обеда 1 смены')),
                ('start_time2', models.TimeField(blank=True, null=True, verbose_name='Начало 2 смены')),
                ('end_time2', models.TimeField(blank=True, null=True, verbose_name='Окончание 2 смены')),
                ('lunch_start2', models.TimeField(blank=True, null=True, verbose_name='Начало обеда 2 смены')),
                ('lunch_end2', models.TimeField(blank=True, null=True, verbose_name='Окончание обеда 2 смены')),
                ('start_time3', models.TimeField(blank=True, null=True, verbose_name='Начало 3 смены')),
                ('end_time3', models.TimeField(blank=True, null=True, verbose_name='Окончание 3 смены')),
                ('lunch_start3', models.TimeField(blank=True, null=True, verbose_name='Начало обеда 3 смены')),
                ('lunch_end3', models.TimeField(blank=True, null=True, verbose_name='Окончание обеда 3 смены')),
            ],
        ),
        migrations.CreateModel(
            name='TimetableContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.TimetableDetail', verbose_name='Детали')),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.Timetable', verbose_name='Расписание')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GraphicsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('value', models.FloatField(verbose_name='Значение')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machines.Equipment', verbose_name='Оборудование')),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machines.Participant'),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassifiedInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Начало периода')),
                ('end', models.DateTimeField(verbose_name='Конец периода')),
                ('is_zero', models.BooleanField(blank=True, default=False, verbose_name='Нет данных')),
                ('automated_classification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='auto_reason', to='machines.Reason', verbose_name='Вычисленная причина')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.Equipment', verbose_name='Оборудование')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Указал причину')),
                ('user_classification', models.ForeignKey(blank=True, limit_choices_to={'is_operator': True}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_reason', to='machines.Reason', verbose_name='Причина оператора')),
            ],
        ),
    ]
