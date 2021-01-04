from . import views
from django.urls import path

urlpatterns=[

   path('login/',views.loggin,name='login'),
   path('logout/',views.logoutPage,name='logout'),
   path('userprofile/',views.userprofile,name='userprofile'),
   path('alluserprofile/',views.alluserprofile,name='alluserprofile'),
   path('register/',views.register,name='register'),
   path('stock/',views.dashboard,name='stock'),

# category
   path('category/',views.categoryAdd,name='category'),
   path('edit/<int:id>',views.categoryEdit,name='edit'),
   path('update/<int:id>',views.categoryUpdate,name='update'),
   path('delete/<int:id>',views.categoryDelete,name='delete'),
   path('view/',views.categoryView,name='view'),

# tag
   path('tag/',views.tagAdd,name='tag'),
   path('tagedit/<int:id>',views.tagEdit,name='tagedit'),
   path('tagupdate/<int:id>',views.tagUpdate,name='tagupdate'),
   path('tagdelete/<int:id>',views.tagDelete,name='tagdelete'),
   path('tagview/',views.tagView,name='tagview'),

# product

   path('product/', views.productAdd, name='product'),
   path('productview/', views.productView, name='productview'),
   path('productedit/<int:id>', views.productEdit, name='productedit'),
   path('productupdate/<int:id>', views.productUpdate, name='productupdate'),
   path('productdelete/<int:id>', views.productDelete, name='productdelete'),

]