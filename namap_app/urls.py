from django.urls import path
from .views import(
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    ajax_add_activity,
)#作成したCBVをインポート

urlpatterns = [
    #顧客一覧ページ
    #path('',...)はプロジェクトのurls.pyから引き継いだルートURLを指す
    path('',CustomerListView.as_view(),name = 'customer_list'),

    #顧客詳細ページ
    #<int:pk>はURLの一部(顧客のID)を変数として受け取るという意味
    #例：　/customer/1/ ,/customer/2/
    path('customer/<int:pk>/',CustomerDetailView.as_view(),name='customer_detail'),

    #新規登録ページ
    path('customer/new/',CustomerCreateView.as_view(),name='customer_create'),

    #更新ページ
    path('customer/<int:pk>/edit/',CustomerUpdateView.as_view(),name='customer_update'),

    #削除ページ
    path('customer/<int:pk>/delete',CustomerDeleteView.as_view(),name='customer_delete'),

    #Ajax処理用URL
    path('ajax/add_activity/',ajax_add_activity,name='ajax_add_activity'),
]