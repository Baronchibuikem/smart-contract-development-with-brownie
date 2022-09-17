from brownie import network, config, accounts


def get_account():
    # running this locally, this will spin up an address and a private key for test purposes
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]['from_key'])
      