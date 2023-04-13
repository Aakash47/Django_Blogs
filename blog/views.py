from django.shortcuts import render, redirect
from django.views import generic
from . models import Post, Acco, Contact
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):
	context = {
	'posts': Post.objects.all(),
	'accos': Acco.objects.all()
	}
	return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

class blogpost(generic.DetailView):
	model = Post
	template_name = 'blogpost.html'

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		desc = request.POST.get('desc')
		contact = Contact(name=name,mail=email,desc=desc)
		contact.save()
		messages.success(request,'Thank You For Your Valuable Response!')
		return redirect('Home')
	return render(request, 'contact.html')

class SearchResultsView(generic.ListView):
	model = Post
	template_name = 'search_results.html'
	
	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Post.objects.filter(
			Q(title__icontains=query)
			)
		return object_list
