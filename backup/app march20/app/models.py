#Finsys Final
import datetime
from django.db import models
from django_countries.fields import CountryField
from datetime import timedelta
from datetime import date
from django.utils import timezone

class Fin_Payment_Terms(models.Model):
    payment_terms_number = models.IntegerField(null=True,blank=True)  
    payment_terms_value = models.CharField(max_length=100,null=True,blank=True) 
    days = models.CharField(max_length=100,null=True,blank=True) 

class Fin_Login_Details(models.Model):
    First_name = models.CharField(max_length=255,null=True,blank=True)
    Last_name = models.CharField(max_length=255,null=True,blank=True)
    User_name = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    User_Type = models.CharField(max_length=255,null=True,blank=True) 

class Fin_Distributors_Details(models.Model):  
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Payment_Term =  models.ForeignKey(Fin_Payment_Terms, on_delete=models.CASCADE,null=True,blank=True)
    Distributor_Code = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=255,null=True,blank=True) 
    Contact = models.CharField(max_length=255,null=True,blank=True)
    Image = models.ImageField(null=True,blank = True,upload_to = 'image/distributor') 
    Start_Date = models.DateField(auto_now_add=True,null=True)
    End_date = models.DateField(max_length=255,null=True,blank=True)
    Admin_approval_status = models.CharField(max_length=255,null=True,blank=True)   

class Fin_Company_Details(models.Model): 
    Payment_Term = models.ForeignKey(Fin_Payment_Terms, on_delete=models.CASCADE,null=True,blank=True)
    Distributor_id = models.ForeignKey(Fin_Distributors_Details, on_delete=models.CASCADE,null=True,blank=True)
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Company_name = models.CharField(max_length=255,null=True,blank=True)
    Business_name = models.CharField(max_length=255,null=True,blank=True)
    Industry = models.CharField(max_length=255,null=True,blank=True)
    Company_Type = models.CharField(max_length=255,null=True,blank=True)

    Company_Code = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=255,null=True,blank=True) 
    Contact = models.CharField(max_length=255,null=True,blank=True)
    Address = models.TextField(max_length=255,null=True,blank=True)
    City = models.CharField(max_length=255,null=True,blank=True)
    State = models.CharField(max_length=255,null=True,blank=True)
    Country = models.CharField(max_length=255,null=True,blank=True)
    Pincode = models.IntegerField(null=True,blank=True)
    Pan_NO = models.CharField(max_length=255,null=True,blank=True)
    GST_Type = models.CharField(max_length=255,null=True,blank=True)
    GST_NO = models.CharField(max_length=255,null=True,blank=True)
    Image = models.ImageField(null=True,blank = True,upload_to = 'image/company') 
    Start_Date = models.DateField(auto_now_add=True,null=True)
    End_date = models.DateField(max_length=255,null=True,blank=True)
    Payment_Type = models.CharField(max_length=255,null=True,blank=True)
    Accountant = models.CharField(max_length=255,null=True,blank=True)
    Admin_approval_status = models.CharField(max_length=255,null=True,blank=True)
    Distributor_approval_status = models.CharField(max_length=255,null=True,blank=True)
    Registration_Type = models.CharField(max_length=255,null=True,blank=True)


class Fin_Modules_List(models.Model):
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company_id = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)

    # -----items-----
    Items = models.IntegerField(null=True,default=0) 
    Price_List = models.IntegerField(null=True,default=0) 
    Stock_Adjustment = models.IntegerField(null=True,default=0) 

    # --------- CASH & BANK-----
    Cash_in_hand = models.IntegerField(null=True,default=0) 
    Offline_Banking = models.IntegerField(null=True,default=0)
    Bank_Reconciliation = models.IntegerField(null=True,default=0)
    UPI = models.IntegerField(null=True,default=0)
    Bank_Holders = models.IntegerField(null=True,default=0)
    Cheque = models.IntegerField(null=True,default=0)
    Loan_Account = models.IntegerField(null=True,default=0)

    #  ------SALES MODULE -------
    Customers  = models.IntegerField(null=True,default=0)
    Invoice = models.IntegerField(null=True,default=0) 
    Estimate = models.IntegerField(null=True,default=0) 
    Sales_Order = models.IntegerField(null=True,default=0) 
    Recurring_Invoice = models.IntegerField(null=True,default=0) 
    Retainer_Invoice = models.IntegerField(null=True,default=0) 
    Credit_Note = models.IntegerField(null=True,default=0) 
    Payment_Received = models.IntegerField(null=True,default=0) 
    Delivery_Challan = models.IntegerField(null=True,default=0)


    #  ---------PURCHASE MODULE--------- 
    Vendors = models.IntegerField(null=True,default=0) 
    Bills = models.IntegerField(null=True,default=0) 
    Recurring_Bills = models.IntegerField(null=True,default=0) 
    Debit_Note = models.IntegerField(null=True,default=0) 
    Purchase_Order = models.IntegerField(null=True,default=0) 
    Expenses = models.IntegerField(null=True,default=0) 
    Recurring_Expenses = models.IntegerField(null=True,default=0) 
    Payment_Made = models.IntegerField(null=True,default=0) 

    # --------EWay_Bill-----
    EWay_Bill = models.IntegerField(null=True,default=0) 


    #  -------ACCOUNTS--------- 
    Chart_of_Accounts = models.IntegerField(null=True,default=0)  
    Manual_Journal = models.IntegerField(null=True,default=0)  
    Reconcile = models.IntegerField(null=True,default=0) 


    # -------PAYROLL------- 
    Employees = models.IntegerField(null=True,default=0) 
    Employees_Loan = models.IntegerField(null=True,default=0)  
    Holiday = models.IntegerField(null=True,default=0) 
    Attendance = models.IntegerField(null=True,default=0) 
    Salary_Details = models.IntegerField(null=True,default=0) 


    update_action = models.IntegerField(null=True,default=0) 
    status = models.CharField(max_length=100,null=True,default='New')  


class Fin_Staff_Details(models.Model):
    company_id = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    Email = models.CharField(max_length=255,null=True,blank=True) 
    img = models.ImageField(null=True,blank = True,upload_to = 'image/staff')    
    Company_approval_status = models.CharField(max_length=255,null=True,blank=True)  

class Fin_Payment_Terms_updation(models.Model):
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Payment_Term = models.ForeignKey(Fin_Payment_Terms, on_delete=models.CASCADE,null=True,blank=True)

    status = models.CharField(max_length=100,null=True,default='New') 


class Fin_ANotification(models.Model): 
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Modules_List = models.ForeignKey(Fin_Modules_List, on_delete=models.CASCADE,null=True,blank=True)
    PaymentTerms_updation = models.ForeignKey(Fin_Payment_Terms_updation, on_delete=models.CASCADE,null=True,blank=True)
    
    Title = models.CharField(max_length=255,null=True,blank=True)
    Discription = models.CharField(max_length=255,null=True,blank=True) 
    Noti_date = models.DateTimeField(auto_now_add=True,null=True)
    date_created = models.DateField(auto_now_add=True,null=True)
    time=models.TimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=100,null=True,default='New')  

class Fin_DNotification(models.Model): 
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Distributor_id = models.ForeignKey(Fin_Distributors_Details, on_delete=models.CASCADE,null=True,blank=True)
    Modules_List = models.ForeignKey(Fin_Modules_List, on_delete=models.CASCADE,null=True,blank=True)
    PaymentTerms_updation = models.ForeignKey(Fin_Payment_Terms_updation, on_delete=models.CASCADE,null=True,blank=True)
    
    Title = models.CharField(max_length=255,null=True,blank=True)
    Discription = models.CharField(max_length=255,null=True,blank=True) 
    Noti_date = models.DateTimeField(auto_now_add=True,null=True)
    date_created = models.DateField(auto_now_add=True,null=True)
    time=models.TimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=100,null=True,default='New')     
   
       
#----------------Shemeem --------------Items&ChartOfAccounts----------------
    
class Fin_Units(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)

