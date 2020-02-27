 BIN +121 Bytes (120%) TechReviewProject/TechReviewApp/__pycache__/urls.cpython-36.pyc 
Binary file not shown.
  BIN +371 Bytes (120%) TechReviewProject/TechReviewApp/__pycache__/views.cpython-36.pyc 
Binary file not shown.
  5  TechReviewProject/TechReviewApp/templates/TechReviewApp/loginmessage.html 
@@ -0,0 +1,5 @@
{% extends 'base.html' %}
{% block content %}
<h2>Welcome</h2>
<p>Thanks for logging in</p>
{% endblock %} 
  5  TechReviewProject/TechReviewApp/templates/TechReviewApp/logoutmessage.html 
@@ -0,0 +1,5 @@
{% extends 'base.html' %}
{% block content %}
<h2>Goodbye</h2>
<p>Thanks for visiting</p>
{% endblock %} 
  2  TechReviewProject/TechReviewApp/templates/base.html 
@@ -20,6 +20,8 @@ <h1>Tech Reviews</h1>
<li><a href="{% url 'products' %}">Products</a></li> 
<li><a href="{% url 'newproduct' %}">Add Products</a></li> 
<li><a href="{% url 'newreview' %}">Add Review</a></li>
<li><a href="{% url 'login' %}">Login</a></li>
<li><a href="{% url 'logout' %}">Logout</a></li>
</ul> 
</div> 
</nav> 
  9  TechReviewProject/TechReviewApp/templates/registration/login.html 
@@ -0,0 +1,9 @@
{% extends 'base.html' %}
{% block content %}
<h2>Login</h2>
<form method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">login</button>
</form>
{% endblock %} 
  2  TechReviewProject/TechReviewApp/urls.py 
@@ -9,5 +9,7 @@
    path('productDetail/<int:id>',views.productDetail, name='productdetail'),
    path('newProduct/', views.newProduct, name='newproduct'),
    path('newReview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]

  12  TechReviewProject/TechReviewApp/views.py 
@@ -1,6 +1,8 @@
from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
@@ -26,6 +28,7 @@ def productDetail(request, id):
    }
    return render (request, 'TechReviewApp/productdetail.html', context=context)

@login_required
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
@@ -38,6 +41,7 @@ def newProduct(request):
          form=ProductForm()
     return render(request, 'TechReviewApp/newproduct.html', {'form' : form})

@login_required
def newReview(request):
     form=ReviewForm
     if request.method=='POST':
@@ -48,4 +52,10 @@ def newReview(request):
               form=ReviewForm()
     else:
          form=ReviewForm()
     return render(request, 'TechReviewApp/newreview.html', {'form' : form}) 
     return render(request, 'TechReviewApp/newreview.html', {'form' : form})

def loginMessage(request):
     return render(request, 'TechReviewApp/loginmessage.html')

def logoutMessage(request):
     return render(request, 'TechReviewApp/logoutmessage.html') 
  BIN +82 Bytes (100%) TechReviewProject/TechReviewProject/__pycache__/settings.cpython-36.pyc 
Binary file not shown.
  BIN +51 Bytes (110%) TechReviewProject/TechReviewProject/__pycache__/urls.cpython-36.pyc 
Binary file not shown.
  2  TechReviewProject/TechReviewProject/settings.py 
@@ -123,3 +123,5 @@
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL='loginmessage'
LOGOUT_REDIRECT_URL='logoutmessage'
  1  TechReviewProject/TechReviewProject/urls.py 
@@ -19,4 +19,5 @@
urlpatterns = [
    path('admin/', admin.site.urls),
    path('TechReviewApp/', include('TechReviewApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
