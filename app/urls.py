#Finsys Final
from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('',views.Fin_index,name='Fin_index'),
    path('Company_Registration',views.Fin_CompanyReg,name='Fin_CompanyReg'),
    path('Company_Registration2/<id>',views.Fin_CompanyReg2,name='Fin_CompanyReg2'),
    path('Distributor_Registration',views.Fin_DistributorReg,name='Fin_DistributorReg'),
    path('Distributor_Registration_Action',views.Fin_DReg_Action,name='Fin_DReg_Action'),
    path('Distributor_Registration2/<id>',views.Fin_DReg2,name='Fin_DReg2'), 
    path('Distributor_Registration_Action2/<id>',views.Fin_DReg2_Action2,name='Fin_DReg2_Action2'), 
    path('Staff_Registration',views.Fin_StaffReg,name='Fin_StaffReg'),
    path('Adminhome',views.Fin_Adminhome,name='Fin_Adminhome'),
    path('LogIn',views.Fin_login,name='Fin_login'),
    path('Payment_Terms',views.Fin_PaymentTerm,name='Fin_PaymentTerm'),
    path('add_payment_terms',views.Fin_add_payment_terms,name='Fin_add_payment_terms'),
    path('Distributor',views.Fin_ADistributor,name='Fin_ADistributor'),
    path('Distributor_Request',views.Fin_Distributor_Request,name='Fin_Distributor_Request'),
    path('Distributor_Request_overview/<id>',views.Fin_Distributor_Req_overview,name='Fin_Distributor_Req_overview'),
    path('DReq_Accept/<id>',views.Fin_DReq_Accept,name='Fin_DReq_Accept'), 
    path('DReq_Reject/<id>',views.Fin_DReq_Reject,name='Fin_DReq_Reject'),
    path('All_Distributors',views.Fin_All_distributors,name='Fin_All_distributors'),
    path('All_Distributor_Overview/<id>',views.Fin_All_Distributor_Overview,name='Fin_All_Distributor_Overview'),  
    path('Distributor_Home',views.Fin_DHome,name='Fin_DHome'),
    path('companyReg_action',views.Fin_companyReg_action,name='Fin_companyReg_action'),
    path('CompanyReg2_action2/<id>',views.Fin_CompanyReg2_action2,name='Fin_CompanyReg2_action2'),
    path('Fin_Modules/<id>',views.Fin_Modules,name='Fin_Modules'),
    path('Add_Modules/<id>',views.Fin_Add_Modules,name='Fin_Add_Modules'),
    path('Company_Home',views.Fin_Com_Home,name='Fin_Com_Home'),
    path('AClients',views.Fin_AClients,name='Fin_AClients'), 
    path('Fin_AClients_Request',views.Fin_AClients_Request,name='Fin_AClients_Request'),  
    path('Fin_AClients_Request_OverView/<id>',views.Fin_AClients_Request_OverView,name='Fin_AClients_Request_OverView'),
    path('Client_Req_Accept/<id>',views.Fin_Client_Req_Accept,name='Fin_Client_Req_Accept'),
    path('Client_Req_Reject/<id>',views.Fin_Client_Req_Reject,name='Fin_Client_Req_Reject'),
    path('Fin_Admin_clients',views.Fin_Admin_clients,name='Fin_Admin_clients'), 
    path('Fin_Admin_clients_overview/<id>',views.Fin_Admin_clients_overview,name='Fin_Admin_clients_overview'),
    path('LOgout',views.logout,name="logout"),
    path('Company_Profile',views.Fin_Company_Profile,name="Fin_Company_Profile"),
    path('Fin_staffReg_action',views.Fin_staffReg_action,name='Fin_staffReg_action'),
    path('StaffReg2/<id>',views.Fin_StaffReg2,name='Fin_StaffReg2'),
    path('StaffReg2_Action/<id>',views.Fin_StaffReg2_Action,name='Fin_StaffReg2_Action'),
    path('Staff_Req',views.Fin_Staff_Req,name='Fin_Staff_Req'),
    path('Staff_Req_Accept/<id>',views.Fin_Staff_Req_Accept,name='Fin_Staff_Req_Accept'),
    path('Staff_Req_Reject/<id>',views.Fin_Staff_Req_Reject,name='Fin_Staff_Req_Reject'),
    path('All_Staffs',views.Fin_All_Staff,name='Fin_All_Staff'),
    path('DClient_req',views.Fin_DClient_req,name='Fin_DClient_req'),
    path('DClient_Req_Accept/<id>',views.Fin_DClient_Req_Accept,name='Fin_DClient_Req_Accept'),
    path('DClient_Req_Reject/<id>',views.Fin_DClient_Req_Reject,name='Fin_DClient_Req_Reject'), 
    path('DClients',views.Fin_DClients,name='Fin_DClients'),
    path('DProfile',views.Fin_DProfile,name='Fin_DProfile'),
    path('Edit_Modules',views.Fin_Edit_Modules,name='Fin_Edit_Modules'),
    path('Edit_Modules_Action',views.Fin_Edit_Modules_Action,name='Fin_Edit_Modules_Action'),
    path('Anotification',views.Fin_Anotification,name='Fin_Anotification'),
    path('Anoti_Overview/<id>',views.Fin_Anoti_Overview,name='Fin_Anoti_Overview'), 
    path('Module_Updation_Accept/<id>',views.Fin_Module_Updation_Accept,name='Fin_Module_Updation_Accept'),
    path('Module_Updation_Reject/<id>',views.Fin_Module_Updation_Reject,name='Fin_Module_Updation_Reject'),
    path('Change_payment_terms',views.Fin_Change_payment_terms,name='Fin_Change_payment_terms'),
    path('payment_terms_Updation_Accept/<id>',views.Fin_payment_terms_Updation_Accept,name='Fin_payment_terms_Updation_Accept'),
    path('payment_terms_Updation_Reject/<id>',views.Fin_payment_terms_Updation_Reject,name='Fin_payment_terms_Updation_Reject'),
    path('Dnotification',views.Fin_Dnotification,name='Fin_Dnotification'),
    path('Dnoti_Overview/<id>',views.Fin_Dnoti_Overview,name='Fin_Dnoti_Overview'), 
    path('DModule_Updation_Accept/<id>',views.Fin_DModule_Updation_Accept,name='Fin_DModule_Updation_Accept'),
    path('DModule_Updation_Reject/<id>',views.Fin_DModule_Updation_Reject,name='Fin_DModule_Updation_Reject'),
    path('ADpayment_terms_Updation_Accept/<id>',views.Fin_Dpayment_terms_Updation_Accept,name='Fin_Dpayment_terms_Updation_Accept'),
    path('ADpayment_terms_Updation_Reject/<id>',views.Fin_ADpayment_terms_Updation_Reject,name='Fin_ADpayment_terms_Updation_Reject'),
    path('Cnotification',views.Fin_Cnotification,name='Fin_Cnotification'),
    path('Wrong',views.Fin_Wrong,name='Fin_Wrong'),
    path('Wrong_Action',views.Fin_Wrong_Action,name='Fin_Wrong_Action'),
    path('DChange_payment_terms',views.Fin_DChange_payment_terms,name='Fin_DChange_payment_terms'),
    path('Client_delete/<id>',views.Fin_Client_delete,name='Fin_Client_delete'),
    path('Distributor_delete/<id>',views.Fin_Distributor_delete,name='Fin_Distributor_delete'),
    path('Staff_delete/<id>',views.Fin_Staff_delete,name='Fin_Staff_delete'),
    path('Edit_Company_profile',views.Fin_Edit_Company_profile,name='Fin_Edit_Company_profile'),
    path('Edit_Company_profile_Action',views.Fin_Edit_Company_profile_Action,name='Fin_Edit_Company_profile_Action'),
    path('Edit_Staff_profile',views.Fin_Edit_Staff_profile,name='Fin_Edit_Staff_profile'),
    path('Edit_Staff_profile_Action',views.Fin_Edit_Staff_profile_Action,name='Fin_Edit_Staff_profile_Action'),
    path('Edit_Dprofile',views.Fin_Edit_Dprofile,name='Fin_Edit_Dprofile'),
    path('Edit_Dprofile_Action',views.Fin_Edit_Dprofile_Action,name='Fin_Edit_Dprofile_Action'),
    path('DClient_req_overview/<id>',views.Fin_DClient_req_overview,name='Fin_DClient_req_overview'),
    path('DClients_overview/<id>',views.Fin_DClients_overview,name='Fin_DClients_overview'),
    path('DClient_remove/<id>',views.Fin_DClient_remove,name='Fin_DClient_remove'),
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


    # harikrishnan---------------------

    path('recurring_bill_list',views.recurring_bill_list,name="recurring_bill_list"),




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)