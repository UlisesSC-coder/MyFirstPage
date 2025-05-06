from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My First Page'
        context['message'] = 'Welcome to my first Django page!'
        context['name'] = "Rigoberto"
        context["data"] = [
            {"name": "John", "age": 30},
            {"name": "Jane", "age": 25},
            {"name": "Doe", "age": 22},
        ]
        return context