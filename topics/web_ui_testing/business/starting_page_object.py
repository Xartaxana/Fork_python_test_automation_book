from playwright.sync_api import Page


class StartingPage:

    def __init__(self, page: Page):
        self.page = page
        self.user_form = page.locator("#userForm")
        self.full_name_field = self.user_form.locator("#userName")
        self.email_field = self.user_form.locator("#userEmail")
        self.current_address_field = self.user_form.locator("#currentAddress")
        self.permanent_address_field = self.user_form.locator("#permanentAddress")
        self.submit_button = page.locator("#submit")
        self.output = page.locator("#output")
        self.full_name_output = self.output.locator("#name")
        self.email_output = self.output.locator("#email")
        self.current_address_output = self.output.locator("#currentAddress")
        self.permanent_address_output = self.output.locator("#permanentAddress")

    def navigate(self, user_data):
        self.page.goto(user_data["base_url"])

    def fill_user_data(self, user_data):
        self.full_name_field.click()
        self.full_name_field.fill(user_data["full_name"])
        self.email_field.click()
        self.email_field.fill(user_data["email"])
        self.current_address_field.click()
        self.current_address_field.fill(user_data["current_address"])
        self.permanent_address_field.click()
        self.permanent_address_field.fill(user_data["permanent_address"])
        self.submit_button.click()

    def get_output(self):
        name_output = self.full_name_output.inner_text()
        email_output = self.email_output.inner_text()
        current_address_output = self.current_address_output.inner_text()
        permanent_address_output = self.permanent_address_output.inner_text()
        return locals()
