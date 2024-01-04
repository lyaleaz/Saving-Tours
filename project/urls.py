'''
urls
'''
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('abouthome',views.abouthome,name="abouthome"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    path('Login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('AdminReports/',views.AdminReports,name="AdminReports"),
    path('PassengerPassword/<int:id>',views.PassengerPassword,name="PassengerPassword"),
    path('<int:id>///',views.PassengerProfile,name="PassengerProfile"),
    path('DriverSignup/',views.DriverSignup,name="DriverSignup"),
    path('AdminHomePage/',views.AdminHomePage,name="AdminHomePage"),
    path('AddNewDriver/',views.AddNewDriver,name="AddNewDriver"),
    path('PassengerHomePage/',views.PassengerHomePage,name="PassengerHomePage"),
    path('SendMail/',views.SendMail,name="SendMail"),
    path('DriverFile/',views.DriverFile,name="DriverFile"),
    path('DriverHomePage/',views.DriverHomePage,name="DriverHomePage"),
    path('Request/',views.Request,name="Request"),
    path('<int:id>', views.details,name='detail'),
    path('<int:id>/"',views.accept,name="Accept"),
    path('<int:id>//',views.decline,name="Decline"),
    path('DeleteOrder/<int:id>',views.DeleteOrder,name="DeleteOrder"),
    path('PassenegrTripInfo/<int:id>',views.PassenegrTripInfo,name="PassenegrTripInfo"),
    path('PassengerListForDriver/<int:bus>',views.PassengerListForDriver
    ,name="PassengerListForDriver"),
    path('DriverChangePassword/<int:id>',views.DriverChangePassword,name="DriverChangePassword"),
    path('MyDrive/',views.MyDrive,name="MyDrive"),
    path('PassengerGetDic/<busnum>/<buscompany>/',views.PassengerGetDic,name="PassengerGetDic"),
    path('DriverDetails/',views.DriverDetails,name="DriverDetails"),
    path('deluser/',views.deluser,name="deluser"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('Block/<int:id>',views.Block,name="Block"),
    path('deleteDriver/<int:id>',views.deleteDriver,name="deleteDriver"),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('NotificationByDriver',views.NotificationByDriver,name="NotificationByDriver"),
    path('PassengerNotification/',views.PassengerNotification,name="PassengerNotification"),
    path('DriverNotification/',views.DriverNotification,name="DriverNotification"),
    path('PMyTrip/',views.PMyTrip,name="PMyTrip"),
    path('Report/<int:id>',views.report,name="report"),
    path('TripEnd/<int:id>',views.endtrip,name="endtrip"),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
