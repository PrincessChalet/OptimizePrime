from django.shortcuts import render

# Create your views here.
def homeView(request):

    # The line below does not account for user accounts
    # will likely need to nest this in some branched statements
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    # this function is just used to display
    # Don't think it needs context so just pass an empty object

    return render(request, 'home_index/index.html', {})