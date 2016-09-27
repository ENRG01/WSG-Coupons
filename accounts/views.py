from .forms import PersonCreationForm, EditProfileForm
from django.shortcuts import redirect, render

# User Registration form
def register(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = PersonCreationForm()
    return render(request, 'registration/register.html', {'form':form})

# User Edit form
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return redirect('coupons:index')
    else:
        form = EditProfileForm()
    return render(request, 'registration/profile_edit.html', {'form':form})
