# from itertools import count
from ast import If
from msilib.schema import Media
import random
from unicodedata import name
from urllib import request
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# File Storage
from django.core.files.storage import FileSystemStorage

from akash.settings import STATIC_URL,EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives,send_mass_mail,EmailMessage    
from django.template.loader import render_to_string
import collections
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

gname=" "
sr_no = 1
class uploadfile:
    fileurl=" "
    status=False
    filename=" "

    def set_file_name(self,name):
        self.filename=name

    def get_file_name(self):
        return self.filename

    def set_file_url(self,url):
        self.fileurl=url

    def get_file_url(self):
        return self.fileurl

    def set_status(self,value):
        self.status=value

    def get_status(self):
        return self.status

class eList:
    list_gender=" "
    list_email=" "
    def setemail(self,email):
        self.list_email=email

    def get_email(self):
        return self.list_email

    def setgender(self,gender):
        self.list_gender=gender

    def get_gender(self):
        return  self.list_gender
 
        
#Admin class
class admin_detail:
    username=" "
    authenticated=False
    processing=False
    def set_processing(self,processing):
        self.processing=processing

    def get_processing(self):
        return self.processing

    def set_username(self,name):
        self.username=name

    def get_username(self):
        return self.username

    def set_aut(self,authenticated):
        self.authenticated=authenticated

    def get_aut(self):
        return self.authenticated


    # def get_count(self):
    #     return self.url

class segment_details:
    cleaned=" "
    segments=[]
    s_males=[]
    s_females=[]
    age_21_plus=[]
    age_21_minus=[]
    email_dict=collections.defaultdict(list)
    
    def get_clean(self):
        return self.clean

    def set_clean(self,clean):
        self.clean=clean
    # email_dict[0]=[1,2]
    
    def set_emails(self,emails,itr):
        sr_no =itr
        filesr = str(sr_no)
        str1="email"+filesr
        self.email_dict[str1]=emails
    def get_emails(self,email):
        return self.email_dict[email]
        # print(emailt)
        # print(self.email_dict[])
    def set_segments_url(self,url):
       self.segments.append(url)

    def get_segments_url(self):
       return self.segments

    def set_male_data(self,count):
       self.s_males.append(count)
    def set_female_data(self,count1):
        self.s_females.append(count1)

    def male_data(self):
       return self.s_males
    def female_data(self):
        return self.s_females
    
    def set_age(self,age_plus,age_minus):
        self.age_21_plus.append(age_plus)
        self.age_21_minus.append(age_minus)

    def get_age_21_plus(self):
        return self.age_21_plus
       
    def get_age_21_minus(self):
        return self.age_21_minus




# Class Creation
listofemails= eList()
seg=segment_details()
Admin=admin_detail()
file1=uploadfile()

def test1():
    seg.set_segurl_name(listofemails.get_email[0])
    

    
# Landing Page
def index(request):
    return render(request,'index.html')

# Login Page
def home(request):
    return render(request,'home.html')