class Fin_Items(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,null=True)
    item_type = models.CharField(max_length=100,null=True)
    unit = models.CharField(max_length=100,null=True)
    hsn = models.BigIntegerField(null=True, blank = True)
    tax_reference = models.CharField(max_length=100,null=True)
    intra_state_tax = models.IntegerField(null=True, default=0)
    inter_state_tax = models.IntegerField(null=True, default=0)
    sales_account = models.CharField(max_length=100,null=True)
    selling_price = models.FloatField(null=True, default=0.0)
    sales_description = models.CharField(max_length=100,null=True)
    purchase_account = models.CharField(max_length=100,null=True)
    purchase_price = models.FloatField(null=True, default=0.0)
    purchase_description = models.CharField(max_length=100,null=True)
    item_created = models.DateField(auto_now_add = True, auto_now = False, null=True)
    min_stock=models.IntegerField(null=True,default=0)
    inventory_account = models.CharField(max_length=100, null=True, blank=True)
    opening_stock = models.IntegerField(null=True, blank=True,default = 0)
    current_stock = models.IntegerField(default=0,blank=True,null=True)
    stock_in = models.IntegerField(default=0,blank=True,null=True)
    stock_out = models.IntegerField(default=0,blank=True,null=True)
    stock_unit_rate= models.FloatField(default=0.0,blank=True,null=True)
    status = models.CharField(max_length=100,null=True, default='Active')

class Fin_Price_List(models.Model):
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)

    TYPE_CHOICES=(
        ('Sales','Sales'),
        ('Purchase','Purchase'),
    )

    ITEM_RATE_CHOICES=(
        ('percentage','Markup or Markdown the item rates by a percentage'),
        ('individual_rate','Enter the rate individually for each item'),
    )

    type = models.CharField(max_length=15,choices=TYPE_CHOICES,null=True,blank=True,default='Sales')
    item_rate = models.CharField(max_length=100,choices=ITEM_RATE_CHOICES,null=True,blank=True,default='percentage')
    description = models.TextField(blank=True, null=True)
    currency = models.CharField(max_length=255,null=True,blank=True,default='Indian Rupee')
    up_or_down = models.CharField(max_length=100,default='None')
    percentage = models.CharField(max_length=100,null=True,blank=True)
    round_off = models.CharField(max_length=100,default='None', null=True, blank=True)
    created_date = models.DateField(auto_now_add = True, auto_now = False, blank = True, null = True)
    status = models.CharField(max_length=15,default='Active',null=True,blank=True)

class Fin_Company_Payment_Terms(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    term_name = models.CharField(max_length=100, null=True)
    days = models.IntegerField(null=True, default=0)
    
class Fin_Customers(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=10,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    place_of_supply = models.CharField(max_length=100,null=True,blank=True)
    gst_type = models.CharField(max_length=100, null=True)
    gstin = models.CharField(max_length=100,null=True,blank=True,default=None)
    pan_no = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    website = models.CharField(max_length=100, default='',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    price_list = models.ForeignKey(Fin_Price_List, on_delete = models.SET_NULL, null = True)
    payment_terms = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    billing_street = models.CharField(max_length=100,null=True,blank=True)
    billing_city = models.CharField(max_length=100,null=True,blank=True)
    billing_state = models.CharField(max_length=100,null=True,blank=True)
    billing_pincode = models.CharField(max_length=100,null=True,blank=True)
    billing_country = models.CharField(max_length=100,null=True,blank=True)
    ship_street = models.CharField(max_length=100,null=True,blank=True)
    ship_city = models.CharField(max_length=100,null=True,blank=True)
    ship_state = models.CharField(max_length=100,null=True,blank=True)
    ship_pincode = models.CharField(max_length=100,null=True,blank=True)
    ship_country = models.CharField(max_length=100,null=True,blank=True)
    opening_balance = models.FloatField(null=True, blank=True, default=0.0)
    opening_balance_due = models.FloatField(null=True, blank=True, default=0.0)
    open_balance_type = models.CharField(max_length=100,null=True,blank=True)
    current_balance = models.FloatField(null=True, blank=True, default=0.0)
    credit_limit = models.FloatField(null=True, blank=True, default=0.0)
    date = models.DateField(null=True, auto_now_add=True,auto_now=False)
    customer_status = (
        ('Active','Active'),
        ('Inactive','Inactive'),
    )
    status =models.CharField(max_length=150,choices=customer_status,default='Active',null=True,blank=True)

class Fin_Vendors(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=10,null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=10,null=True)
    company = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    website = models.CharField(max_length=100, null=True)
    gst_type = models.CharField(max_length=100, null=True)
    gstin = models.CharField(max_length=100, null=True)
    pan_no = models.CharField(max_length=100, null=True)
    opening_balance = models.FloatField(null=True, blank=True, default=0.0)
    open_balance_type = models.CharField(max_length=100,null=True,blank=True)
    current_balance = models.FloatField(null=True, blank=True, default=0.0)
    credit_limit = models.FloatField(null=True, blank=True, default=0.0)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True, auto_now_add=True,auto_now=False)
    price_list = models.ForeignKey(Fin_Price_List, on_delete = models.SET_NULL, null = True)
    payment_terms = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    billing_street = models.CharField(max_length=100,null=True)
    billing_city = models.CharField(max_length=100,null=True)
    billing_state = models.CharField(max_length=100,null=True)
    billing_pincode = models.CharField(max_length=100,null=True)
    billing_country = models.CharField(max_length=100,null=True)
    ship_street = models.CharField(max_length=100, null=True)
    ship_city = models.CharField(max_length=100, null=True)
    ship_state = models.CharField(max_length=100, null=True)
    ship_pincode = models.CharField(max_length=100, null=True)
    ship_country = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=15,default = 'Active')
    
class Fin_CNotification(models.Model): 
    Login_Id = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Company_id = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    Item = models.ForeignKey(Fin_Items, on_delete = models.CASCADE, null=True, blank=True) # Added - shemeem -> Handle Item's min stock alerts
    Customers = models.ForeignKey(Fin_Customers, on_delete = models.CASCADE, null=True,blank=True) # Added - shemeem -> Handle customer's credit limit alerts
    Vendors = models.ForeignKey(Fin_Vendors, on_delete = models.CASCADE, null=True,blank=True) # Added - shemeem -> Handle vendor's credit limit alerts
    
    Title = models.CharField(max_length=255,null=True,blank=True)
    Discription = models.CharField(max_length=255,null=True,blank=True) 
    Noti_date = models.DateTimeField(auto_now_add=True,null=True)
    date_created = models.DateField(auto_now_add=True,null=True)
    time=models.TimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=100,null=True,default='New')     

class Fin_Items_Transaction_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Fin_Items, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Items_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Fin_Items,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)


class Fin_Chart_Of_Account(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    account_type = models.CharField(max_length=255,null=True,blank=True)
    account_name = models.CharField(max_length=255,null=True,blank=True)
    account_code = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    balance = models.FloatField(null=True, blank=True, default=0.0)
    balance_type = models.CharField(max_length=100,null=True,blank=True)
    credit_card_no = models.CharField(max_length=255,null=True,blank=True)
    sub_account = models.BooleanField(null=True,blank=True, default=False)
    parent_account = models.CharField(max_length=255,null=True,blank=True)
    bank_account_no = models.BigIntegerField(null=True,blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True, blank=True)
    create_status=models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)


class Fin_ChartOfAccount_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    account = models.ForeignKey(Fin_Chart_Of_Account, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)

#End



    
    
# -------------Shemeem--------Price List & Customers-------------------------------


