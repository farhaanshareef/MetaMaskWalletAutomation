from pageObject.MetaMaskPage import MetaMaskPage

class Test_MetaMask:

    def test_setup_meta_mask(self, setup):
        driver = setup
        self.meta_mask_page = MetaMaskPage(driver)
        self.meta_mask_page.open_meta_mask_setup()
        self.meta_mask_page.accept_terms_and_conditions()
        self.meta_mask_page.import_existing_wallet()
        self.meta_mask_page.agree_and_proceed()
        self.meta_mask_page.enter_seed_phrase()
        self.meta_mask_page.click_confirm_recovery_button()
        self.meta_mask_page.enter_password("Farhan@1234")
        self.meta_mask_page.confirm_password("Farhan@1234")
        self.meta_mask_page.accept_privacy_policy()
        self.meta_mask_page.click_import_wallet_button()
        self.meta_mask_page.click_got_it_button()
        self.meta_mask_page.click_next_and_done_buttons()
        self.meta_mask_page.close_whats_new_popup()
        self.meta_mask_page.go_back()
        self.meta_mask_page.close_whats_new_popup()
        self.meta_mask_page.click_meta_mask_logo()

    def test_add_network(self, setup):
        driver= setup
        self.meta_mask_page = MetaMaskPage(driver)
        self.meta_mask_page.open_meta_mask_setup()
        self.meta_mask_page.enter_unlock_password()
        self.meta_mask_page.click_unlock_button()
        self.meta_mask_page.add_network()

    def test_change_network(self, setup):
        driver = setup
        self.meta_mask_page = MetaMaskPage(driver)
        self.meta_mask_page.open_meta_mask_setup()
        self.meta_mask_page.enter_unlock_password()
        self.meta_mask_page.click_unlock_button()
        self.meta_mask_page.select_network()
        self.meta_mask_page.click_meta_mask_logo()
