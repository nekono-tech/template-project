from django.test import Client, TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    """
    HomeViewのテストクラス
    """

    def setUp(self):
        """
        テストの前処理
        """
        self.client = Client()
        self.url = reverse('home')  # URLの名前解決

    def test_home_view_status_code(self):
        """
        ステータスコードが200(OK)であることを確認
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        """
        正しいテンプレートが使用されていることを確認
        """
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_view_context(self):
        """
        コンテキスト変数が正しく渡されていることを確認
        """
        response = self.client.get(self.url)
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], 'トップページ')

    def test_home_view_content(self):
        """
        レスポンスの内容に期待するテキストが含まれていることを確認
        """
        response = self.client.get(self.url)
        self.assertContains(response, 'Django App へようこそ')
