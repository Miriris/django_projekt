from django.urls import path
import crm.views as views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("company/create", views.CompanyCreateView.as_view(), name="create_company"),
    path("company/list/", views.CompanyListView.as_view(), name="company_list"),
    path("opportunity/create", views.OpportunityCreateView.as_view(), name="create_opportunity"),
    path("opportunity/opportunities", views.OpportunityListView.as_view(), name="opportunity_list"),
    path("opportunity/update/<int:pk>", views.OpportunityUpdateView.as_view(), name="update_opportunity"),
    path("employee/", views.EmployeeUpdateView.as_view(), name="update_employee"),
]

