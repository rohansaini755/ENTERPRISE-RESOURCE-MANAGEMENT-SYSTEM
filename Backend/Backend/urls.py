"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Farmer import views as far
from Associated_company import views as cmp
from Products import views as pr
from Transactions import views as tr
from Branch import views as br
urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',far.check),
    path('new_farmer/',far.new_farmer),
    path('farmer_list/',far.get_all_farmer),
    path('new_company/',cmp.new_company),
    path('company_list/',cmp.get_all_company),
    path('company_detail_v/',cmp.company_detail),
    path('new_product/',pr.new_product),
    path('product_list/',pr.get_all_product),
    path('products/',pr.product_list),
    path('farmer_detail/',far.farmer_profile),
    path('add_transaction/',tr.new_transaction),
    path('transaction_list/',tr.all_transaction),
    path('farmer_transaction/',tr.farmer_transaction),
    path('branch/',br.add_branch),
    path('login/',br.login),
    path('session/',br.session),
    path('branch-list/',br.get_all_branch),
    path('branch-profile/',br.branch_profile),
    path('add-template/',pr.new_template),
    path('template/',pr.get_all_template),
]
