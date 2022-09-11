from brownie import FundMe, network
from scripts.util_scripts import get_account

def deploy_fund_me():
    account = get_account()

    if network.show_active() != "development":
        fund_me = FundMe.deploy({"from": account})
        print(f'Contract deployed to {fund_me.address}')


def main():
    deploy_fund_me()