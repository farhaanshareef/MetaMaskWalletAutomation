import pytest
from pageObject.MetaMaskPage import MetaMaskPage
from pageObject.SwapUniSwapPage import UniSwapPage

class Test_UniSwap:

    @pytest.mark.run(order=1)
    def test_wrap_eth_uniswap(self, setup):
        driver = setup
        self.uniswap_page = UniSwapPage(driver)
        self.uniswap_page.open_meta_mask_setup()
        self.uniswap_page.enter_unlock_password()
        self.uniswap_page.click_unlock_button()
        self.uniswap_page.switch_web()
        self.uniswap_page.click_uniswap_connect_button()
        self.uniswap_page.click_MetaMask_connect_button()
        uniwap_address= self.uniswap_page.get_user_address_uniswap()
        if uniwap_address == False:
            self.uniswap_page.open_meta_mask_setup()
            self.uniswap_page.click_next_button()
            self.uniswap_page.click_connect_button()
            metamask_address= self.uniswap_page.get_user_wallet_address_metamask()
            self.uniswap_page.switch_web()
            uniwap_address= self.uniswap_page.get_user_address_uniswap()

        else:
            self.uniswap_page.open_meta_mask_setup()
            metamask_address= self.uniswap_page.get_user_wallet_address_metamask()

        metamask_last_4 = metamask_address[-4:]
        uniswap_last_4 = uniwap_address[-4:]
        assert metamask_last_4 == uniswap_last_4, "Wallet not connected successfully"

        if uniwap_address != False:
            self.meta_mask_page = MetaMaskPage(driver)
            network_name= self.meta_mask_page.select_network()
            self.meta_mask_page.click_meta_mask_logo()
            if network_name== "Goerli test network":
                self.uniswap_page.wrap_eth_uniswap()

    @pytest.mark.run(order=2)
    def test_swap_eth_uniswap(self, setup):
        driver = setup
        self.uniswap_page = UniSwapPage(driver)
        self.uniswap_page.open_meta_mask_setup()
        self.uniswap_page.enter_unlock_password()
        self.uniswap_page.click_unlock_button()
        self.uniswap_page.switch_web()
        self.uniswap_page.click_uniswap_connect_button()
        self.uniswap_page.click_MetaMask_connect_button()
        uniwap_address = self.uniswap_page.get_user_address_uniswap()
        if uniwap_address == False:
            self.uniswap_page.open_meta_mask_setup()
            self.uniswap_page.click_next_button()
            self.uniswap_page.click_connect_button()
            metamask_address = self.uniswap_page.get_user_wallet_address_metamask()
            self.uniswap_page.switch_web()
            uniwap_address = self.uniswap_page.get_user_address_uniswap()
        else:
            self.uniswap_page.open_meta_mask_setup()
            metamask_address = self.uniswap_page.get_user_wallet_address_metamask()

        metamask_last_4 = metamask_address[-4:]
        uniswap_last_4 = uniwap_address[-4:]
        assert metamask_last_4 == uniswap_last_4, "Wallet not connected successfully"

        if uniwap_address != False:
            self.meta_mask_page = MetaMaskPage(driver)
            network_name = self.meta_mask_page.select_network()
            self.meta_mask_page.click_meta_mask_logo()
            if network_name == "Goerli test network":
                self.uniswap_page.swap_eth_uniswap()