Step to create django framework website:

1) django-admin startproject djangocore
2) python manage.py start app djangoapp
    djangocore --> source as root
      --> djangocore
      --> djangoapp
      --> rasaapp

django core :
  setting.py 
    'djangoapp'
    'rasaapp'
  urls.py:
    from .views import index
      path('url',function),

django app:
   static
     djangoapp
       css -->
   templates:
     djangoapp
       index.html --> { % load static % } , src="{% static 'djangoapp/.png' %}"
   views.py
     def index(request):
        return render(request,'djangoapp/index.html')


rasaapp:
  Before Install rasa and run rasa init

after train your model with your conversation and enable api using 

#rasa run -m models --enable-api --cors "*" --debug

and copy the file to rasapp folder in django

check the url : https://github.com/JiteshGaikwad/Chatbot-Widget

static
  rasaapp 
    css images
templates
  rasaapp
     html
views.py
    def rasa(requests):
      return render(request,'rasaapp.index.html)




-------**********----------
