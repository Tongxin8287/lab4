#coding:utf-8
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from books.models import Author,Book
from django.http import HttpResponse
import MySQLdb
global ISBN
global Title
global Author_name
global Publisher
global PublishDate
global Price
global isbn_up
def first_page(request):
	return render_to_response('First_page.html')
def search_t(request):
	return render_to_response('Search.html')
def search_a(request):
	key = request.GET['Author_name']
	if not key:
		return render_to_response('No_in.html')
	else:
		author_id = Author.objects.filter(Name = key)
		books = Book.objects.filter(AuthorID = author_id)
		return render_to_response('Result.html',locals())
def add_book_t(request):
	return render_to_response('add_book.html')
def add_book_a(request):
	global ISBN
	global Title
	global Author_name
	global Publisher
	global PublishDate
	global Price
	ISBN = request.GET['ISBN']
	Title = request.GET['Title']
	Author_name = request.GET['Author_name']
	Publisher = request.GET['Publisher']
	PublishDate = request.GET['PublishDate']
	Price = request.GET['Price']
	is_exist = Author.objects.filter(Name = Author_name)
	if not ISBN:
		return render_to_response('No_in.html')
	else:
		if is_exist:
			book_add = Book(ISBN = ISBN,Title = Title,AuthorID = Author.objects.get(Name = Author_name),Publisher = Publisher,\
				PublishDate = PublishDate, Price = Price)
			book_add.save()
			return render_to_response('First_page.html')
		else:
			return render_to_response('add_author.html')
def add_author_a(request):
	global ISBN
	global Title
	global Author_name
	global Publisher
	global PublishDate
	global Price
	AuthorID = request.GET['AuthorID']
	Name = request.GET['Name']
	Age = request.GET['Age']
	Country = request.GET['Country']
	if not AuthorID:
		return render_to_response('No_in.html')
	else:
		auth_add = Author(AuthorID = AuthorID, Name = Name, Age = Age, Country = Country)
		auth_add.save()
		book_add = Book(ISBN = ISBN,Title = Title,AuthorID = Author.objects.get(Name = Author_name),Publisher = Publisher,\
				PublishDate = PublishDate, Price = Price)
		book_add.save()
	return render_to_response('First_page.html')
def detail(request,isbn):
	b = Book.objects.get(ISBN = isbn)
	a = b.AuthorID
	return render_to_response('Detail.html',locals())
def delete_a(request,isbn):
	book_del = Book.objects.get(ISBN = isbn)
	book_del.delete()
	return render_to_response('First_page.html')
def update_t(request,isbn):
	global isbn_up
	isbn_up = isbn
	return render_to_response('Update.html')
def update_a(request):
	global isbn_up
	global ISBN
	global Title
	global Author_name
	global Publisher
	global PublishDate
	global Price
	book = Book.objects.get(ISBN = isbn_up)
	ISBN = book.ISBN
	Title = book.Title
	Author_name = request.GET['Author_name']
	Publisher = request.GET['Publisher']
	PublishDate = request.GET['PublishDate']
	Price = request.GET['Price']
	have_auth = Author.objects.filter(Name = Author_name)
	if Publisher:
		book.Publisher = Publisher
	if PublishDate:
		book.PublishDate = PublishDate
	if Price:
		book.Price = Price
	if Author_name:
		if have_auth:
			book.AuthorID = Author.objects.get(Name = Author_name)
		else:
			return render_to_response('add_author.html')
	book.save()
	return render_to_response('First_page.html')

