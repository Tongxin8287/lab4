from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('books.views',
    # Examples:
    # url(r'^$', 'booksite.views.home', name='home'),
    # url(r'^booksite/', include('booksite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','first_page'),
    url(r'search/$','search_t'),
    url(r'result/$','search_a'),
    # url(r'^result/author/$','author_result'),
    url(r'detail/(\d+)$','detail',name = 'Detail'),
    url(r'add/$','add_book_t'),
    url(r'add_book/$','add_book_a'),
    url(r'add_author/$','add_author_a'),
    url(r'delete/(\d+)$','delete_a', name = 'Delete'),
    url(r'^update/(\d+)$','update_t', name = 'Update'),
    url(r'update_a/$','update_a'),
    # url(r'update/(\d+)$','update_a', name = 'Update'),
    # url(r'^add/book/success/$','search_t'),
)
