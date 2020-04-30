from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterationForm, UserUpdateForm, ProfileUpdateForm
from store.contexting import list_of_sub_categories, list_of_categories


def register(request):
  if request.method == 'POST':
    form = UserRegisterationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account has been created for {username}!')
      return redirect('login')
  else:
    form = UserRegisterationForm()
  context = {"categories_list": list_of_categories(),
             "sub_categories_list": list_of_sub_categories(),
             "form": form
             }
  return render(request, 'users/register.html', context)

@login_required()
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, f'Your Account has been updated!')
      return redirect ('profile')
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form': u_form,
    'p_form': p_form,
    "categories_list": list_of_categories(),
    "sub_categories_list": list_of_sub_categories()
  }
  return render(request, 'users/profile.html', context)

