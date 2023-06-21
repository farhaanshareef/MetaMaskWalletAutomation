import time
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MetaMaskPage:
    LOCATORS = {
        "terms_checkbox": (By.ID, "onboarding__terms-checkbox"),
        "import_wallet_button": (By.CLASS_NAME, "btn-secondary"),
        "agree_button": (By.CLASS_NAME, "btn--large"),
        "seed_phrase_input": (By.ID, "import-srp__srp-word-{}"),
        "confirm_recovery_button": (By.CLASS_NAME, "import-srp__confirm-button"),
        "password_input": (By.CLASS_NAME, "form-field__input"),
        "privacy_policy_checkbox": (By.CLASS_NAME, "fa-square"),
        "import_button": (By.CLASS_NAME, "create-password__form--submit-button"),
        "got_it_button": (By.CLASS_NAME, "btn--large"),
        "next_button": (By.CLASS_NAME, "btn-primary"),
        "whats_new_popup_button": (By.CLASS_NAME, "whats-new-popup__button"),
        "meta_mask_logo": (By.CLASS_NAME, "app-header__logo-container--clickable"),
        "password_field": (By.ID, "password"),
        "unlock_button_class": (By.CLASS_NAME, "btn-default"),
        "connect-button-uniswap": (By.XPATH, "//button[normalize-space()='Connect']"),
        "select-network": (By.CLASS_NAME, "chip__left-icon"),
        "show-networks-button": (By.CLASS_NAME, "network-dropdown-content--link"),
        "toggle-button-class" : (By.CLASS_NAME, 'settings-page__content-item-col'),
        "goerli_network_xpath": (By.XPATH, "//span[contains(text(),'Goerli test network')]"),
        "primary_button": (By.CSS_SELECTOR, ".btn--rounded.btn-primary"),
        "add_manually_button": (By.CSS_SELECTOR, "h6.box.mm-text.mm-text--body-sm.box--flex-direction-row.box--color-primary-default"),
        "add_network_button": (By.CLASS_NAME, "network__add-network-button")
    }

    def __init__(self, driver):
        self.driver = driver

    def open_meta_mask_setup(self):
        # Switch to the MetaMask window
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.refresh()
        #self.driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome")

    def accept_terms_and_conditions(self):
        # Click on the terms and conditions checkbox
        WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable(self.LOCATORS["terms_checkbox"])).click()

    def import_existing_wallet(self):
        # Click on the "Import an existing wallet" button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["import_wallet_button"])).click()

    def agree_and_proceed(self):
        # Click on the "I Agree" button
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.LOCATORS["agree_button"])).click()

    def enter_seed_phrase(self):
        words = ["hidden", "aisle", "tiger", "dove", "pact", "nominee", "ship", "symbol", "satoshi", "blade", "hero",
                 "glimpse"]

        for i in range(12):
            word_field = self.driver.find_element(By.ID, f"import-srp__srp-word-{i}")
            word_field.send_keys(words[i])

    def click_confirm_recovery_button(self):
        # Click on the confirm recovery button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["confirm_recovery_button"])).click()

    def enter_password(self, password):
        time.sleep(1)
        password_field = self.driver.find_elements(*self.LOCATORS["password_input"])
        password_field[0].send_keys(password)

    def confirm_password(self, password):
        confirm_password_field = self.driver.find_elements(*self.LOCATORS["password_input"])
        confirm_password_field[1].send_keys(password)

    def accept_privacy_policy(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["privacy_policy_checkbox"])).click()

    def click_import_wallet_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["import_button"])).click()

    def click_got_it_button(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='onboarding-complete-done']"))).click()
        except:
            assert False, "Got it button is not clickable"

    def click_next_and_done_buttons(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='pin-extension-next']")))
        next_button= self.driver.find_element(By.CSS_SELECTOR, "[data-testid='pin-extension-next']")
        next_button.click()
        time.sleep(2)
        done_button = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='pin-extension-done']")
        done_button.click()

    def close_whats_new_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["whats_new_popup_button"])).click()

    def go_back(self):
        self.driver.back()

    def click_meta_mask_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["meta_mask_logo"])).click()

    def enter_unlock_password(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.LOCATORS["password_field"])).send_keys("Farhan@1234")

    def click_unlock_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["unlock_button_class"])).click()

    def switch_web(self):
        # Switch to the opensea window
        self.driver.switch_to.window(self.driver.window_handles[0])

    def select_network(self):
        network = 'Goerli test network'
        try:
            #click on the got it button
            got_it_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.LOCATORS["primary_button"]))
            got_it_button.click()
        except:
            pass
        try:
            #check if the network is already selected
            xpath = f"//span[contains(text(), '{network}')]"
            network_element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            network_name = network_element.text
            print("The current selected network name is", network_name)
            return network_name
        except TimeoutException:
            print(f"{network} is not added yet. Please add it first")
            #if network is not visible then add network
            select_network_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LOCATORS["select-network"]))
            select_network_button.click()

            show_networks_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LOCATORS["show-networks-button"]))
            show_networks_button.click()

            time.sleep(1)
            options = self.driver.find_elements(By.CLASS_NAME, 'settings-page__content-item-col')
            toggle_button = options[4]

            toggle_button_state = toggle_button.text.strip().lower()
            print(toggle_button_state)
            if toggle_button_state == "on":
                print("Toggle button is already ON")
            else:
                toggle_button.click()
                print("Toggle button is not ON. Additional actions can be performed here.")

            select_network_button.click()

            xpath = f"//span[contains(text(), '{network}')]"
            goerli_network = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            network_name = goerli_network.text
            print("The network name is ", network_name)
            goerli_network.click()
            time.sleep(1)
            return network_name

    def add_network(self):
        # Network add details
        network = 'Smart Chain-Testnet'
        rpc_url = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
        network_id = "97"
        token_name = "BNB"
        explorer_link = "https://testnet.bscscan.com"

        try:
            #click on the got it button on welcome screen
            got_it_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.LOCATORS["primary_button"]))
            got_it_button.click()
        except:
            pass

        try:
            xpath = "//span[contains(text(), '{network}')]"
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            network_name = self.driver.find_element(By.XPATH, xpath).text
            if network_name == "Smart Chain-Testnet":
                print("Binance network is already added")
        except:
            # Click on network button
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.LOCATORS["select-network"])).click()

            except ElementClickInterceptedException:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.LOCATORS["select-network"])).click()

            # Click on add network button
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.LOCATORS["add_network_button"])).click()

            # Click on add network manually button text
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.LOCATORS["add_manually_button"])).click()

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "form-field__input")))
            # Add the text on all the required fields on add network page
            network_fields = self.driver.find_elements(By.CLASS_NAME, 'form-field__input')
            network_fields[0].send_keys(network)
            network_fields[1].send_keys(rpc_url)
            network_fields[2].send_keys(network_id)
            network_fields[3].send_keys(token_name)
            network_fields[4].send_keys(explorer_link)
            save_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.LOCATORS["primary_button"])).click()
            switch_confirm_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            "h6.box.mm-text.mm-text--body-sm.box--flex-direction-row.box--color-primary-inverse"))).click()
            got_it = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable(self.LOCATORS["primary_button"])).click()

            xpath = "//span[contains(text(), '{network}')]"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            network_name = self.driver.find_element(By.XPATH, xpath).text
            expected_text = network
            assert network_name == expected_text, f"Network not added successfully. Expected {expected_text}, got {network_name}"