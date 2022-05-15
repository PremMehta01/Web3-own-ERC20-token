from scripts.helpful_scripts import get_account
from brownie import ComingToken, config, network
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    coming_token = ComingToken.deploy(
        initial_supply,
        {"from": account},
        # publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(
        "Newly deployed token: "
        + str(coming_token.name())
        + " with total-supply of wei: "
        + str(initial_supply)
    )
