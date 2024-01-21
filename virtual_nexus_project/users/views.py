from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse_lazy
from .forms import UserProfileForm
from .models import UserProfile

@method_decorator(login_required(login_url=reverse_lazy('account_login')), name='dispatch')
class ProfileView(View):
    template_name = 'profile/profile.html'

    def get(self, request):
        form = UserProfileForm(instance=request.user.userprofile)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form}) 
    
class ProfileDetailView(View):
    template_name = 'profile/profile.html'

    def get(self, request, pk):
        user_profile = get_object_or_404(UserProfile, pk=pk)
        return render(request, self.template_name, {'user': user_profile})
