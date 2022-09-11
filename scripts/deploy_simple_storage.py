from brownie import accounts, config, SimpleStorage, network
from scripts.util_scripts import get_account


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    store_value = simple_storage.retrieve()
    print(store_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)


def main():
    deploy_simple_storage()
