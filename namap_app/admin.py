# Register your models here.
from django.contrib import admin
from .models import Customer, Activity, Tag

#Tagモデル用の設定
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name') #一覧にIDと名前を表示
    search_fields = ('name',) #名前で検索できるように

#Customerモデル用の設定
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    #一覧画面に表示するカラム
    list_display = ('company_name','contact_name','email','user','created_at')

    #絞り込み（フィルター）機能を追加
    list_filter = ('user','tags','created_at')

    #検索機能を追加（会社名、担当者名、メールで検索可能に）
    search_fields = ('company_name','contact_name','email')

    #編集画面でのレイアウトを調整
    fieldsets = (
        ('基本情報',{'fields':('company_name','contact_name','email','phone')}),
        ('担当・タグ',{'fields':('user','tags')}),
    )

    #多対多(tags)を編集しやすくする
    filter_horizontal = ('tags',)

    #編集画面で自動入力される項目を読み取り専用に
    readonly_fields = ('created_at','updated_at')

#Activityモデル用の設定
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('customer','activity_date','status','created_at')
    list_filter = ('status','activity_date','customer__user') #顧客の担当営業でも絞り込める
    search_fields = ('customer__company_name','note') #顧客名やメモで検索

    #日付での絞り込みを便利にする
    date_hierarchy = 'activity_date'

    #編集画面での項目
    fields = ('customer','activity_date','status','note')

    #顧客の選択を検索ボックス　(raw_id_fields)にして表示を高速化
    raw_id_fields = ('customer',)