class Fin_PriceList_Items(models.Model):
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    list = models.ForeignKey(Fin_Price_List,on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(Fin_Items,on_delete=models.CASCADE,null=True,blank=True)
    standard_rate = models.FloatField(null=True,blank=True,default=0.0)
    custom_rate=models.FloatField(null=True,blank=True,default=0.0)


class Fin_PriceList_Transaction_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    list = models.ForeignKey(Fin_Price_List,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_PriceList_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    list = models.ForeignKey(Fin_Price_List,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)





class Fin_Customers_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Fin_Customers,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Customers_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Fin_Customers,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

#End


# harikrishnan (start)--------------------------------
    
class Employee(models.Model):
    upload_file = models.FileField(upload_to='file/',blank=True) 
    upload_image = models.ImageField(upload_to='media/',blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    alias = models.CharField(max_length=255,null=True,blank=True)
    employee_mail = models.EmailField(null=True,blank=True)
    employee_number = models.CharField(max_length=255,null=True,blank=True)
    employee_designation = models.CharField(max_length=255,null=True,blank=True)
    function = models.CharField(max_length=255,null=True,blank=True)
    employee_current_location = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.CharField(max_length=255,null=True,blank=True)
    date_of_joining = models.DateField(null=True,blank=True)
    employee_salary_type = models.CharField(max_length=255,null=True,blank=True)
    salary_details = models.CharField(max_length=10,null=True,blank=True)
    salary_effective_from = models.CharField(max_length=255,null=True,blank=True)

    pay_head = models.CharField(max_length=255,null=True,blank=True)
    salary_amount = models.FloatField(null=True,blank=True)
    amount_per_hour = models.IntegerField(null=True,blank=True)
    total_working_hours = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=255,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    blood_group = models.CharField(max_length=255,null=True,blank=True)
    fathers_name_mothers_name = models.CharField(max_length=255,null=True,blank=True)
    spouse_name = models.CharField(max_length=255,null=True,blank=True)
    emergency_contact = models.CharField(max_length=255,null=True,blank=True)
    provide_bank_details = models.CharField(max_length=255,null=True,blank=True)
    account_number = models.CharField(max_length=255,null=True,blank=True)
    ifsc = models.CharField(max_length=255,null=True,blank=True)
    name_of_bank = models.CharField(max_length=255,null=True,blank=True)
    branch_name = models.CharField(max_length=255,null=True,blank=True)
    bank_transaction_type = models.CharField(max_length=255,null=True,blank=True)
    tds_applicable = models.CharField(max_length=255,null=True,blank=True)
    tds_type = models.CharField(max_length=255,null=True,blank=True)
    percentage_amount = models.IntegerField(null=True,blank=True)
    pan_number = models.CharField(max_length=255,null=True,blank=True)
    income_tax_number = models.CharField(max_length=255,null=True,blank=True)
    aadhar_number = models.CharField(max_length=255,null=True,blank=True)
    universal_account_number = models.CharField(max_length=255,null=True,blank=True)
    pf_account_number = models.CharField(max_length=255,null=True,blank=True)
    pr_account_number = models.CharField(max_length=255,null=True,blank=True)
    esi_number = models.CharField(max_length=255,null=True,blank=True)

    street = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    pincode = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    temporary_street = models.CharField(max_length=255,null=True,blank=True)
    temporary_city = models.CharField(max_length=255,null=True,blank=True)
    temporary_state = models.CharField(max_length=255,null=True,blank=True)
    temporary_pincode = models.CharField(max_length=255,null=True,blank=True)
    temporary_country = models.CharField(max_length=255,null=True,blank=True)
    employee_status = models.CharField(max_length=30,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)

class Employee_History(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(null=True,blank=True)
    action = models.CharField(max_length=255,null=True,blank=True)

class Employee_Comment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(default = date.today())

class Holiday(models.Model):
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    holiday_name = models.CharField(max_length=255,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    holiday_days = models.CharField(max_length=255,null=True,blank=True)


class Holiday_Comment(models.Model):
    month = models.CharField(max_length=255,null=True,blank=True)
    year = models.CharField(max_length=255,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(default = date.today())
    
class Employee_Blood_Group(models.Model):
    blood_group = models.CharField(max_length=255,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)

# harikrishnan (end)--------------------------------

class Fin_Banking(models.Model):
    login_details = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)

    bank_name = models.CharField(max_length=255,null=True,blank=True) 
    account_number = models.CharField(max_length=255,null=True,blank=True) 
    ifsc_code = models.CharField(max_length=255,null=True,blank=True) 
    branch_name = models.CharField(max_length=255,null=True,blank=True) 
    opening_balance_type = models.CharField(max_length=255,null=True,blank=True) 
    opening_balance = models.IntegerField(null=True,default=0)
    date = models.DateTimeField(auto_now_add=False,null=True)
    current_balance = models.IntegerField(null=True,default=0)
    bank_status = models.CharField(max_length=255,null=True,blank=True) 
   


class Fin_BankingHistory(models.Model):
    login_details = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    banking = models.ForeignKey(Fin_Banking, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    action = models.CharField(max_length=255,null=True,blank=True)


class Fin_BankHolder(models.Model):
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True, blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True, blank=True)

    Holder_name = models.CharField(max_length=255, null=True, blank=True)
    Alias = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    Email = models.EmailField(max_length=255, null=True, blank=True)
    ACCOUNT_TYPE_CHOICES = [('CC', 'Credit Card'), ('BA', 'Bank Account'),]
    Account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES, default='BA',)

    Set_cheque_book_range = models.BooleanField(default=False)
    Enable_cheque_printing = models.BooleanField(default=False)
    Set_cheque_printing_configuration = models.BooleanField(default=False)

    Mailing_name = models.CharField(max_length=100)
    Address = models.TextField(max_length=255, null=True, blank=True)
    Country = CountryField(max_length=20, null=True, blank=True)
    STATE_CHOICES = [
    ('AN', 'Andaman and Nicobar Islands'),
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CH', 'Chhattisgarh'),
    ('DL', 'National Capital Territory of Delhi'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu and Kashmir'),
    ('LA', 'Ladakh'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OR', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TG', 'Telangana'),
    ('TR', 'Tripura'),
    ('UT', 'Uttarakhand'),
    ('UP', 'Uttar Pradesh'),
    ('WB', 'West Bengal')
    ]
    State = models.CharField(max_length=100, choices=STATE_CHOICES,)
    Pin = models.CharField(max_length=6)

    REGISTRATION_TYPE_CHOICES = [('regular', 'Regular'), ('composition', 'Composition'), ('consumer', 'Consumer'),
                                 ('unregistered', 'Unregistered'),]
    Pan_it_number = models.CharField(max_length=10, blank=True)
    Registration_type = models.CharField(max_length=20, choices=REGISTRATION_TYPE_CHOICES, default='unknown')
    Gstin_un = models.CharField(max_length=15, blank=True)
    Set_alter_gst_details = models.BooleanField(default=False)

    Date = models.DateField(default=datetime.date.today)
    ArithmeticErrormount = models.DecimalField(max_digits=10, decimal_places=2)
    Types = [('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT'),]
    Open_type = models.CharField(max_length=20, choices=Types, default='unknown')

    Swift_code = models.CharField(max_length=11,null=True, blank=True)
    Bank_name = models.CharField(max_length=20, null=True, blank=True)
    Ifsc_code = models.CharField(max_length=15, null=True, blank=True)
    Branch_name = models.CharField(max_length=20, null=True, blank=True)
    Account_number = models.CharField(max_length=20, null=True, blank=True)

    banking_details = models.ForeignKey(Fin_Banking, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.Holder_name
    
    

class Fin_BankHolderComment(models.Model):
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)

    Holder = models.ForeignKey(Fin_BankHolder, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment #{self.id}'
       

class Fin_BankHolderHistory(models.Model):
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    Holder = models.ForeignKey(Fin_BankHolder, on_delete=models.CASCADE)


    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited')
        ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)
    
class Fin_BankingAttachments(models.Model): 

    login_details = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    banking = models.ForeignKey(Fin_Banking, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    file = models.ImageField(null=True,blank = True,upload_to = 'image/banking')
    
class Fin_BankingComments(models.Model): 

    login_details = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    banking = models.ForeignKey(Fin_Banking, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    comment = models.CharField(max_length=255,null=True,blank=True)
    
class Fin_BankTransactions(models.Model): 

    login_details = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    banking = models.ForeignKey(Fin_Banking, on_delete=models.CASCADE,null=True,blank=True)

    from_type = models.CharField(max_length=255,null=True,blank=True) 
    to_type = models.CharField(max_length=255,null=True,blank=True) 
    amount = models.IntegerField(null=True,default=0)
    adjustment_date = models.DateTimeField(auto_now_add=False,null=True)
    description = models.CharField(max_length=255,null=True,blank=True) 
    transaction_type = models.CharField(max_length=255,null=True,blank=True) 
    adjustment_type = models.CharField(max_length=255,null=True,blank=True) 
    current_balance = models.IntegerField(null=True,default=0)
    bank_to_bank = models.IntegerField(null=True,default=0)
    
class Fin_BankTransactionHistory(models.Model): 

    login_details = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    bank_transaction = models.ForeignKey(Fin_BankTransactions, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    action = models.CharField(max_length=255,null=True,blank=True)
    
    
class Holiday_History(models.Model):
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    holiday_name = models.CharField(max_length=255,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    holiday = models.ForeignKey(Holiday,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(null=True,blank=True)
    action = models.CharField(max_length=255,null=True,blank=True)
    

# -------------Shemeem--------Invoice & Vendors-------------------------------

# Invoice

class Fin_Invoice(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Customer = models.ForeignKey(Fin_Customers, on_delete=models.CASCADE, null=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    reference_no = models.IntegerField(null=True, blank=True)
    invoice_no = models.CharField(max_length=100)
    payment_terms = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    invoice_date = models.DateField(null=True, blank=True)
    duedate = models.DateField(null=True, blank=True)
    salesOrder_no = models.CharField(max_length=100, null=True, blank=True)
    exp_ship_date = models.DateField(null=True,blank=True)
    price_list_applied = models.BooleanField(null=True, default=False)
    
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    upi_no = models.CharField(max_length=100, null=True, blank=True)
    bank_acc_no = models.CharField(max_length=100, null=True, blank=True)

    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    paid_off = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)
    
    note = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='invoice',default="default.jpg")
    status =models.CharField(max_length=150,default='Draft')

    def getNumFieldName(self):
        return 'invoice_no'


class Fin_Invoice_Items(models.Model):
    Invoice = models.ForeignKey(Fin_Invoice,on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Fin_Items,on_delete=models.SET_NULL, null=True)
    hsn = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    tax = models.CharField(max_length=100, null=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)


class Fin_Invoice_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)


class Fin_Invoice_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Invoice = models.ForeignKey(Fin_Invoice,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Invoice_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    Invoice = models.ForeignKey(Fin_Invoice,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)


# Vendors




class Fin_Vendor_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Vendor = models.ForeignKey(Fin_Vendors,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Vendor_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    Vendor = models.ForeignKey(Fin_Vendors,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
# End

# -------------Shemeem--------Sales Order-------------------------------

class Fin_CompanyRepeatEvery(models.Model):
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    repeat_every = models.CharField(max_length=100,null=True,blank=True) 
    repeat_type = models.CharField(max_length=100,null=True,blank=True) 
    duration = models.IntegerField(null=True,blank=True)
    days = models.IntegerField(null=True,blank=True)
    
    
class Fin_Recurring_Invoice(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Customer = models.ForeignKey(Fin_Customers, on_delete=models.CASCADE, null=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    entry_type = models.CharField(max_length=20, null=True, blank=True)
    profile_name = models.CharField(max_length=20, null=True, blank=True)
    
    reference_no = models.IntegerField(null=True, blank=True)
    rec_invoice_no = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    salesOrder_no = models.CharField(max_length=100, null=True, blank=True)

    repeat_every = models.ForeignKey(Fin_CompanyRepeatEvery, on_delete = models.SET_NULL,null=True)
    payment_terms = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    price_list_applied = models.BooleanField(null=True, default=False)
    price_list = models.ForeignKey(Fin_Price_List, on_delete = models.SET_NULL,null=True)

    payment_method = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    upi_no = models.CharField(max_length=100, null=True, blank=True)
    bank_acc_no = models.CharField(max_length=100, null=True, blank=True)

    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    paid_off = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)
    
    note = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='rec_invoice',default=None)
    status =models.CharField(max_length=150,default='Draft')

    def getNumFieldName(self):
        return 'rec_invoice_no'
    
class Fin_Sales_Order(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Customer = models.ForeignKey(Fin_Customers, on_delete=models.CASCADE, null=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    reference_no = models.IntegerField(null=True, blank=True)
    sales_order_no = models.CharField(max_length=100)
    payment_terms = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    sales_order_date = models.DateField(null=True, blank=True)
    exp_ship_date = models.DateField(null=True,blank=True)

    payment_method = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    upi_no = models.CharField(max_length=100, null=True, blank=True)
    bank_acc_no = models.CharField(max_length=100, null=True, blank=True)

    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    paid_off = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)

    # converted_from_estimate = models.ForeignKey(Fin_Estimate, on_delete = models.SET_NULL, null = True)
    converted_to_invoice =  models.ForeignKey(Fin_Invoice, on_delete = models.SET_NULL, null = True)
    converted_to_rec_invoice =  models.ForeignKey(Fin_Recurring_Invoice, on_delete = models.SET_NULL, null = True)
    
    note = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='sales_order', null=True, default=None)
    status =models.CharField(max_length=150,default='Draft')

    def getNumFieldName(self):
        return 'sales_order_no'


class Fin_Sales_Order_Items(models.Model):
    SalesOrder = models.ForeignKey(Fin_Sales_Order,on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Fin_Items,on_delete=models.SET_NULL, null=True)
    hsn = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    tax = models.CharField(max_length=100, null=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)


class Fin_Sales_Order_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)


class Fin_Sales_Order_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    SalesOrder = models.ForeignKey(Fin_Sales_Order,on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Sales_Order_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    SalesOrder = models.ForeignKey(Fin_Sales_Order,on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

# Endz

# CREATED BY AISWARYA 
class Fin_Eway_Transportation(models.Model):
    Company = models.ForeignKey('Fin_Company_Details', on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey('Fin_Login_Details', on_delete=models.CASCADE, null=True)
    
    Name = models.CharField(max_length=200, null= True)
    Type = models.CharField(max_length=100, null=True)


class Fin_Ewaybills(models.Model):
    Company = models.ForeignKey('Fin_Company_Details', on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey('Fin_Login_Details', on_delete=models.CASCADE, null=True)

    DocumentType = models.CharField(max_length=200, null=True, verbose_name='Document Type')
    TRANSACTION_TYPES = (
        ('Goods', 'Goods'),
        ('Service', 'Service'),
    )
    TransactionSubtype = models.CharField(max_length=200, null=True, verbose_name='Transaction Subtype')
    TransactionType = models.CharField(max_length=150, choices=TRANSACTION_TYPES, null=True, verbose_name='Transaction Type')
    TransactionHsn = models.IntegerField(null=True, blank=True, default=0, verbose_name='Transaction HSN')

    Ewaybill_ID = models.AutoField(primary_key=True)
    Ewaybill_No = models.CharField(max_length=10)
    BillDate = models.DateField(null=True, blank=True, verbose_name='Bill Date')
    
    Customer = models.ForeignKey('Fin_Customers', on_delete=models.CASCADE, null=True)
    CustomerName = models.CharField(max_length=100, null=True, blank=True, verbose_name='Customer Name')
    CustomerEmail = models.EmailField(null=True, verbose_name='Customer Email')
    Customer_GstType = models.CharField(max_length=100, null=True, verbose_name='GST Type')
    Customer_GstNumber = models.CharField(max_length=100, default='', verbose_name='Customer GST Number')
    Customer_PlaceOfSupply = models.CharField(max_length=100, null=True, blank=True, verbose_name='Customer Place of Supply')
    
    
    BillingAddress = models.TextField(null=True, blank=True, verbose_name='Billing Address')
    
    ReferenceNumber = models.TextField(null=True, blank=True, verbose_name='Reference Number')
    Date = models.DateField(auto_now_add=True, auto_now=False, null=True,verbose_name='Date')
    
    Transportation = models.ForeignKey('Fin_Eway_Transportation', on_delete=models.CASCADE, null=True)
    VehicleNumber = models.CharField(max_length=100, null=True, verbose_name='Vehicle Number')
    Kilometer = models.FloatField(null=True, verbose_name='Kilometer')
    SubTotal = models.FloatField(null=True, blank=True, verbose_name='Subtotal')
    Igst = models.FloatField(null=True, blank=True, verbose_name='IGST')
    Cgst = models.FloatField(null=True, blank=True, verbose_name='CGST')
    Sgst = models.FloatField(null=True, blank=True, verbose_name='SGST')
    TaxAmount = models.FloatField(null=True, blank=True, verbose_name='Tax Amount')
    ShippingCharge = models.FloatField(null=True, blank=True, verbose_name='Shipping Charge')
    Adjustment = models.FloatField(default=0, null=True, blank=True, verbose_name='Adjustment')
    GrandTotal = models.FloatField(null=True, blank=True, verbose_name='Grand Total')
    Note = models.TextField(null=True, verbose_name='Note')
    File = models.FileField(upload_to='purchase/ewbill', default="default.png", verbose_name='File')

    DeliverToDifferentAddress = models.BooleanField(default=False, verbose_name='Deliver to different address')
    DeliveryName = models.CharField(max_length=100, null=True, blank=True, verbose_name='Delivery Name')
    DeliveryAddress = models.TextField(null=True, blank=True, verbose_name='Delivery Address')
    DeliveryPhone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Delivery Phone')
    DeliveryEmail = models.EmailField(null=True, blank=True, verbose_name='Delivery Email')
    DeliveryPlace = models.CharField(max_length=100, null=True, blank=True)

    BILL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Billed', 'Billed'),
    )
    Status = models.CharField(max_length=150, choices=BILL_STATUS_CHOICES, default='Draft', verbose_name='Status')

    def __str__(self):
        return f'{self.Ewaybill_No} - {self.CustomerName}'

    class Meta:
        verbose_name_plural = 'Fin Ewaybills'




class Fin_Eway_Items(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Ewaybills = models.ForeignKey(Fin_Ewaybills,on_delete=models.CASCADE,null=True,blank=True)

    
    Item = models.ForeignKey(Fin_Items,on_delete=models.SET_NULL, null=True)
    hsn = models.BigIntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    tax = models.CharField(max_length=100, null=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)
    

class Fin_Eway_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)


class Fin_Eway_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    
    Ewaybills = models.ForeignKey(Fin_Ewaybills,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)
    
    
# tinto modals STRAT
class Fin_Loan_Term(models.Model):
    duration= models.IntegerField(null=True,blank=True)
    term = models.CharField(max_length=255,null=True,blank=True)
    days = models.IntegerField(null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)

class Fin_Loan(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    employee_name = models.CharField(max_length=255,null=True,blank=True)
    employeeid = models.CharField(max_length=255,null=True,blank=True)
    employee_email = models.EmailField(max_length=255,null=True,blank=True)
    salary = models.IntegerField(null=True,blank=True)
    join_date = models.DateField(null=True,blank=True)
    loan_date = models.DateField(null=True,blank=True)
    loan_amount = models.IntegerField(null=True,blank=True)
    total_loan=models.IntegerField(null=True,blank=True)
    loan_duration = models.ForeignKey(Fin_Loan_Term,on_delete=models.CASCADE,null=True,blank=True)
    expiry_date = models.DateField(null=True,blank=True)
    payment_method = models.CharField(max_length=255,null=True,blank=True)
    cheque_number = models.CharField(max_length=255,null=True,blank=True)
    upi_id = models.CharField(max_length=255,null=True,blank=True)
    
    bank_account = models.CharField(max_length=255,null=True,blank=True)
    monthly_cutting= models.CharField(max_length=255,null=True,blank=True)
    monthly_cutting_percentage = models.IntegerField(null=True,blank=True)
    monthly_cutting_amount = models.IntegerField(null=True,blank=True)
    note = models.CharField(max_length=255,null=True,blank=True)
    attach_file = models.FileField(upload_to='file/',blank=True) 
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    
    status = models.CharField(max_length=255,null=True,blank=True,default='Active')
    balance = models.IntegerField(null=True,blank=True)
    transaction_count = models.IntegerField(null=True,blank=True,default=0)

class Fin_Employee_Loan_History(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    employee_loan = models.ForeignKey(Fin_Loan,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    action = models.CharField(max_length=255,null=True,blank=True)

class Fin_Employee_Additional_Loan(models.Model):
    balance_loan=models.IntegerField(null=True,blank=True)
    new_loan=models.IntegerField(null=True,blank=True)
    total_loan=models.IntegerField(null=True,blank=True)
    payment_method=models.CharField(max_length=255,null=True,blank=True)
    cheque_number = models.CharField(max_length=255,null=True,blank=True)
    upi_id = models.CharField(max_length=255,null=True,blank=True)
    bank_account = models.CharField(max_length=255,null=True,blank=True)
    new_date=models.DateField(null=True,blank=True)

    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    employee_loan = models.ForeignKey(Fin_Loan,on_delete=models.CASCADE,blank=True,null=True)

class Fin_Employee_Loan_Repayment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    principle_amount=models.IntegerField(null=True,blank=True)
    new_loan=models.IntegerField(null=True,blank=True)
    interest_amount=models.IntegerField(null=True,blank=True)
    payment_date = models.DateField(null=True,blank=True)
    payment_method=models.CharField(max_length=255,null=True,blank=True)
    total_amount=models.IntegerField(null=True,blank=True)
    cheque_number = models.CharField(max_length=255,null=True,blank=True)
    upi_id = models.CharField(max_length=255,null=True,blank=True)
    bank_account = models.CharField(max_length=255,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    employee_loan = models.ForeignKey(Fin_Loan,on_delete=models.CASCADE,blank=True,null=True)
    balance = models.IntegerField(null=True,blank=True)

class Fin_Employee_Loan_Transactions(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    employee_loan = models.ForeignKey(Fin_Loan,on_delete=models.CASCADE,blank=True,null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    particulars = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    repayment = models.ForeignKey(Fin_Employee_Loan_Repayment,on_delete=models.CASCADE,null=True,blank=True)
    additional = models.ForeignKey(Fin_Employee_Additional_Loan,on_delete=models.CASCADE,null=True,blank=True)
    balance= models.IntegerField(null=True,blank=True)

class Fin_Employee_Loan_Transactions_History(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    employee_loan = models.ForeignKey(Fin_Loan,on_delete=models.CASCADE,blank=True,null=True)
    repayment = models.ForeignKey(Fin_Employee_Loan_Repayment,on_delete=models.CASCADE,null=True,blank=True)
    additional = models.ForeignKey(Fin_Employee_Additional_Loan,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    action = models.CharField(max_length=255,null=True,blank=True)
    transaction = models.ForeignKey(Fin_Employee_Loan_Transactions,on_delete=models.CASCADE,blank=True,null=True)

class Fin_Employee_loan_comments(models.Model):                                         
    company=models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE)
    logindetails=models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE)
    employee_loan=models.ForeignKey(Fin_Loan,on_delete=models.CASCADE)
    comments = models.CharField(max_length=255,null=True,blank=True)
#End


#---------------------------- Purchase Bill --------------------------------#

class Fin_Purchase_Bill(models.Model):
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    logindetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(Fin_Vendors,  on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Fin_Customers,  on_delete=models.CASCADE, null=True)
    pricelist = models.ForeignKey(Fin_Price_List,  on_delete=models.CASCADE, null=True)
    pay_term = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    bill_no = models.CharField(max_length=100, null=True, blank=True)
    ref_no = models.IntegerField(null=True, blank=True)
    porder_no = models.CharField(max_length=20, null=True, blank=True) #updated shemeem -> Handle Purchase order numbers with char patterns.
    bill_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    pay_type = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    upi_no = models.CharField(max_length=100, null=True, blank=True)
    bank_no = models.CharField(max_length=100, null=True, blank=True)
    ven_psupply = models.CharField(max_length=100, null=True, blank=True)
    cust_psupply = models.CharField(max_length=100, null=True, blank=True)
    subtotal = models.CharField(max_length=100, default=0, null=True)
    igst = models.CharField(max_length=100, default=0, null=True)
    cgst = models.CharField(max_length=100, default=0, null=True)
    sgst = models.CharField(max_length=100, default=0, null=True)
    taxamount = models.CharField(max_length=100, default=0, null=True)
    ship_charge = models.CharField(max_length=100, default=0, null=True)
    adjust = models.CharField(max_length=100, default=0, null=True)
    grandtotal = models.FloatField(default=0, null=True)
    paid = models.CharField(null=True, blank=True, max_length=255)
    balance = models.CharField(null=True, blank=True, max_length=255)
    file = models.FileField(upload_to='purchase_bill')
    description = models.CharField(null=True, blank=True, max_length=255)
    BILL_STATUS = (
        ('Draft','Draft'),
        ('Save','Save'),
    )
    status = models.CharField(max_length=10, choices=BILL_STATUS, default='Draft')

    def getNumFieldName(self):
        return 'bill_no'

class Fin_Purchase_Bill_Item(models.Model):
    pbill = models.ForeignKey(Fin_Purchase_Bill, on_delete=models.CASCADE)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE)
    item = models.ForeignKey(Fin_Items, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, null=True)
    price = models.CharField(max_length=100, default=0, null=True)
    tax = models.CharField(max_length=100, default=0, null=True)
    discount = models.CharField(max_length=100, default=0, null=True)
    total = models.IntegerField(default=0, null=True)

class Fin_Purchase_Bill_Ref_No(models.Model):
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE)
    logindetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    ref_no = models.CharField(max_length=100, default=0, null=True)

class Fin_Purchase_Bill_History(models.Model):
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE)
    logindetails = models.ForeignKey(Fin_Login_Details,  on_delete=models.CASCADE, null=True)
    pbill = models.ForeignKey(Fin_Purchase_Bill, on_delete=models.CASCADE)
    change_date = models.DateField(auto_now_add=True, null=True)
    BILL_ACTION = (
        ('Created','Created'),
        ('Updated','Updated'),
    )
    action = models.CharField(max_length=10, choices=BILL_ACTION)

class Fin_Purchase_Bill_Comment(models.Model):
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE)
    logindetails = models.ForeignKey(Fin_Login_Details,  on_delete=models.CASCADE, null=True)
    pbill = models.ForeignKey(Fin_Purchase_Bill, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100, default=0, null=True)
    
#End


    
    
class TrialPeriod(models.Model):
    company = models.OneToOneField(Fin_Company_Details, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    interested_in_buying = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, null=True)

    def is_active(self):
        return self.end_date >= timezone.now().date()
        
        
# < ------------- Shemeem -------- > Estimates < ------------------------------- >

class Fin_Estimate(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Customer = models.ForeignKey(Fin_Customers, on_delete=models.CASCADE, null=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    reference_no = models.IntegerField(null=True, blank=True)
    estimate_no = models.CharField(max_length=100)
    payment_terms = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    estimate_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True,blank=True)

    payment_method = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    upi_no = models.CharField(max_length=100, null=True, blank=True)
    bank_acc_no = models.CharField(max_length=100, null=True, blank=True)

    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank = True)

    converted_to_sales_order =  models.ForeignKey(Fin_Sales_Order, on_delete = models.SET_NULL, null = True)
    converted_to_invoice =  models.ForeignKey(Fin_Invoice, on_delete = models.SET_NULL, null = True)
    converted_to_rec_invoice =  models.ForeignKey(Fin_Recurring_Invoice, on_delete = models.SET_NULL, null = True)
    
    note = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='estimate', null=True, default=None)
    status =models.CharField(max_length=150,default='Draft')

    def getNumFieldName(self):
        return 'estimate_no'


class Fin_Estimate_Items(models.Model):
    Estimate = models.ForeignKey(Fin_Estimate,on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Fin_Items,on_delete=models.SET_NULL, null=True)
    hsn = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    tax = models.CharField(max_length=100, null=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)


class Fin_Estimate_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)


class Fin_Estimate_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Estimate = models.ForeignKey(Fin_Estimate,on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Estimate_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    Estimate = models.ForeignKey(Fin_Estimate,on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
class Fin_Recurring_Invoice_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)

#End

# < ------------- Shemeem -------- > Manual Journals < ------------------------------- >

class Fin_Manual_Journal(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.IntegerField(null=True, blank=True)
    journal_no = models.CharField(max_length=100)
    journal_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length=255,null=True,blank=True,default='INR-Indian Rupee')

    subtotal_debit = models.FloatField(default=0.0, null=True, blank = True)
    subtotal_credit = models.FloatField(default=0.0, null=True, blank = True)
    total_debit = models.FloatField(default=0.0, null=True, blank = True)
    total_credit = models.FloatField(default=0.0, null=True, blank = True)
    balance_debit = models.FloatField(default=0.0, null=True, blank = True)
    balance_credit = models.FloatField(default=0.0, null=True, blank = True)

    file = models.FileField(upload_to='Journals', null=True, default=None)
    status =models.CharField(max_length=150,default='Draft')

    def getNumFieldName(self):
        return 'journal_no'


class Fin_Manual_Journal_Accounts(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Journal = models.ForeignKey(Fin_Manual_Journal,on_delete=models.CASCADE, null=True)
    Account = models.ForeignKey(Fin_Chart_Of_Account,on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length = 255, null=True, blank=True)
    contact = models.CharField(max_length = 255, null=True, blank=True)
    debit = models.FloatField(default=0.0, null=True, blank=True)
    credit = models.FloatField(default=0.0, null=True, blank=True)


class Fin_Manual_Journal_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)


class Fin_Manual_Journal_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Journal = models.ForeignKey(Fin_Manual_Journal,on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Manual_Journal_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    Journal = models.ForeignKey(Fin_Manual_Journal,on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
#End

class Fin_Eway_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)

    Ewaybill = models.ForeignKey(Fin_Ewaybills,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
# < ------------- Shemeem -------- > Recurring Invoice < ------------------------------- >    
class Fin_Recurring_Invoice_Items(models.Model):
    RecInvoice = models.ForeignKey(Fin_Recurring_Invoice,on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Fin_Items,on_delete=models.SET_NULL, null=True)
    hsn = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    tax = models.CharField(max_length=100, null=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)
    
    
class Fin_Recurring_Invoice_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    RecInvoice = models.ForeignKey(Fin_Recurring_Invoice,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)
    
    
class Fin_Recurring_Invoice_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    RecInvoice = models.ForeignKey(Fin_Recurring_Invoice,on_delete=models.CASCADE,null=True,blank=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
#End

class Fin_Attendances(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)
    reason = models.CharField(max_length = 255)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    company = models.ForeignKey(Fin_Company_Details,on_delete = models.CASCADE)
    login_id = models.ForeignKey(Fin_Login_Details,on_delete = models.CASCADE)

class Fin_Attendance_history(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE)
    login_id = models.ForeignKey(Fin_Login_Details,on_delete = models.CASCADE)
    attendance = models.ForeignKey(Fin_Attendances,on_delete=models.CASCADE)
    date = models.DateField(default = date.today())
    action = models.CharField(max_length = 100)

class Fin_attendance_comment(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE)
    login_id = models.ForeignKey(Fin_Login_Details,on_delete = models.CASCADE)
    attendance = models.ForeignKey(Fin_Attendances,on_delete=models.CASCADE)
    comment = models.CharField(max_length = 100)
    date = models.DateField(default = date.today())
    
# < ------------- Shemeem -------- > Purchase Order < ------------------------------- >

class Fin_Purchase_Order(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)

    Vendor = models.ForeignKey(Fin_Vendors, on_delete=models.CASCADE, null=True)
    vendor_name = models.CharField(max_length=200, null=True, blank=True)
    vendor_email = models.EmailField(max_length=100, null=True, blank=True)
    vendor_address = models.TextField(null=True, blank=True)
    vendor_gst_type = models.CharField(max_length=100, null=True, blank=True)
    vendor_gstin = models.CharField(max_length=100, null=True, blank=True)
    vendor_source_of_supply = models.CharField(max_length=100, null=True, blank=True)

    reference_no = models.IntegerField(null=True, blank=True)
    purchase_order_no = models.CharField(max_length=100)
    payment_terms = models.ForeignKey(Fin_Company_Payment_Terms, on_delete = models.SET_NULL,null=True)
    purchase_order_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True,blank=True)

    payment_method = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    upi_no = models.CharField(max_length=100, null=True, blank=True)
    bank_acc_no = models.CharField(max_length=100, null=True, blank=True)

    Customer = models.ForeignKey(Fin_Customers, on_delete=models.CASCADE, null=True)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    customer_address = models.TextField(null=True, blank=True)
    customer_gst_type = models.CharField(max_length=100, null=True, blank=True)
    customer_gstin = models.CharField(max_length=100, null=True, blank=True)
    customer_place_of_supply = models.CharField(max_length=100, null=True, blank=True)

    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    paid_off = models.FloatField(default=0.0, null=True, blank=True)
    balance = models.FloatField(default=0.0, null=True, blank=True)

    converted_to_bill =  models.ForeignKey(Fin_Purchase_Bill, on_delete = models.SET_NULL, null = True)
    # converted_to_rec_bill =  models.ForeignKey(Fin_Recurring_Invoice, on_delete = models.SET_NULL, null = True)
    
    note = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='purchase_order', null=True, default=None)
    status =models.CharField(max_length=150,default='Draft')

    def getNumFieldName(self):
        return 'purchase_order_no'


class Fin_Purchase_Order_Items(models.Model):
    PurchaseOrder = models.ForeignKey(Fin_Purchase_Order,on_delete=models.CASCADE, null=True)
    Item = models.ForeignKey(Fin_Items,on_delete=models.SET_NULL, null=True)
    hsn = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    total = models.FloatField(default=0.0, null=True, blank=True)
    tax = models.CharField(max_length=100, null=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)


class Fin_Purchase_Order_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)


class Fin_Purchase_Order_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    PurchaseOrder = models.ForeignKey(Fin_Purchase_Order,on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Purchase_Order_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    PurchaseOrder = models.ForeignKey(Fin_Purchase_Order,on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

# End

class Stock_Adjustment(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    mode_of_adjustment = models.CharField(max_length=255,null=True,blank=True)
    reference_no = models.CharField(max_length=255,null=True,blank=True)
    adjusting_date = models.DateField(null=True,blank=True)
    account = models.CharField(max_length=255,null=True,blank=True)
    reason = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    attach_file = models.FileField(upload_to='file/stock_adj/',blank=True)
    status=models.CharField(max_length=255,null=True,blank=True)
    
    
    

class Stock_Adjustment_Items(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    item= models.ForeignKey(Fin_Items,on_delete=models.CASCADE,null=True,blank=True)
    stock_adjustment=models.ForeignKey(Stock_Adjustment,on_delete=models.CASCADE,null=True,blank=True)
    quantity_avail = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    quantity_inhand = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    quantity_adj = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    current_val = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    changed_val = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    adjusted_val = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    type=models.CharField(max_length=255,null=True,blank=True,default='None')

class Stock_Adjustment_History(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    item= models.ForeignKey(Fin_Items,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    action = models.CharField(max_length=255,null=True,blank=True)
    stock_adjustment=models.ForeignKey(Stock_Adjustment,on_delete=models.CASCADE,null=True,blank=True)

class Stock_Adjustment_Comment(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    stock_adjustment=models.ForeignKey(Stock_Adjustment,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=500,default='')

class Stock_Reason(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    reason = models.CharField(max_length=500)
  
class Stock_Adjustment_RefNo(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    reference_no = models.BigIntegerField(null = False, blank=False)
    
    
class Fin_Delivery_Challan(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Customer = models.ForeignKey(Fin_Customers, on_delete=models.CASCADE, null=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    challan_date = models.DateField(null=True, blank=True)
    reference_no = models.IntegerField(null=True, blank=True)
    challan_no = models.CharField(max_length=100, blank=True)
    challan_type = models.CharField(max_length=100, blank=True)

    description = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='file/',blank=True) 
    
    
    

    

    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    paid_number = models.IntegerField(default=0, null=True)
    balance = models.FloatField(default=0.0, null=True, blank = True)

    
    converted_to_invoice =  models.ForeignKey(Fin_Invoice, on_delete = models.SET_NULL, null = True)
    converted_to_recurring_invoice =  models.ForeignKey(Fin_Recurring_Invoice, on_delete = models.SET_NULL, null = True)
    
    note = models.TextField(null=True, blank=True)
    
    status =models.CharField(max_length=150,default='Draft')


class Fin_Delivery_Challan_Items(models.Model):
    items = models.ForeignKey(Fin_Items, on_delete=models.CASCADE, null=True)
    hsn = models.CharField( max_length=150,null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    delivery_challan = models.ForeignKey(Fin_Delivery_Challan, on_delete=models.CASCADE, null=True)
    
    tax_rate = models.FloatField(default=0, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)

    discount = models.FloatField(default=0, null=True)
    total = models.FloatField(default=0, null=True, blank = True)

class Fin_Delivery_Challan_Reference(models.Model):
    
    reference_number = models.CharField( max_length=150,null=True, blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    

class Fin_Delivery_Challan_History(models.Model):
    
    
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    delivery_challan = models.ForeignKey(Fin_Delivery_Challan, on_delete=models.CASCADE, null=True)
    date = models.DateField( null=True, blank = True)
    action = models.CharField( max_length=150,default='Created')

class Fin_Delivery_Challan_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    delivery_challan = models.ForeignKey(Fin_Delivery_Challan,on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
    
# < ------------- Shemeem -------- > Expense < ------------------------------- >

class Fin_Expense(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)

    reference_no = models.IntegerField(null=True, blank=True)
    expense_no = models.CharField(max_length=100)
    expense_date = models.DateField(null=True, blank=True)
    Account = models.ForeignKey(Fin_Chart_Of_Account, on_delete=models.SET_NULL, null=True)
    expense_account = models.CharField(max_length=150, null=True, blank=True)
    expense_type = models.CharField(max_length=150, null=True, blank=True)
    hsn_number = models.CharField(max_length=50, null=True, blank=True)
    sac_number = models.CharField(max_length=50, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    tax_rate = models.CharField(max_length=50, null=True, blank=True)

    payment_method = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    upi_no = models.CharField(max_length=100, null=True, blank=True)
    bank_acc_no = models.CharField(max_length=100, null=True, blank=True)

    Vendor = models.ForeignKey(Fin_Vendors, on_delete=models.CASCADE, null=True)
    vendor_name = models.CharField(max_length=200, null=True, blank=True)
    vendor_email = models.EmailField(max_length=100, null=True, blank=True)
    vendor_address = models.TextField(null=True, blank=True)
    vendor_gst_type = models.CharField(max_length=100, null=True, blank=True)
    vendor_gstin = models.CharField(max_length=100, null=True, blank=True)
    vendor_source_of_supply = models.CharField(max_length=100, null=True, blank=True)

    Customer = models.ForeignKey(Fin_Customers, on_delete=models.CASCADE, null=True)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    customer_address = models.TextField(null=True, blank=True)
    customer_gst_type = models.CharField(max_length=100, null=True, blank=True)
    customer_gstin = models.CharField(max_length=100, null=True, blank=True)
    customer_place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    
    note = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='expense', null=True, default=None)
    status =models.CharField(max_length=150,default='Draft')

    def getNumFieldName(self):
        return 'expense_no'


class Fin_Expense_Reference(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    reference_no = models.BigIntegerField(null = False, blank=False)


class Fin_Expense_History(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    Expense = models.ForeignKey(Fin_Expense,on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited'),
    ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_Expense_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    Expense = models.ForeignKey(Fin_Expense,on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500,null=True,blank=True)

# End

class loan_account(models.Model):
    account_name=models.TextField(max_length=100)
    account_number=models.TextField(max_length=100)
    lenderbank=models.TextField(max_length=100)
    recieced_bank=models.TextField(max_length=100)
    intrest=models.TextField(max_length=100,null=True,blank=True)
    term=models.TextField(max_length=100)
    loan_amount=models.TextField(max_length=100)
    processing=models.TextField(max_length=100,null=True,blank=True)
    paid=models.TextField(max_length=100,null=True,blank=True)
    status=models.TextField(max_length=100)
    desc=models.TextField(max_length=100,null=True,blank=True)
    balance=models.IntegerField(default=0)    
    date=models.DateField(blank=True,null=True)
    recieved_amount=models.IntegerField(default=0)   
    paid_cheque = models.TextField(max_length=100,null=True,blank=True)
    paid_upi = models.TextField(max_length=100,null=True,blank=True)
    paid_bank_acc_number = models.TextField(max_length=100,null=True,blank=True)
    recieved_cheque = models.TextField(max_length=100,null=True,blank=True)
    recieved_upi = models.TextField(max_length=100,null=True,blank=True)
    bank_acc_number = models.TextField(max_length=100,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    attach_file = models.FileField(upload_to='file/',blank=True)

class loan_transaction(models.Model):
    bank_type=models.TextField(max_length=100)
    from_trans=models.TextField(max_length=100)
    to_trans=models.TextField(max_length=100)
    loan=models.ForeignKey(loan_account, on_delete=models.CASCADE ,null=True,blank=True)
    loan_amount=models.IntegerField(default=0,blank=True,null=True)
    loan_desc=models.TextField(blank=True,null=True)
    loan_date=models.DateField(blank=True,null=True)
    loan_intrest=models.TextField(max_length=100,default=0,blank=True,null=True)
    balance=models.IntegerField(default=0)   
    type=models.TextField(max_length=100)
    total = models.IntegerField(default=0)
    recieved_bank = models.TextField(max_length=100,null=True,blank=True)
    recieved_cheque = models.TextField(max_length=100,null=True,blank=True)
    recieved_upi = models.TextField(max_length=100,null=True,blank=True)
    bank_acc_number = models.TextField(max_length=100,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
   


class Fin_loanAccountHistory(models.Model):
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    loan_ac = models.ForeignKey(loan_account, on_delete=models.CASCADE)


    date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    action_choices = [
        ('Created', 'Created'),
        ('Edited', 'Edited')
        ]
    action = models.CharField(max_length=20, null=True, blank = True, choices=action_choices)


class Fin_LoanTransactionHistory(models.Model): 

    login_details = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE,null=True,blank=True)
    transaction = models.ForeignKey(loan_transaction, on_delete=models.CASCADE,null=True,blank=True)
    loan_ac = models.ForeignKey(loan_account, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    action = models.CharField(max_length=255,null=True,blank=True)
    
#START HARIKRISHNAN

class Fin_Recurring_Bills(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    vendor = models.ForeignKey(Fin_Vendors,on_delete=models.CASCADE,null=True,blank=True)
    recurring_bill_number = models.CharField(max_length=255,null=True,blank=True)
    profile_name = models.CharField(max_length=255,null=True,blank=True)
    reference_number = models.IntegerField(null=True,blank=True)
    bill_number = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    company_payment_terms = models.ForeignKey(Fin_Company_Payment_Terms,on_delete=models.CASCADE,null=True,blank=True)
    expected_shipment_date = models.DateField(null=True,blank=True)
    purchase_order_number = models.CharField(max_length=255,null=True,blank=True)
    payment_method = models.CharField(max_length=255,null=True,blank=True)
    cheque_number = models.CharField(max_length=255,null=True,blank=True)
    upi_id = models.CharField(max_length=255,null=True,blank=True)
    bank_account = models.CharField(max_length=255,null=True,blank=True)
    customer = models.ForeignKey(Fin_Customers,on_delete=models.CASCADE,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    document = models.FileField(null=True,blank=True,upload_to='document')
    sub_total = models.FloatField(null=True,blank=True)
    cgst = models.FloatField(null=True,blank=True)
    sgst = models.FloatField(null=True,blank=True)
    taxAmount_igst = models.FloatField(null=True,blank=True)
    shipping_charge = models.FloatField(null=True,blank=True)
    adjustment = models.FloatField(null=True,blank=True)
    grand_total = models.FloatField(null=True,blank=True)
    advanceAmount_paid = models.FloatField(null=True,blank=True)
    balance = models.FloatField(null=True,blank=True)
    status = models.CharField(max_length=255,null=True,blank=True)
    repeat_every = models.ForeignKey(Fin_CompanyRepeatEvery,on_delete=models.CASCADE,null=True,blank=True)
    attachment = models.FileField(null=True,blank=True,upload_to='recurring_bill_attachments')
    pricelist = models.ForeignKey(Fin_Price_List,on_delete=models.CASCADE,null=True,blank=True)

class Fin_Recurring_Bill_Items(models.Model):
    items = models.ForeignKey(Fin_Items,on_delete=models.CASCADE,null=True,blank=True)
    hsn = models.CharField(max_length=255,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    tax_rate = models.IntegerField(null=True,blank=True)
    discount = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    recurring_bill = models.ForeignKey(Fin_Recurring_Bills,on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)

#END

# Debit note models strat

class Fin_Debit_Note(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True,blank=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True,blank=True)
    Vendor = models.ForeignKey(Fin_Vendors, on_delete=models.CASCADE, null=True,blank=True)
    vendor_email = models.EmailField(max_length=100, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    gst_type = models.CharField(max_length=100, null=True, blank=True)
    gstin = models.CharField(max_length=100, null=True, blank=True)
    place_of_supply = models.CharField(max_length=100, null=True, blank=True)
    debit_note_number = models.CharField(max_length=100, blank=True)
    debit_note_date = models.DateField(null=True, blank=True)
    reference_number = models.IntegerField(null=True, blank=True)
    bill_number = models.CharField(max_length=100, blank=True)

    
    bill_type = models.CharField(max_length=100, blank=True)
    payment_type = models.CharField(max_length=100, blank=True)
    cheque_number = models.CharField(max_length=100, blank=True,null=True,)
    upi_id = models.CharField(max_length=100, blank=True,null=True,)
    bank_account = models.CharField(max_length=100, blank=True,null=True,)

    description = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='file/',blank=True) 
    

    subtotal = models.IntegerField(default=0, null=True)
    igst = models.FloatField(default=0.0, null=True, blank=True)
    cgst = models.FloatField(default=0.0, null=True, blank=True)
    sgst = models.FloatField(default=0.0, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    tax_amount = models.FloatField(default=0.0, null=True, blank=True)
    adjustment = models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge = models.FloatField(default=0.0, null=True, blank=True)
    grandtotal = models.FloatField(default=0.0, null=True, blank=True)
    paid = models.IntegerField(default=0, null=True)
    balance = models.FloatField(default=0.0, null=True, blank = True)

    
  
    note = models.TextField(null=True, blank=True)
    
    status =models.CharField(max_length=150,default='Draft')


class Fin_Debit_Note_Items(models.Model):
    items = models.ForeignKey(Fin_Items, on_delete=models.CASCADE, null=True)
    hsn = models.CharField( max_length=150,null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    debit_note = models.ForeignKey(Fin_Debit_Note, on_delete=models.CASCADE, null=True)
    
    tax_rate = models.FloatField(default=0, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)

    discount = models.FloatField(default=0, null=True)
    total = models.FloatField(default=0, null=True, blank = True)


class Fin_Debite_Note_Reference(models.Model):
    
    reference_number = models.CharField( max_length=150,null=True, blank=True)
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    debit_note = models.ForeignKey(Fin_Debit_Note, on_delete=models.CASCADE, null=True)
  

class Fin_Debite_Note_History(models.Model):
    
    
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    LoginDetails = models.ForeignKey(Fin_Login_Details, on_delete=models.CASCADE, null=True)
    debit_note = models.ForeignKey(Fin_Debit_Note, on_delete=models.CASCADE, null=True)
    date = models.DateField( null=True, blank = True)
    action = models.CharField( max_length=150,default='Created')

class Fin_Debite_Note_Comments(models.Model):
    Company = models.ForeignKey(Fin_Company_Details, on_delete=models.CASCADE, null=True)
    debit_note = models.ForeignKey(Fin_Debit_Note, on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=500,null=True,blank=True)
    
# Debit note models end

class Fin_Recurring_Bill_Reference(models.Model):
    reference_number = models.IntegerField(null=True,blank=True)
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)

class Fin_Recurring_Bill_History(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    recurring_bill = models.ForeignKey(Fin_Recurring_Bills,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    action = models.CharField(max_length=255,null=True,blank=True)

class Fin_Recurring_Bill_Comments(models.Model):
    company = models.ForeignKey(Fin_Company_Details,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(Fin_Login_Details,on_delete=models.CASCADE,null=True,blank=True)
    recurring_bill = models.ForeignKey(Fin_Recurring_Bills,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=255,null=True,blank=True)