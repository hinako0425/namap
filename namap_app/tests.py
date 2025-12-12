from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer,Activity

class CustomerModelTests(TestCase):
    """
    Customerモデルに関するテスト
    """
    def test_is_empty(self):
        """初期状態ではデータが0件であること"""
        saved_customers = Customer.objects.all()
        self.assertEqual(saved_customers.count(),0)
    
    def test_create_customer(self):
        """顧客データを1件作成し、正しく保存されるか"""
        #1.データを作成・保存
        customer = Customer.objects.create(
            company_name= "テスト株式会社",
            contact_name="テスト 太郎",
            email="test@example.com"
        )
        #2.データベースから全件取得
        saved_customers = Customer.objects.all()

        #3.検証
        self.assertEqual(saved_customers.count(),1)
        self.assertEqual(saved_customers[0].company_name,"テスト株式会社")

class CustomerViewTests(TestCase):
    """View(画面表示)に関するテスト"""
    def setUp(self):
        #テスト用ユーザーを作成
        self.user = User.objects.create_user(username='testuser',password='password')

        #このユーザーが担当する顧客を作成
        self.customer = Customer.objects.create(
            company_name="自分の担当顧客",
            contact_name="担当者A",
            email="a@example.com",
            user=self.user #重要：このユーザーに紐づける
        )

        #別のユーザーを作成(権限確認用)
        self.other_user=User.objects.create_user(username='otheruser',password='password')

    def test_login_required(self):
        """ログインしていない場合、ログインページにリダイレクトされるか"""
        # ログインせずに一覧ページにアクセス
        response = self.client.get(reverse('customer_list'))

        # 302リダイレクト
        self.assertEqual(response.status_code,302)

        #リダイレクト先がログインページであることを確認
        self.assertIn('/accounts/login/',response.url)

    def test_logged_in_users_can_see_list(self):
        """ログインユーザーは自分の担当顧客一覧を見られるか"""
        #1.ログインする
        self.client.force_login(self.user)
        #2.一覧ページにアクセス
        response=self.client.get(reverse('customer_list'))
        #3.正常に表示されるはず(ステータスコード200)
        self.assertEqual(response.status_code,200)
        #4.画面に「自分の担当顧客」という文字が含まれているか検証
        self.assertContains(response,"自分の担当顧客")

    def test_cannot_see_others_data(self):
        """別のユーザーでログインした場合、他人のデータは見えないはず"""
        #1.別のユーザーでログイン
        self.client.force_login(self.other_user)
        #2.一覧ページにアクセス
        response=self.client.get(reverse('customer_list'))
        #3.ページ自体は表示されるが...
        self.assertEqual(response.status_code,200)
        #4. 他人の顧客データ(self.customer)は表示されていないはず
        self.assertNotContains(response,"自分の担当顧客")