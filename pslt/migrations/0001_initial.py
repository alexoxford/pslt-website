# Generated by Django 2.0.6 on 2018-06-03 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.URLField()),
                ('year', models.IntegerField()),
                ('type', models.CharField(choices=[('Proposal', 'Proposal'), ('PDR', 'PDR'), ('CDR', 'CDR'), ('FRR', 'FRR'), ('PLAR', 'PLAR'), ('Other', 'Other')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.URLField()),
                ('text', models.CharField(max_length=100)),
                ('alt_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.URLField()),
                ('alt_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateTimeField()),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pslt.Media')),
            ],
            bases=('pslt.media',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pslt.Media')),
            ],
            bases=('pslt.media',),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='pslt.Tag'),
        ),
    ]