# Login Funcation
def check(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('pass')
        Admin.set_username(username)
    user = authenticate(request, username=username, password=password)
    Admin.set_aut(True)

    if user is not None:
        login(request,user)
        return render(request,'dashboard.html',{'name':username,'nameset':True})
    else:
        login_Fail = True 
        Admin.set_aut(False)
        return render(request,'home.html',{'login_Fail':login_Fail})

# Logout Function   
def logoutUser(request):    
    logout(request)
    file1.set_status(False)
    name=Admin.get_username()
    Admin.set_aut(False)
    Admin.set_processing(False)
    return render(request,'home.html',{'name':name,'logout':True})

name=Admin.get_username()

# Redirect
def aut_user(request):
    name=Admin.get_username()
    print(file1.get_status())
    print(Admin.get_processing())
    print(Admin.get_aut())
    print(seg.get_segments_url())
    if(Admin.get_aut() and file1.get_status() and Admin.get_processing()):
        return render(request,'dashboard.html',{'nameset':True,'name':name,'cleansucess':True,'finalfile':seg.get_clean()})
    elif(Admin.get_aut() and file1.get_status()):
        return render(request,'dashboard.html',{'filesucess':file1.get_status(),'name':name,'nameset':True,'url':file1.get_file_url(),'filename':file1.get_file_name})
    elif(Admin.get_aut()):
        return render(request,'dashboard.html',{'name':name,'nameset':True})
    else:
         return render(request,'home.html')

    
# File Uploading
def upload(request):
    csv_list=['CustomerID', 'Gender', 'Age', 'Annual Income (k)', 'Spending Score (1-100)', 'Email']
    name=Admin.get_username()
    if(file1.get_status()==False):
        if request.method== "POST":
            uploaded_file = request.FILES['fileupload']


            # check contents
            # c_file=pd.read_csv(uploaded_file)
            print(file1.get_status())
            x = uploaded_file.name.split(".")
            if (x[len(x)-1])=="csv":
                fs= FileSystemStorage()
                c_file=pd.read_csv(uploaded_file)
                column_names=list(c_file.columns)
                if column_names==csv_list:
                    filename=fs.save(uploaded_file.name,uploaded_file)
                    filestatus =True
                    file1.set_file_name=filename
                    url =fs.url(filename)
                    file1.set_file_url(url)
                    file1.set_status(filestatus)
                    print(file1.get_status())
                    fileerror=False
                    return render(request,'dashboard.html',{'filesucess':file1.get_status(),'name':name,'nameset':True,'url':file1.get_file_url(),'filename':file1.get_file_name})
                else:
                    fileerror = True
            else:
                fileerror = True

            if fileerror==True :   
                return render(request,'dashboard.html',{'fileerror':fileerror,'name':name,'nameset':True})
                
    # elif(file1.get_status()==True):
    #     return render(request,'dashboard.html',{'filesucess':file1.get_status(),'name':name,'nameset':True,'url':file1.get_file_url(),'filename':file1.get_file_name})



def directdash(request):
    print(file1.get_status())
    if(file1.get_status()==True):
        return render(request,'dashboard.html',{'filesucess':file1.get_status(),'name':name,'nameset':True,'filename':file1.get_file_name})

# Clean Data Function
def cleandata(request):
    sr_no =1
    filesr = str(sr_no)
    name=Admin.get_username()
    if request.method== "POST":
         url = request.POST.get('fileId')
         df = pd.read_csv("/django/akash"+url)
         df.drop('CustomerID',axis=1,inplace=True)
         df['Gender'].replace(['Female','Male'], [0,1],inplace=True)
         column_median = df.median()
         df = df.fillna(column_median)
         df.dropna(subset=['Email'], inplace = True)
         df.drop_duplicates(subset=["Email"],inplace=True)
         df = df.loc[(df["Spending Score (1-100)"] >20) &(df["Annual Income (k)"] >20) ]
         df.to_csv("/django/akash/media/finalwork"+ filesr +".csv")
         fs= FileSystemStorage()
         finalurl="finalwork" + filesr + ".csv"
         url =fs.url(finalurl)
         seg.set_clean(url)
         sr_no = sr_no +1 

         segmented_url=segmentdata(url)
         Admin.set_processing(True)
        #  seg_name=seg.get_seg_name()
        #  seg_size=np.count_nonzero(segmented_url)
        #  print(len(segmented_url))  
    return render(request,'dashboard.html',{'nameset':True,'name':name,'cleansucess':True,'finalfile':url,'url':segmented_url})

def mail_page(request):
    if(Admin.get_processing()==True):
        name=Admin.get_username()
        if request.method== "POST":
            url = request.POST.get('fileId')
            gender=" "
            print("url of mail page is")
            print(url)
            df = pd.read_csv( "/django/akash"+url)
            annual_income=df["Annual Income (k)"].values
            spend=df["Spending Score (1-100)"].values
            emails=df["Email"].values
            annual=df["Annual Income (k)"].value_counts()
            print("Annual")
            print(annual)
            ageminus =len(df[df.Age<=21])
            ageplus =len(df[df.Age>21])
            total =len(df)
            gender_male= 1 in df["Gender"].values
            gender_female=0 in df["Gender"].values
            if(gender_male==True):
                if gender_female==True:
                    gender=df["Gender"].value_counts()
                    male=gender[0]
                    female=gender[1]
                elif gender_female==False:
                    gender=df["Gender"].value_counts()
                    male=gender.values
                    male=male[0]
                    female=0
                    # print("jbcxbv")
                    # print(male)
                    # print(female)
            else:
                male=0
                if gender_female==False:
                    female=0
                elif gender_female==True:
                    gender=df["Gender"].value_counts()
                    female=gender.values
                    female=female[0]
                    

            print(total)
            print(ageplus)
            print(ageminus)
            print("AHJS")
            print(annual_income)
            print(spend)
            print(emails)
            print(gender)
            print("Till")
            #  annual_income=df["Annual Income (k)"].values
            #  spending_score=df["Spending Score (1-100)"].values
            listofemails.setemail(emails)
            # print(gender)
    return render(request,'mailing.html',{'name':name,'nameset':True,'emails':emails,'male':male,'female':female,'age18plus': ageminus,'age18minus': ageplus,'annual':annual_income,'spend':spend})
    # return render(request,'mailing.html')

def send_email(request):
        # print("Send mail:" , listofemails.get_email())
         generate_rand()

         if request.method=="POST":
            subject_msg = "Xpress Mail offer"
            text_content_msg =request.POST.get('message')
            subject, from_email = subject_msg, EMAIL_HOST_USER
            # For simple text
            # message=(subject,text_content_msg,from_email,list(listofemails.get_email()))
            # send_mass_mail([message],fail_silently=False)

            # for Html content
            html_content1 = 'offer.html'
            html_content=render_to_string(html_content1)
            # print("Html content is ")
            # print(html_content)
            message1=EmailMessage(subject,html_content,from_email,list(listofemails.get_email()))  
            message1.content_subtype = "html"  # Main content is now text/html
            message1.send()
            return render(request,'dashboard.html',{'nameset':True,'name':name,'cleansucess':True,'finalfile':seg.get_clean(),'url':seg.get_segments_url(),'sucess':True})
           

            # return render(request,'mailing.html',{'name':name,'nameset':True,'sucess':True})

def generate_rand():
    num=str(random.randint(1,10))
    # FIRST GROUP
    file_name = "templates/offer.txt"
    # completeName = os.path.join(save_path, file_name)
    file1 = open(file_name, "w")
    file1.write(num)
    file1.close()
            
        
def offer(request):
        return render(request,"offer.html")

def segmentdata(fileurl):
    df2=pd.read_csv("/django/akash"+fileurl)
    print(df2.shape)
    df1=df2[["Gender","Age","Annual Income (k)","Spending Score (1-100)","Email"]]
    X=df1[["Annual Income (k)","Spending Score (1-100)"]]
    #The input data
    X.head()
    wcss=[]

    # for i in range(1,11):
    #     km=KMeans(n_clusters=i)
    #     km.fit(X)
    #     wcss.append(km.inertia_)
    #Taking 5 clusters
    km1=KMeans(n_clusters=5)
    #Fitting the input data
    km1.fit(X)
    #predicting the labels of the input data
    y=km1.predict(X)
    #adding the labels to a column named label
    df1["label"] = y
    #The new dataframe with the clustering done
    df1.head(n=1000)
    # empty array

    url=np.empty(5,object)
    # count=0
    for i in range(0,5):
        fi=str(i)
        cust = df1[df1.label == i]
        
        # emails=df1.Email[df1.label == i]
        emails=cust["Email"].values
        seg.set_emails(emails,i)

        male=len(df1[df1.Gender==1][df1.label == i])
        female=len(df1[df1.Gender==0][df1.label == i])
        age_18_plus=len(df1[df1.Age>=21][df1.label == i])
        age_18_minus=len(df1[df1.Age<21][df1.label == i])
        cust.to_csv("/django/akash/media/segmented/segment"+ fi +".csv")
        fs= FileSystemStorage()
        finalurl="segmented/segment" + fi + ".csv"
        url[i] =fs.url(finalurl)
        print(url[i])
        seg.set_segments_url(url[i])   
       
        # df4 = pd.read_csv("/django/akash"+url[i])
        # emails=df4["Email"].values
        # males=len(df4[df4.Gender==1])
        # females=len(df4[df4.Gender==0])

        # print(i)
        # print("Emails")
        # print("Males:")
        # print(male)
        # print("Females:")
        # print(females)
        seg.set_male_data(male)
        seg.set_female_data(female)
        seg.set_age(age_18_plus,age_18_minus)
        print("21+")
        print(seg.get_age_21_plus())
        print("21-")
        print(seg.get_age_21_minus())
        
    print(seg.get_segments_url())   
    return url
        
def analytics(request):
    males=seg.male_data()
    females=seg.female_data()
    name=Admin.get_username()
    plusage=seg.get_age_21_plus()
    minusage=seg.get_age_21_minus()
    print("Analysis")
    print(plusage)
    print(females)
    
    
    return render(request,"analytics.html",{'name':name,'nameset':True,'segmented':True,'males':males,'females':females,'ageplus':plusage,'ageminus':minusage})


def segment_email(request):
         name=Admin.get_username()
         if request.method=="POST":
            subject_msg = "Xpress Mail offer"
            text_content_msg =request.POST.get('message')
            segment=request.POST.get('segment')
            email=" "
            print(segment)
            seg_generate_rand(segment)
            if(segment=="segment1"):
                email=seg.get_emails("email0")
                print(email)
            elif(segment=="segment2"):
                email=seg.get_emails("email1")
                print(email)
                
            elif(segment=="segment3"):
                email=seg.get_emails("email2")
                print(email)
                
            elif(segment=="segment4"):
                email=seg.get_emails("email3")
                print(email)
                 
            else:
                email=seg.get_emails("email4")
                print(email)
                
            subject, from_email = subject_msg, EMAIL_HOST_USER
            # For simple text
            message=(subject,text_content_msg,from_email,list(email))
            # send_mass_mail([message],fail_silently=False)

            # for Html content
            html_content1 = 'offer.html'
            html_content=render_to_string(html_content1)
            # print("Html content is ")
            # print(html_content)
            message1=EmailMessage(subject,html_content,from_email,list(email))  
            message1.content_subtype = "html"  # Main content is now text/html
            message1.send()
            # return HttpResponse('Success',{'mail':'Sucess'})
            # return render(request ,"sucess.html",{'success':True})
            return render(request,'dashboard.html',{'nameset':True,'name':name,'cleansucess':True,'finalfile':seg.get_clean(),'url':seg.get_segments_url(),'sucess':True})


def seg_generate_rand(segment_name):
    print(segment_name)
    if(segment_name=="segment1"):
        num=str(random.randint(10,20))
    elif(segment_name=="segment2"):
        num=str(random.randint(20,40))
    elif(segment_name=="segment3"):
        num=str(random.randint(50,70))
    elif(segment_name=="segment4"):
        num=str(random.randint(70,80))
    else:
        num=str(random.randint(80,90))
    
    # FIRST GROUP
    file_name = "templates/offer.txt"
    # completeName = os.path.join(save_path, file_name)
    file1 = open(file_name, "w")
    file1.write(num)
    file1.close()

    # Test