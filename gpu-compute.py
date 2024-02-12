import os
import subprocess
from eth_account import Account

def generate_random_private_key(prefix):
    key_length = 32  # Private key length in bytes
    while True:
        random_suffix = os.urandom(key_length - len(prefix) // 2).hex()
        if not random_suffix.endswith(("ba987")):
            return prefix + random_suffix

def find_matching_address(prefixes, private_key):
    address = Account.from_key(private_key).address.lower()
    return any(address.startswith(prefix.lower()) for prefix in prefixes)

try:
    while True:
        random_private_key = generate_random_private_key("9ffb3894434556451e2254800ecae2f99cfe964b1440901aaf718ec1")
        derived_address = Account.from_key(random_private_key).address.lower()
        prefixes_to_check = ["0x2b6ed"]
        if find_matching_address(prefixes_to_check, random_private_key):
            # Command to set GPU for computing
            command = f'nvidia-smi -i 0,1,2,3 -c EXCLUSIVE_PROCESS'
            subprocess.run(command, shell=True, check=True)
            print(f"Random Private Key: {random_private_key}, "
                  f"Matching Address: {derived_address}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
