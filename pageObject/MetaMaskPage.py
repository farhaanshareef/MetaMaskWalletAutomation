import time
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
        "meta_mask_logo": (By.CLASS_NAME, "app-header__logo-container--clickable")
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
        WebDriverWait(self.driver, 20).until(
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

    def import_wallet(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["import_button"])).click()

    def click_got_it_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["got_it_button"])).click()

    def click_next_and_done_buttons(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["next_button"]))
        next_button = self.driver.find_elements(*self.LOCATORS["next_button"])
        next_button[0].click()
        time.sleep(1)
        next_button[0].click()

    def close_whats_new_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["whats_new_popup_button"])).click()

    def go_back(self):
        self.driver.back()

    def click_meta_mask_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATORS["meta_mask_logo"])).click()