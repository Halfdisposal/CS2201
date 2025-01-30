from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse



# create a function
def app_view(request):
    return HttpResponse("<h1>Welcome to First App </h1>")

# Create your views here.
from .models import Book
def BookDetailView(request, pk):
    book = get_object_or_404(Book, pk = pk)
    return render(request, 'app1/book_detail.html', {'book': book})

from django.shortcuts import redirect
from .forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'app1/register.html', {'form': form})

def accounts_login(request):
    return render(request, 'app1/index.html')



from .models import GeeksModel
def home(request):
    return render(request, 'app1/home.html')


