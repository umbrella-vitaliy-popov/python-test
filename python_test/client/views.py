from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .models import Client

# Insert views here


def set_if_not_empty(dictionary, key, value):
    if value is not None and value != '':
        dictionary[key] = value


class ClientCreateView(CreateView):
    model = Client
    template_name = 'create-update-form.html'
    fields = [
        'client_name',
        'contact_name',
        'email_address',
        'phone_number',
        'street_name',
        'suburb',
        'postcode',
        'state'
    ]

    def get_form(self, form_class=None):
        form = super(ClientCreateView, self).get_form(form_class)
        form.fields['contact_name'].required = False
        form.fields['street_name'].required = False
        form.fields['suburb'].required = False
        form.fields['postcode'].required = False
        form.fields['state'].required = False
        return form


class ClientDetailView(DetailView):
    template_name = 'detail.html'

    def get_object(self):
        return get_object_or_404(Client, id=self.kwargs.get("id"))


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'create-update-form.html'
    fields = [
        'client_name',
        'contact_name',
        'email_address',
        'phone_number',
        'street_name',
        'suburb',
        'postcode',
        'state'
    ]

    def get_form(self, form_class=None):
        form = super(ClientUpdateView, self).get_form(form_class)
        form.fields['contact_name'].required = False
        form.fields['street_name'].required = False
        form.fields['suburb'].required = False
        form.fields['postcode'].required = False
        form.fields['state'].required = False
        return form

    def get_object(self):
        return get_object_or_404(Client, id=self.kwargs.get("id"))


class ClientListView(ListView):
    template_name = 'list.html'

    def get_queryset(self):
        query_dict = {}
        set_if_not_empty(query_dict, 'client_name__contains', self.request.GET.get('client_name'))
        set_if_not_empty(query_dict, 'phone_number__contains', self.request.GET.get('phone_number'))
        set_if_not_empty(query_dict, 'email_address__contains', self.request.GET.get('email_address'))
        set_if_not_empty(query_dict, 'suburb__contains', self.request.GET.get('suburb'))
        ordering = self.request.GET.get('ordering', '-client_name')
        return Client.objects.all().filter(**query_dict).order_by(ordering)


