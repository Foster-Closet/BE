
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foster_closet.settings")
import django
django.setup()

from twilio.rest import Client
from django.conf import settings


print(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)




message = client.messages.create(
                     body='Test message from python',
                     from_='+19198997515',
                     to='+19193601335'
                 )