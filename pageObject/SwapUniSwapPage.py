import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UniSwapPage:
    LOCATORS = {
        "password_field": (By.ID, "password"),
        "unlock_button_class": (By.CLASS_NAME, "btn-default"),
        "connect-button-uniswap": (By.XPATH, "//button[normalize-space()='Connect']"),
        "MetaMask-button": (By.XPATH, "//div[contains(text(),'MetaMask')]"),
        "next-button": (By.CLASS_NAME, "btn-primary"),
        "connect-button": (By.CSS_SELECTOR, "button[data-testid='page-container-footer-next']"),
        "user_wallet_address_uniswap": (By.CLASS_NAME, "ldiIWn"),
        "user_wallet_address_metamask": (By.CLASS_NAME, "selected-account__address"),
        "user-wallet-uniswap": (By.CSS_SELECTOR, "p.sc-m6ivbz-4.cRLmmC"),
        "wrap_token_button": (By.XPATH, "//button[@data-testid='wrap-button']"),
        "confirm_button_metamask": (By.CSS_SELECTOR, "button[data-testid='page-container-footer-next']"),
        "pending_text_metamask": (By.CSS_SELECTOR, "div.transaction-status-label.transaction-status-label--pending"),
        "success_message_uniswap": (By.XPATH, "//div[@class='sc-bczRLJ sc-nrd8cx-0 sc-1ma4iwx-0 hJYFVB fhPvJh dokMED']"),
        "token_amount_input": (By.CSS_SELECTOR, "input.sc-1x3stf0-0.iIWDYd.sc-3zewi2-11.diLZKF.token-amount-input"),
        "open_currency_select_button": (By.XPATH, "//button[contains(@class, 'open-currency-select-button')]"),
        "token_search_input": (By.ID, "token-search-input"),
        "token_name_uniswap": (By.XPATH, "//div[@title='Uniswap']"),
        "token_name_weth": (By.XPATH, "//div[@title='Wrapped Ether']"),
        "swap_button": (By.XPATH, "//button[@data-testid='swap-button']"),
        "confirm_swap_button": (By.CSS_SELECTOR, "div.sc-sx9n2y-0.eaUeqv.css-iapcxi"),
        "pending_modal_content_title": (By.XPATH, "//div[@data-testid='pending-modal-content-title' and contains(text(),'Success')]"),
        "currency_display_text": (By.CLASS_NAME, "currency-display-component__text"),
        "wrap_success_msg": (By.CSS_SELECTOR, "div.sc-bczRLJ.sc-nrd8cx-0.sc-1ma4iwx-0.hJYFVB.fhPvJh.dokMED")
    }

    def __init__(self, driver):
        self.driver = driver

    def highlight_element(self, element):
        original_style = element.get_attribute("style")
        new_style = "background-color: yellow; border: 2px solid red;"
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)
        time.sleep(1)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)

    def open_meta_mask_setup(self):
        # Switch to the MetaMask window
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        self.driver.refresh()

    def enter_unlock_password(self):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOCATORS["password_field"]))
        password_field.send_keys("Farhan@1234")

    def click_unlock_button(self):
        unlock_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["unlock_button_class"]))
        unlock_button.click()

    def switch_web(self):
        # Switch to the Uniswap window
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_uniswap_connect_button(self):
        connect_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["connect-button-uniswap"]))
        self.highlight_element(connect_button)
        connect_button.click()

    def click_MetaMask_connect_button(self):
        metamask_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["MetaMask-button"]))
        self.highlight_element(metamask_button)
        metamask_button.click()

    def click_next_button(self):
        next_button= WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["next-button"])).click()

    def click_connect_button(self):
        connect_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOCATORS["connect-button"])).click()

    def get_user_wallet_address_metamask(self):

        #get the wallet address
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.LOCATORS["user_wallet_address_metamask"])))
        wallet_address = self.driver.find_element(*self.LOCATORS["user_wallet_address_metamask"]).text
        print("User MetaMask wallet" ,wallet_address)
        return wallet_address

    def get_user_address_uniswap(self):
        try:
            #get wallet address uniswap
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.LOCATORS["user-wallet-uniswap"])))
            time.sleep(2)
            wallet_address = self.driver.find_element(*self.LOCATORS["user-wallet-uniswap"]).text
            print("User wallet address on uniswap", wallet_address)
            return wallet_address
        except:
            return False

    def get_user_balance(self):
        user_balance = self.driver.find_element(*self.LOCATORS["currency_display_text"]).text
        balance = user_balance
        print("User balance on MetaMask:", balance)
        return balance

    def switch_to_uniswap(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def enter_amount(self, amount):
        amount_field= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.LOCATORS["token_amount_input"])))
        self.highlight_element(amount_field)
        amount_field.click()

        amount_field = self.driver.find_element(*self.LOCATORS["token_amount_input"])
        amount_field.send_keys(amount)

    def select_token(self, index):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.LOCATORS["open_currency_select_button"]))
        token_button = self.driver.find_elements(*self.LOCATORS["open_currency_select_button"])
        token_button[index].click()

    def search_token(self, token_name):
        search_token= WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOCATORS["token_search_input"]))
        self.highlight_element(search_token)
        search_token.send_keys(token_name)

    def click_wrap_eth_token_name(self):
        click_wrap= WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOCATORS["token_name_weth"]))
        self.highlight_element(click_wrap)
        click_wrap.click()

    def click_uniswap_token_name(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOCATORS["token_name_uniswap"])).click()

    def click_button(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def wrap_eth_uniswap(self):
        balance = self.get_user_balance()
        if balance == 0:
            assert False, "Cannot continue test case because your balance is 0"
        self.switch_to_uniswap()
        amount = 0.0001
        self.enter_amount(amount)
        self.select_token(1)
        self.search_token("WETH")
        self.click_wrap_eth_token_name()
        self.click_button(self.LOCATORS["wrap_token_button"])
        time.sleep(2)
        self.open_meta_mask_setup()
        self.click_button(self.LOCATORS["confirm_button_metamask"])

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((self.LOCATORS["pending_text_metamask"])))

        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located((self.LOCATORS["pending_text_metamask"])))

        self.switch_to_uniswap()

        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((self.LOCATORS["wrap_success_msg"])))
        succcess_text = element.text
        assert "Wrapped" in succcess_text, "Wrapped not successful"
        print("Test Case Completed successfully")

    def swap_eth_uniswap(self):
        balance = self.get_user_balance()
        if balance == 0:
            assert False, "Cannot continue test case because your balance is 0"
        self.switch_to_uniswap()
        amount = 0.0001
        self.enter_amount(amount)
        self.select_token(1)
        self.search_token("Uniswap")
        self.click_uniswap_token_name()
        self.click_button(self.LOCATORS["swap_button"])
        self.click_button(self.LOCATORS["confirm_swap_button"])
        self.open_meta_mask_setup()
        self.click_button(self.LOCATORS["confirm_button_metamask"])
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((self.LOCATORS["pending_text_metamask"])))
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located((self.LOCATORS["pending_text_metamask"])))

        self.switch_to_uniswap()

        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((self.LOCATORS["pending_modal_content_title"])))
        text = element.text
        expected_text = "Success"
        assert text == expected_text, f"Transaction is not successful expected {expected_text} got {text}"