from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Current Entry fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from":account,'allow_revert': True, "value": entrance_fee})

# 2500000 wei
# 0.0000000000025 ether

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from":account})

def main():
    fund()
    withdraw()