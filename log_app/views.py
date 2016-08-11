from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .models import Log

# Create your views here.


# class HomeView(TemplateView):
#     template_name = 'index.html'
#
#     def post(self, request):
#         print(request.GET['level'])
#         print(request.GET['name_logger'])
#         print(request.GET['message'])
#         return HttpResponseRedirect('/')
#
#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         if self.request.user.is_authenticated():
#             context['user_message'] = 'Authenticated user'
#         else:
#             context['user_message'] = 'Non Authenticated user'
#         return context


@csrf_exempt
def index_view(request):
    context = {}
    if request.user.is_authenticated():
        context['user_message'] = 'Authenticated user'
        if request.method == 'POST':
            Log.objects.create(
                level=request.POST['level'],
                message=request.POST['message'],
                name_logger=request.POST['name_logger'],
                sender_id=request.user.id
            )
        loggers = Log.objects.filter(sender_id=request.user.id).all()
        context['loggers'] = loggers
    else:
        context['user_message'] = 'Non Authenticated user'
    return render(request, 'index.html', context)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        login(request, user)
        return HttpResponse('ok')
        # return redirect('/')
        # return HttpResponseRedirect('/')
    my_form = AuthenticationForm()
    return render(request, 'login.html', {'form': my_form})


# class AuthorisationView(FormView):
#     form_class = AuthenticationForm
#     template_name = 'login.html'
#     success_url = '/'
#
#     def form_valid(self, form):
#         self.user = form.get_user()
#         login(self.request, self.user)
#         return super(AuthorisationView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)
