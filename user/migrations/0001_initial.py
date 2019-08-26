# Generated by Django 2.1 on 2019-04-13 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='educationexperice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startime', models.DateField(blank=True, null=True, verbose_name='教育开始时间')),
                ('endtime', models.DateField(blank=True, null=True, verbose_name='教育结束时间')),
                ('school', models.CharField(blank=True, max_length=128, null=True, verbose_name='学校')),
                ('major', models.CharField(blank=True, max_length=128, null=True, verbose_name='专业')),
                ('educationbackground', models.CharField(blank=True, max_length=128, null=True, verbose_name='教育背景')),
            ],
            options={
                'verbose_name': '教育经历',
                'verbose_name_plural': '教育经历',
            },
        ),
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_friend', models.BooleanField(default=False, verbose_name='是否为好友')),
            ],
            options={
                'verbose_name': '好友列表',
                'verbose_name_plural': '好友列表',
            },
        ),
        migrations.CreateModel(
            name='imageprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgurl', models.CharField(blank=True, max_length=1000, null=True, verbose_name='头像路径')),
            ],
            options={
                'verbose_name': '头像',
                'verbose_name_plural': '头像',
            },
        ),
        migrations.CreateModel(
            name='jobexperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_place', models.CharField(blank=True, max_length=128, null=True, verbose_name='工作单位')),
                ('job', models.CharField(blank=True, max_length=128, null=True, verbose_name='职业')),
                ('job_period_start', models.DateField(blank=True, null=True, verbose_name='就职时间')),
                ('job_period_end', models.DateField(blank=True, null=True, verbose_name='离职时间')),
                ('job_city', models.CharField(blank=True, max_length=128, null=True, verbose_name='工作城市')),
                ('job_salary', models.CharField(blank=True, max_length=128, null=True, verbose_name='年薪')),
                ('job_province', models.CharField(blank=True, max_length=128, null=True, verbose_name='省份')),
            ],
            options={
                'verbose_name': '工作经历',
                'verbose_name_plural': '工作经历',
            },
        ),
        migrations.CreateModel(
            name='user_profile_company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile_company', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identity', models.CharField(choices=[('1', '毕业生'), ('2', '在校生'), ('3', '企业账号')], default='3', max_length=128, verbose_name='用户身份')),
                ('phonenumber', models.CharField(blank=True, max_length=128, null=True, verbose_name='电话号码')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='公司名')),
                ('email', models.EmailField(blank=True, max_length=128, null=True, verbose_name='邮件')),
            ],
            options={
                'verbose_name': '企业个人信息',
                'verbose_name_plural': '企业个人信息',
            },
        ),
        migrations.CreateModel(
            name='user_profile_graduate',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile_graduate', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identity', models.CharField(choices=[('1', '毕业生'), ('2', '在校生'), ('3', '企业账号')], default='1', max_length=128, verbose_name='用户身份')),
                ('phonenumber', models.CharField(blank=True, max_length=128, null=True, verbose_name='电话号码')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='姓名')),
                ('gender', models.CharField(blank=True, choices=[('M', '男'), ('F', '女')], max_length=128, null=True, verbose_name='性别')),
                ('age', models.CharField(blank=True, max_length=128, null=True, verbose_name='年龄')),
                ('major', models.CharField(blank=True, max_length=128, null=True, verbose_name='专业')),
                ('email', models.EmailField(blank=True, max_length=128, null=True, verbose_name='邮件')),
                ('birth_data', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('education_background', models.CharField(blank=True, choices=[('U', '本科生'), ('M', '硕士'), ('P', '博士')], max_length=128, null=True, verbose_name='学历')),
                ('university', models.CharField(blank=True, max_length=128, null=True, verbose_name='所在学校')),
                ('living_city', models.CharField(blank=True, max_length=128, null=True, verbose_name='居住城市')),
                ('living_province', models.DateField(blank=True, max_length=128, null=True, verbose_name='居住省份')),
                ('school_period_start', models.DateField(blank=True, null=True, verbose_name='在校时间开始')),
                ('school_period_end', models.DateField(blank=True, null=True, verbose_name='在校时间结束')),
                ('honour', models.TextField(blank=True, max_length=1000, null=True, verbose_name='荣誉')),
                ('self_judgement', models.TextField(blank=True, max_length=1000, null=True, verbose_name='自我评价')),
            ],
            options={
                'verbose_name': '毕业生个人信息',
            },
        ),
        migrations.CreateModel(
            name='user_profile_stu',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile_stu', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('education_background', models.CharField(blank=True, choices=[('U', '本科生'), ('M', '硕士'), ('P', '博士')], max_length=128, null=True, verbose_name='学历')),
                ('university', models.CharField(blank=True, max_length=128, null=True, verbose_name='所在学校')),
                ('living_province', models.CharField(blank=True, max_length=128, null=True, verbose_name='居住省份')),
                ('living_city', models.CharField(blank=True, max_length=128, null=True, verbose_name='居住城市')),
                ('identity', models.CharField(choices=[('1', '毕业生'), ('2', '在校生'), ('3', '企业账号')], default='2', max_length=128, verbose_name='用户身份')),
                ('phonenumber', models.CharField(blank=True, max_length=128, null=True, verbose_name='电话号码')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='姓名')),
                ('gender', models.CharField(blank=True, choices=[('M', '男'), ('F', '女')], max_length=128, null=True, verbose_name='性别')),
                ('age', models.CharField(blank=True, max_length=128, null=True, verbose_name='年龄')),
                ('major', models.CharField(blank=True, max_length=128, null=True, verbose_name='专业')),
                ('email', models.EmailField(blank=True, max_length=128, null=True, verbose_name='邮件')),
                ('birth_data', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('institution', models.CharField(blank=True, max_length=128, null=True, verbose_name='学院')),
                ('self_sign', models.CharField(blank=True, max_length=128, null=True, verbose_name='个性签名')),
                ('self_judgement', models.TextField(blank=True, null=True, verbose_name='自我评价')),
            ],
            options={
                'verbose_name': '在校生个人信息',
                'verbose_name_plural': '在校生个人信息',
            },
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_jobexperiment', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='imageprofile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_imageprofile', to=settings.AUTH_USER_MODEL, verbose_name='用户头像'),
        ),
        migrations.AddField(
            model_name='friends',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuser', to=settings.AUTH_USER_MODEL, verbose_name='朋友的id'),
        ),
        migrations.AddField(
            model_name='friends',
            name='whosfriend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fwhosfriend', to=settings.AUTH_USER_MODEL, verbose_name='谁的朋友'),
        ),
        migrations.AddField(
            model_name='educationexperice',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_educationexperience', to=settings.AUTH_USER_MODEL, verbose_name='用户教育经历'),
        ),
    ]