import django

from django.db import models
from django.test import TestCase,SimpleTestCase,Client,tag
from django.urls import resolve
from .models import *
from .views import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group 
import requests



'''
class ViewTest(TestCase):
    def test_login(self):
        self.client.login(username='areen', password='123123')
        response = self.client.get('/Login/')
        self.assertContains(response, 'login', 4, 200)
class medelsTest(TestCase):
    def test_create_message(self):
        message1=Updates.objects.create(message="title for messs",senderID="areen")
        message1.save()
        self.assertEqual(str(message1),"title for messs")

'''
class LogoutTest(TestCase):
   def testLogout(self):
       user=User.objects.create(username='aren', password='123123')
       self.client.login(username='username',password='password')
       response = self.client.get(('logoutUser'), follow=True)
       self.assert_(response.status_code, 200)

'''
class ManageUsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', email='email',
                                        last_name='last_name',
                                        first_name='first_name')
        self.user.set_password('password')
        self.user.save() '''


class PassengerHomePageTests(TestCase): 

    def test_PassengerHomePage(self):
        c = Client()
        response = c.get(('PassengerHomePage'))
        self.assert_(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'PassengerHomePage.html')

    def test_DriverNotification(self):
        c = Client()
        response = c.get(('DriverNotification'))
        self.assert_(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'DriverNotification.html')  

    def test_AddNewDriver(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver.html')  


    def test_AddNewDriver_sendMail(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/SendMail.html') 

    def test_AddNewDriver_DriverDetails(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/DriverDetails.html')   

    def test_AddNewDriver_deluser(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/deluser.html') 

    def test_AddNewDriver_Request(self):
       c = Client()
       response = c.get(('AddNewDriver'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AddNewDriver/Request.html')          


    def test_PageHome(self):
       c = Client()
       response = c.get(('index'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'index/signup.html') 

    def test_PageHome_login(self):
       c = Client()
       response = c.get(('index'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'index/login.html')        

    def test_PageHome_DriverSignup(self):
       c = Client()
       response = c.get(('index'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'index/DriverSignup.html')

    def test_AdminHomePage(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage.html')  

    def test_AdminHomePage_SendMail(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/SendMail.html')   

    def test_AdminHomePage_AddNewDriver(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/AddNewDriver.html')  

    def test_AdminHomePage_DriverDetails(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/DriverDetails.html')  

    def test_AdminHomePage_deluser(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/deluser.html')

    def test_AdminHomePage_Request(self):
       c = Client()
       response = c.get(('AdminHomePage'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'AdminHomePage/Request.html')

    def test_deluser(self):
       c = Client()
       response = c.get(('deluser'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'deluser.html') 

    def test_DriverDetails(self):
       c = Client()
       response = c.get(('DriverDetails'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'DriverDetails.html')

    def test_DriverFile(self):
       c = Client()
       response = c.get(('DriverFile'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'DriverFile.html')

    def test_DriverHomePage(self):
       c = Client()
       response = c.get(('DriverHomePage'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'DriverHomePage.html') 

    def test_DriverNotification(self):
       c = Client()
       response = c.get(('DriverNotification'))
       self.assert_(response.status_code, 200)
       self.assertTemplateNotUsed(response, 'DriverNotification.html')
       
    def test_DriverSignup(self):
      c = Client()
      response = c.get(('DriverSignup'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'DriverSignup.html') 

    def test_DriverSignup_DriverFile(self):
      c = Client()
      response = c.get(('DriverSignup'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'DriverSignup/DriverFile.html')  

    def test_login1(self):
      c = Client()
      response = c.get(('login'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'login.html')

    def test_login_AdminHomePade(self):
      c = Client()
      response = c.get(('login'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'login/AdminHomePade.html')

    def test_login_PassengerHomePage(self):
      c = Client()
      response = c.get(('login'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'login/PassengerHomePage.html')

    def test_login_DriverHomePage(self):
      c = Client()
      response = c.get(('login'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'login/DriverHomePage.html')

    def test_NotificationByDriver(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'NotificationByDriver.html')

    def test_PassengerNotification(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'NotificationByDriver/PassengerNotification.html')   


    def test_PassengerNotification_logout(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'NotificationByDriver/login.html')

    def test_PassengerNotification_home_pagre(self):
      c = Client()
      response = c.get(('NotificationByDriver'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'NotificationByDriver/PassengerHomePage.html') 

    def test_SendMail(self):
     c = Client()
     response = c.get(('SendMail'))
     self.assert_(response.status_code, 200)
     self.assertTemplateNotUsed(response, 'SendMail.html')



    def test_Signup(self):
      c = Client()
      response = c.get(('signup'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'signup.html')

    '''
    def test_Requset(self):
      c = Client()
      response = c.get(('Requset'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'Requset.html')
    '''
    
    def test_PassengerNotification1(self):
      c = Client()
      response = c.get(('PassengerNotification'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'PassengerNotification.html')  
    def test_PassengerProfile(self):
      c = Client()
      response = c.get(('PassengerProfile'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'PassengerProfile.html')
    

####################################integration-test########################
@tag('integration_test')
class testPassengerHomePage_integration_test_class(TestCase): 

   def testRegisterStudentAndLogin_new(self):
        #User.objects.create(username='aa', password='aa'
       data = {'username': 'a12', 'password': 'a12'}
       data_login=User.objects.create () #+ User.objects.create = ({'name':'Areen'})

       response = self.client.post(('login'), data=data, follow=True)

       self.assert_(response.status_code, 200)


       response = self.client.post(('PassengerHomePage/'), data=data, follow=True)


       self.assertTemplateNotUsed(response, 'PassengerHomePage.html')
   

   def test_PassengerProfile(self):
      c = Client()
      response = c.get(('PassengerProfile'))
      self.assert_(response.status_code, 200)
      self.assertTemplateNotUsed(response, 'PassengerProfile.html')


   def test_LogIn_PassengerGetDic(self):
      response = self.client.get('Login')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerGetDic'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)


   def test_LogIn_AdminHomePage(self):
      response = self.client.get('Login')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('AdminHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)
###
   def test_LogIn_DriverHomePage(self):
      response = self.client.get('Login')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('AdminHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)  


   def test_LogIn_add_new_passenger(self):
      response = self.client.get('signup')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('Login'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)   


   def test_LogIn_PassengerHomePage_toPassengerGetDic(self):
      response = self.client.get('signup')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerGetDic'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)


   
   def test_LogIn_PassengerGetDic_toPassengerHomePage(self):
      response = self.client.get('PassengerGetDic')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)      



   def test_LogIn_DriverNotification_toDriverHomePage(self):
      response = self.client.get('DriverNotification')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('DriverHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)        



   def test_LogIn_DriverChangePassword_toDriverHomePage(self):
      response = self.client.get('DriverChangePassword')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('DriverHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)


      
   def test_LogIn_MyDrive_toDriverHomePage(self):
      response = self.client.get('MyDrive')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('DriverHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300) 



   def test_LogIn_MyDrive_toDriverNotification(self):
      response = self.client.get('MyDrive')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('DriverNotification'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)  


   def test_LogIn_MyDrive_DriverHomePage(self):
      response = self.client.get('MyDrive')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('DriverHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)  


   def test_LogIn_DriverChangePassword_Login(self):
      response = self.client.get('MyDrive')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('Login'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)                      


   def test_PassengerGetDic_ToPassengerNotification(self):
      response = self.client.get('PassengerGetDic')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerNotification'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)


   def test_PassengerGetDic_ToPMyTrip(self):
      response = self.client.get('PassengerGetDic')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PMyTrip'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)        


   def test_PassengerGetDic_To74(self):
      response = self.client.get('PassengerGetDic')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('74//'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)        


   def test_PassengerGetDic_ToPassengerPassword(self):
      response = self.client.get('PassengerGetDic')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerPassword'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)


   def test_PassengerGetDic_ToLogin(self):
      response = self.client.get('PassengerGetDic')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('Login'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)     


   def test_PassengerGetDic_PassengerHomePage(self):
      response = self.client.get('PassengerGetDic')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerHomePage'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)



   def test_PassengerHomePage_ToPassengerNotification(self):
      response = self.client.get('PassengerHomePage')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerNotification'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)  


   def test_PassengerHomePage_ToPMyTrip(self):
      response = self.client.get('PassengerHomePage')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PMyTrip'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)   


   def test_PassengerHomePage_PassengerPassword(self):
      response = self.client.get('PassengerHomePage')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerPassword'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)         



   def test_PassengerHomePage_ToLogin(self):
      response = self.client.get('PassengerHomePage')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('Login'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)        



   def test_PassengerNotification_ToPMyTrip(self):
      response = self.client.get('PassengerNotification')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PMyTrip'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)   


   def test_PassengerNotification_ToPassengerPassword(self):
      response = self.client.get('PassengerNotification')#url שלב 1
      self.assertTrue(User.is_authenticated)

      response = self.client.get(('PassengerPassword'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)   




   def test_PassengerNotification_ToLogin(self):
     response = self.client.get('PassengerNotification')#url שלב 1
     self.assertTrue(User.is_authenticated)

     response = self.client.get(('Login'))#url אחרי הפעולה
     self.assertNotEqual(response.status_code, 300)

     response = self.client.get(('logoutUser'), follow=True)#log out

     self.assertNotEqual(response.status_code, 300)    



   def test_PMyTrip_ToPassengerNotification(self):
     response = self.client.get('PMyTrip')#url שלב 1
     self.assertTrue(User.is_authenticated)

     response = self.client.get(('PassengerNotification'))#url אחרי הפעולה
     self.assertNotEqual(response.status_code, 300)

     response = self.client.get(('logoutUser'), follow=True)#log out

     self.assertNotEqual(response.status_code, 300)  




   def test_PMyTrip_ToPassengerPassword(self):
     response = self.client.get('PMyTrip')#url שלב 1
     self.assertTrue(User.is_authenticated)

     response = self.client.get(('PassengerPassword'))#url אחרי הפעולה
     self.assertNotEqual(response.status_code, 300)

     response = self.client.get(('logoutUser'), follow=True)#log out

     self.assertNotEqual(response.status_code, 300)            



   def test_PMyTrip_ToLogin(self):
      response = self.client.get('PMyTrip')#url שלב 1
      self.assertTrue(User.is_authenticated)
 
      response = self.client.get(('Login'))#url אחרי הפעולה
      self.assertNotEqual(response.status_code, 300)

      response = self.client.get(('logoutUser'), follow=True)#log out

      self.assertNotEqual(response.status_code, 300)  



   def test_PMyTrip_ToPassengerHomePage(self):
     response = self.client.get('PMyTrip')#url שלב 1
     self.assertTrue(User.is_authenticated)

     response = self.client.get(('PassengerHomePage'))#url אחרי הפעולה
     self.assertNotEqual(response.status_code, 300)

     response = self.client.get(('logoutUser'), follow=True)#log out

     self.assertNotEqual(response.status_code, 300)    

   def test_PassengerPassword_ToPassengerNotification(self):
     response = self.client.get('PassengerPassword')#url שלב 1
     self.assertTrue(User.is_authenticated)

     response = self.client.get(('PassengerNotification'))#url אחרי הפעולה
     self.assertNotEqual(response.status_code, 300)

     response = self.client.get(('logoutUser'), follow=True)#log out

     self.assertNotEqual(response.status_code, 300)  


   def test_PassengerPassword_ToPMyTrip(self):
     response = self.client.get('PassengerPassword')#url שלב 1
     self.assertTrue(User.is_authenticated)

     response = self.client.get(('PMyTrip'))#url אחרי הפעולה
     self.assertNotEqual(response.status_code, 300)

     response = self.client.get(('logoutUser'), follow=True)#log out

     self.assertNotEqual(response.status_code, 300)   



   def test_PassengerPassword_ToLogin(self):
     response = self.client.get('PassengerPassword')#url שלב 1
     self.assertTrue(User.is_authenticated)

     response = self.client.get(('Login'))#url אחרי הפעולה
     self.assertNotEqual(response.status_code, 300)

     response = self.client.get(('logoutUser'), follow=True)#log out

     self.assertNotEqual(response.status_code, 300)                       






         
        



   


















            

      
                                                               
    
         
    

      
   


   # def test_add_homework_WithLogin123(self):
   #    self.client.force_login(self.user)
   #    teacher = Teacher.objects.create(user=self.user)
   #    data = {'name': 'name', 'password': 'password'}
   #    response = self.client.post(reverse('PassengerHomePage'), data=data, follow=True)
   #    self.assertEqual(response.status_code, 200)


   #    self.assertTemplateUsed(response, 'index.html')
   #    self.assertRedirects(response, reverse('Login'))


   



