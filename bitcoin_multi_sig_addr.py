from bitcoin import *

#generate the first set of keys
my_priv_key_1 = random_key()
print(f'My first private key = {my_priv_key_1}')
my_pub_key_1 = privtopub(my_priv_key_1)
print(f'My first public key = {my_pub_key_1}')

#generate the second set of keys
my_priv_key_2 = random_key()
print(f'My second private key = {my_priv_key_2}')
my_pub_key_2 = privtopub(my_priv_key_2)
print(f'My second public key = {my_pub_key_2}')

#using the new keys, create a new multi sig address
my_multisig = mk_multisig_script(my_pub_key_1, my_pub_key_2, 1, 2)
my_multisig_addr = scriptaddr(my_multisig)
print(f'My multi sig BTC address = {my_multisig_addr}')
