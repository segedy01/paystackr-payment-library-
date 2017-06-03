from application.modules.paystackr import PayStackr
from application.modules.exceptions import (FailedAuthentication, InvalidHTTPMethod, InvalidPayload,
	InvalidType)
import os
from unittest import TestCase
import requests_mock
import requests


class PayStackrTest(TestCase):

	def setup(self):
		pass


	def teardown(self):
		pass


	def test_failed_authentication(self):

		hold_secret_key = os.environ['SECRET_KEY']
		del os.environ['SECRET_KEY']

		with self.assertRaises(FailedAuthentication):
			paystack = PayStackr()

		os.environ['SECRET_KEY'] = hold_secret_key


	def test_method_exceptions(self):

		method = {
				'fake_method': 'isnotput',
				'valid_method': 'get'
				}
		url = 'https://api.paystack.co/customer'
		url_new = 'https://api.paystack.co/transaction/initialize'
		payload = 'isthisapayload?'

		paystack = PayStackr()

		with self.assertRaises(InvalidHTTPMethod):
			raiseerror =  paystack.method_calls(url=url, method=method.get('fake_method'))

		with self.assertRaises(InvalidPayload):
			raiserror = paystack.method_calls(url=url_new, method=method.get('valid_method'), payload=payload)



	def test_header(self):

		paystack = PayStackr()

		response = paystack.set_header(test='test_dict')
		self.assertEqual(response.get('test'), 'test_dict')


	def test_get_method_call(self):
		paystack = PayStackr()

		with requests_mock.mock() as mockingmocker:
			mockingmocker.get('http://test.com', json={'status':'testok',
				'message':{'run': 'fools'}, 'data': 'please fuck of'}, 
				headers={'test': 'header'})
			response = paystack.method_calls(method='get', url='http://test.com',payload={'test':'test_load'})

			json_response = response.json()

			print json_response

			self.assertEqual(response.status_code, 200)
			self.assertEqual(json_response.get('status'), 'testok')
			self.assertEqual(json_response.get('message'), {'run': 'fools'})


	@staticmethod
	def _request_callback(request, context):
		context.status_code = 201
		context.headers['test'] = 'header'
		return {'request': request.body}


	def test_post_method_call(self):
		url = 'https://joblivery.com'
		paystack = PayStackr()

		with requests_mock.mock() as mockingmocker:
			mockingmocker.post(url, json=self.__class__._request_callback)
			response = requests.post(url, data='data')

		json_response = response.json()
		print json_response

		self.assertEqual(response.status_code, 201)
		self.assertEqual(json_response.get('request'), 'data')

