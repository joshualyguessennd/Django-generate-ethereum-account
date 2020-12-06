from rest_framework import serializers
from .models import Account
from web3 import Web3

public_key = "0x929500a528011160C83d2fC9999375F3afe1F763"
private_key = ""

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
        eth_addr = web3.eth.account.create()
        
        account = Account(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
                wallet = eth_addr.address
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        account.set_password
        account.save()
        return account
