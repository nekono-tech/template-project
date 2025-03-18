from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    トップページを表示するビュー
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """
        コンテキストデータを取得する
        """
        context = super().get_context_data(**kwargs)

        # コンテキストデータを追加する
        context["title"] = "トップページ"
        return context
