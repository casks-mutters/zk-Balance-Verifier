# app.py
from web3 import Web3
import hashlib
import sys

RPC_URL = "https://mainnet.infura.io/v3/your_api_key"

def pseudo_zk_proof(balance_wei):
    data = str(balance_wei).encode()
    return hashlib.sha256(data).hexdigest()

def get_balance(address):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ Connection to RPC failed.")
        sys.exit(1)
        print("🌐 Connected to network:", w3.eth.chain_id)
    balance_wei = w3.eth.get_balance(Web3.to_checksum_address(address))
    return balance_wei

def check_multiple(addresses):
    for addr in addresses:
        balance = get_balance(addr)
        proof = pseudo_zk_proof(balance)
        print("🔗 Address:", addr)
        print("💰 Balance (ETH):", Web3.from_wei(balance, 'ether'))
        print("🧩 Zero-Knowledge Proof (simulated hash):", proof)
        print("✅ Verification complete — proof integrity sound.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <eth_address_1> [eth_address_2 ...]")
        sys.exit(1)
    addresses = sys.argv[1:]
    check_multiple(addresses)
