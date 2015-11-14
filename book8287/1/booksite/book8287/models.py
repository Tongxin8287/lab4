from django.db import models

# class Publisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state_province = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.URLField()

# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()
# def make_uuid():
# 	return str(uuid.uuid4()).replace('-','')
class Author(models.Model):
	AuthorID = models.IntegerField(primary_key = True,max_length = 50)
	Name = models.CharField(max_length = 50)
	Age = models.IntegerField(max_length = 30)
	Country = models.CharField(max_length = 50)
	class Meta:
			db_table = 'Author'

class Book(models.Model):
	ISBN = models.IntegerField(primary_key = True,max_length = 32)
	Title = models.CharField(max_length = 30)
	AuthorID = models.ForeignKey(Author)
	Publisher = models.CharField(max_length = 50)
	PublishDate = models.DateField(max_length = 50)
	Price = models.CharField(max_length = 50)
	class Meta:
			db_table = 'Book'
