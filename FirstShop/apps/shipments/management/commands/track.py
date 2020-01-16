
from django.core.management.base import BaseCommand
from ._private import save_log
from apps.delivery_api.models import Provider
import requests
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--order', type=int, help="order")

    def handle(self, *args, **options):
        if options['order']:
            try:
                o_id = Provider.objects.filter(invoice_id=options['order'])
            except Exception as e:
                print(e)
            else:
                if o_id.exists():
                    params = {
                        "OrderID": options['order'],
                    }
                    API_key = 'Un7g6Viz.rFN3a9IMQYegqDauHOnwH5LSSO64YlyQ'
                    response = requests.get('http://{}:{}/delivery_api/{}'.format(settings.HOST_NAME, settings.PORT, options['order']),
                                            headers={'format': 'json', 'Authorization': 'Api-Key {}'.format(API_key)})

                    if response.status_code == 200:
                        save_log(params, response)
                        print(response.text)
                    else:
                        save_log(params, response)
                        print(response.status_code)
                print(response)

