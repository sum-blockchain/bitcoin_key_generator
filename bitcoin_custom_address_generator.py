from bitcoin import *

# input a custom string for the private key
my_priv = sha256('this is my bitcoin private address')
print(f'My private key = {my_priv}')

# generate the public key based on the private key we just created
my_pub = privtopub(my_priv)
print(f'My public key = {my_pub}')

# generate the BTC address
my_btc_addr = pubtoaddr(my_pub)
print(f'My BTC address = {my_btc_addr}')
