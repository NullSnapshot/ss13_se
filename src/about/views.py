
from django.views import generic

from .utils import load_readme


class AboutView(generic.TemplateView):
    template_name = 'about/about.html'
    # The readme will only be loaded once at startup and then stored in mem.
    readme_md = load_readme()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about_md'] = self.readme_md
        return context

