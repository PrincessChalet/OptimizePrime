from django.shortcuts import render

# Create your views here.
def homeView(request):

    # this function is just used to display
    # Don't think it needs context so just pass an empty object

    return render(request, 'home_index/index.html', {})