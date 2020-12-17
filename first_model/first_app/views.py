from django.shortcuts import render
from first_app.models import Topic, AccessRecord, WebPage
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    data_dict = {'access_records': webpages_list}
    # d = {'insert_content': 'Hello first model app!'}
    return render(request, 'first_app/index.html', context=data_dict)
