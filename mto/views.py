from django.http import JsonResponse
from django.views.generic import CreateView
from .forms import MtoRegistrationForm


class MtoRegistrationView(CreateView):
    form_class = MtoRegistrationForm
    template_name = "mto/registration.html"

    def get_form_kwargs(self):
        kwargs = super(MtoRegistrationView, self).get_form_kwargs()
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=200)

    def form_valid(self, form):
        data = {}
        user = form.save(commit=False)
        user.username = form.instance.first_name
        user.is_active = True
        user.save()
        data['message'] = "Mto has been created successfully"
        return JsonResponse(data)
