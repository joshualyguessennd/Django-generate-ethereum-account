from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from web3 import Web3
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from .models import Generated_adress
# Create your views here.

public_key = "Your public address"
private_key = "Your private Key"

url = "https://rinkeby.infura.io/v3/#####################"

web3 = Web3(Web3.HTTPProvider(url))

address = web3.toChecksumAddress("0x9944336231a7F8EEb325F314DafAED075cAB59d9")
abi = json.loads('''[
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "address",
				"name": "asset",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "allowee",
				"type": "address"
			}
		],
		"name": "tokenAllowance",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')


contract = web3.eth.contract(address=address, abi=abi)

@csrf_exempt
def generate_random_address(request):
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        value = request.POST.get('value')
        data = {}
        address = web3.eth.account.create()
        a = address.address
        str_data = str(a)

        foo_create = Generated_adress.objects.update_or_create(address=str_data, user_id=user_id, value=value)
        data = {
            'address': str_data,
            'value': value,
            'user_id': user_id
        }
    return JsonResponse(data)
