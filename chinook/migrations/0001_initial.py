# Generated by Django 4.0.3 on 2022-03-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('albumid', models.AutoField(db_column='AlbumId', primary_key=True, serialize=False)),
                ('title', models.TextField(db_column='Title')),
                ('artistid', models.IntegerField(db_column='ArtistId')),
            ],
            options={
                'db_table': 'albums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('artistid', models.AutoField(db_column='ArtistId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerid', models.AutoField(db_column='CustomerId', primary_key=True, serialize=False)),
                ('firstname', models.TextField(db_column='FirstName')),
                ('lastname', models.TextField(db_column='LastName')),
                ('company', models.TextField(blank=True, db_column='Company', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('city', models.TextField(blank=True, db_column='City', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('country', models.TextField(blank=True, db_column='Country', null=True)),
                ('postalcode', models.TextField(blank=True, db_column='PostalCode', null=True)),
                ('phone', models.TextField(blank=True, db_column='Phone', null=True)),
                ('fax', models.TextField(blank=True, db_column='Fax', null=True)),
                ('email', models.TextField(db_column='Email')),
                ('supportrepid', models.IntegerField(blank=True, db_column='SupportRepId', null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeid', models.AutoField(db_column='EmployeeId', primary_key=True, serialize=False)),
                ('lastname', models.TextField(db_column='LastName')),
                ('firstname', models.TextField(db_column='FirstName')),
                ('title', models.TextField(blank=True, db_column='Title', null=True)),
                ('reportsto', models.IntegerField(blank=True, db_column='ReportsTo', null=True)),
                ('birthdate', models.DateTimeField(blank=True, db_column='BirthDate', null=True)),
                ('hiredate', models.DateTimeField(blank=True, db_column='HireDate', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('city', models.TextField(blank=True, db_column='City', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('country', models.TextField(blank=True, db_column='Country', null=True)),
                ('postalcode', models.TextField(blank=True, db_column='PostalCode', null=True)),
                ('phone', models.TextField(blank=True, db_column='Phone', null=True)),
                ('fax', models.TextField(blank=True, db_column='Fax', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genreid', models.AutoField(db_column='GenreId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceItems',
            fields=[
                ('invoicelineid', models.AutoField(db_column='InvoiceLineId', primary_key=True, serialize=False)),
                ('invoiceid', models.IntegerField(db_column='InvoiceId')),
                ('trackid', models.IntegerField(db_column='TrackId')),
                ('unitprice', models.TextField(db_column='UnitPrice')),
                ('quantity', models.IntegerField(db_column='Quantity')),
            ],
            options={
                'db_table': 'invoice_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoiceid', models.AutoField(db_column='InvoiceId', primary_key=True, serialize=False)),
                ('customerid', models.IntegerField(db_column='CustomerId')),
                ('invoicedate', models.DateTimeField(db_column='InvoiceDate')),
                ('billingaddress', models.TextField(blank=True, db_column='BillingAddress', null=True)),
                ('billingcity', models.TextField(blank=True, db_column='BillingCity', null=True)),
                ('billingstate', models.TextField(blank=True, db_column='BillingState', null=True)),
                ('billingcountry', models.TextField(blank=True, db_column='BillingCountry', null=True)),
                ('billingpostalcode', models.TextField(blank=True, db_column='BillingPostalCode', null=True)),
                ('total', models.TextField(db_column='Total')),
            ],
            options={
                'db_table': 'invoices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MediaTypes',
            fields=[
                ('mediatypeid', models.AutoField(db_column='MediaTypeId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'media_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('playlistid', models.AutoField(db_column='PlaylistId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'playlists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SqliteStat1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tbl', models.TextField(blank=True, null=True)),
                ('idx', models.TextField(blank=True, null=True)),
                ('stat', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sqlite_stat1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('trackid', models.AutoField(db_column='TrackId', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('albumid', models.IntegerField(blank=True, db_column='AlbumId', null=True)),
                ('mediatypeid', models.IntegerField(db_column='MediaTypeId')),
                ('genreid', models.IntegerField(blank=True, db_column='GenreId', null=True)),
                ('composer', models.TextField(blank=True, db_column='Composer', null=True)),
                ('milliseconds', models.IntegerField(db_column='Milliseconds')),
                ('bytes', models.IntegerField(blank=True, db_column='Bytes', null=True)),
                ('unitprice', models.TextField(db_column='UnitPrice')),
            ],
            options={
                'db_table': 'tracks',
                'managed': False,
            },
        ),
    ]
