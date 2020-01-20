
# Enable brower http caching for homepage


def home_page(request):
    # get the django.http.response.HttpResponse object
    resp = render(request, 'base/home_page.html')
    # set http response header and value.
    resp['Cache-Control'] = 'public,max-age=100000'
    resp['Vary'] = 'Accept-Encoding'
    # return the HttpResponse object.


def standard_page(request):
    # get the django.http.response.HttpResponse object
    resp = render(request, 'base/standard_page.html')
    # set http response header and value.
    resp['Cache-Control'] = 'public,max-age=100000'
    resp['Vary'] = 'Accept-Encoding'
    # return the HttpResponse object.


def contact_page(request):
    # get the django.http.response.HttpResponse object
    resp = render(request, 'base/contact_page.html')
    # set http response header and value.
    resp['Cache-Control'] = 'public,max-age=100000'
    resp['Vary'] = 'Accept-Encoding'
    # return the HttpResponse object.
