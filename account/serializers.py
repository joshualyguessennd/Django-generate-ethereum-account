from rest_framework import serializers
from .models import Account
from web3 import Web3, Account as account_eth
import hashlib #for SHA256 computation
import binascii # for conversion between Hexa and bytes
import secrets
import os
import unicodedata


<<<<<<< HEAD
=======
public_key = "0x929500a528011160C83d2fC9999375F3afe1F763"
private_key = ""
>>>>>>> eb90fceb6b76639873dd01bb9a4cbc34d6d74a13

url = "https://rinkeby.infura.io/v3/"
web3 = Web3(Web3.HTTPProvider(url))



class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
                    'password': {'write_only': True}
        }
    

    


    def save(self):
        
        entropy = secrets.token_hex(16)
        data = entropy.strip()
        data = binascii.unhexlify(data)
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'wordlist/english.txt')

        if len(data) not in [16, 20, 14, 28, 32]:
            raise ValueError(
                "Data should be one of the following: [16, 20, 24, 32], but it is not (%d)." % len(data))
        h = hashlib.sha256(data).hexdigest()
        b = bin(int(binascii.hexlify(data), 16))[2:].zfill(
            len(data)*8)+bin(int(h, 16))[2:].zfill(256)[: len(data)*8//32]
        with open(file_path, "r") as f:
            wordlist = [w.strip() for w in f.readlines()]
        seed = []
        for i in range(len(b)//11):
            indx = int(b[11*i:11*(i+1)],2)
        seed.append(wordlist[indx])
        seed_list = " ".join(seed)
        account_eth.enable_unaudited_hdwallet_features()
        eth_addr = web3.eth.account.from_mnemonic(seed_list)
        
        account = Account(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
                wallet = eth_addr.address,
                seed = seed
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        account.set_password
        account.save()
        return account
