from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    """ログインページ"""

    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """ログイン成功時の処理"""
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        """ログイン失敗時の処理"""
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):
        """コンテキストデータの取得"""
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        """ログイン成功時のURLの取得"""
        return str(self.success_url)


class CustomLogoutView(LogoutView):
    """ログアウトページ"""

    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        """ログアウト処理"""
        response = super().dispatch(request, *args, **kwargs)
        return response

    def get_success_url(self):
        """ログアウト成功時のURLの取得"""
        return str(self.success_url)
