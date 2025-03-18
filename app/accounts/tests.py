# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AccountsTestCase(TestCase):
    def setUp(self):
        """テストユーザーの作成"""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.login_url = reverse("accounts:login")
        self.logout_url = reverse("accounts:logout")
        self.home_url = reverse("home")

    def test_login_success(self):
        """ログイン成功のテスト"""
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "testpass123"}
        )
        # ログイン後にホームページにリダイレクトされることを確認
        self.assertRedirects(response, self.home_url)
        # ユーザーが認証されていることを確認
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_failure(self):
        """ログイン失敗のテスト"""
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "wrongpass"}
        )
        # ログインページに留まることを確認
        self.assertEqual(response.status_code, 200)
        # ユーザーが認証されていないことを確認
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        """ログアウトのテスト"""
        # 最初にログイン
        self.client.login(username="testuser", password="testpass123")
        # ログアウトを実行
        response = self.client.post(self.logout_url)
        # ログアウト後にホームページにリダイレクトされることを確認
        self.assertRedirects(response, self.home_url)
        # ユーザーが認証されていないことを確認
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_page_loads(self):
        """ログインページの表示テスト"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")
