"""
    Payment Class
"""
from application.constants.utils_constants import *
from .exceptions import *
from paystackr import PayStackr
import requests


class Payments(PayStackr):

	def initialise_payment(self, payload, currency):
		"""
			args:
				payload = 
				{
					callback_url: a redirect url
					amouunt: 5000
					email: customer_email
				}

				curency = Naira/Dollar
		"""
		if payload:
			callback = payload['callback_url']
			amount = payload['amount']
			email = payload['email']

		else:
			raise InvalidPayload('we need a payload please')

		if currency:
			if currency.upper() == 'NAIRA':
				amount_in_kobo = amount * KOBO

			elif currency.upper() == 'DOLLAR':
				#calls a converiosn api that collects the 
				#amount converts it to naira then to kobo
				#later should be changed to a file where it can be edited from dashboard
				conversion_url = 'http://apilayer.net/api/live?access_key='+ CURRENCY_ACCESS_KEY + '&currencies=NGN'
				response = requests.post(conversion_url)
				json_response = response.json()
				xchange = float(json_response['quotes']['USDNGN'])
				dollar_to_naira = amount * xchange
				amount_in_kobo = dollar_to_naira * KOBO

			else:
				raise InvalidType('currency should be in naira or dollar')

		else:
			raise InvalidPayload('a valid currency is expected')

		valid_payload = {
			'callback_url': callback,
			'amount': amount_in_kobo,
			'email': email
		}

		url = Base_API + '/transaction/initialize'
		response = self.method_calls(POST, url, valid_payload)
		return response


	def verify_transaction(self, reference):

		"""
		"""

		url = Base_API + '/transaction/verify/' + str(reference)
		response = self.method_calls(GET, url)
		return response