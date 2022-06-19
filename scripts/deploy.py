from brownie import accounts, config, SimpleStorage, network



def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]['from_key'])
        
    

def deploy_simple_storage():
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
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
