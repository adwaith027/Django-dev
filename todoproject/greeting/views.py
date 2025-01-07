from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def randomfn(request):
    return render(request,'rep.html')




def redir(request):
    return redirect('/issue')

def page(request,titl):
    return render(request,'page.html',{'data':titl})

def count(request,num):
    return render(request,'count.html',{'data':num})

def page_vist(request):
    # Get the current count from the session, or set it to 0 if it doesn't exist
    count = request.session.get('page_count', 0)
    # Increment the count
    count += 1
    # Store the updated count in the session
    request.session['page_count'] = count
    # Render the template with the count variable
    return render(request,'page_view.html', {'count': count})


def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})


def login_user(request):
    if request.method=='POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           user = form.get_user()
           login(request, user)
           return redirect('/')
    else:
        form = AuthenticationForm()
        print(form)
    return render(request,'login.html',{'form': form})


# @login_required(login_url='/login/')
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)