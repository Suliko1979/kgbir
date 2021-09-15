from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.views.generic import View


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

