from django.urls import  path
from . import views
#from django.contrib.auth.views import

urlpatterns =[
path('',views.home, name='home'),
path('dashboard/',views.dashboard, name='dashboard'),
path('faculty_info/',views.faculty_info, name='faculty_info'),
path('results/',views.results, name='results'),
path('book_pub/',views.book_pub, name='book_pub'),
path('book_cha/',views.book_cha, name='book_cha'),
path('about/', views.about, name='about'),
path('show/', views.show, name='show'),
path('paper/', views.paper, name='paper'),
path('book/', views.book, name='book'),
path('chapter/', views.chapter, name='chapter'),
# path('generateinvoice/<int:pk>/', views.GenerateInvoice.as_view(), name = 'generateinvoice'),
# path('generate_pdf_through_template/', views.generate_pdf_through_template, name='generate_pdf_through_template'),
# path('render_pdf/', views.render_pdf, name='render_pdf'),
]
