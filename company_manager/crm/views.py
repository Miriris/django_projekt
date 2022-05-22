from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
import crm.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from crm.forms import CompanyForm


class IndexView(TemplateView):
    template_name = "index.html"


class CompanyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "company/create_company.html"
    form_class = CompanyForm
    success_url = reverse_lazy("index")
    # Translators: This message is shown after successful creation of a company.
    success_message = _("Company was created successfully.")


class CompanyListView(LoginRequiredMixin, ListView):
    model = models.Company
    template_name = "company/company_list.html"


class OpportunityCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "crm.add_opportunity"
    model = models.Opportunity
    template_name = "opportunity/create_opportunity.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")
    success_message = "Opportunity was created successfully."


class OpportunityUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "crm.change_opportunity"
    model = models.Opportunity
    template_name = "opportunity/update_opportunity.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("opportunity_list")


class OpportunityListView(ListView):
    model = models.Opportunity
    template_name = "opportunity/opportunity_list.html"


class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ["department", "phone_number", "office_number", "manager"]
    template_name = "employee/update_employee.html"
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."

    def get_object(self, queryset=None):
        return self.request.user.employee
