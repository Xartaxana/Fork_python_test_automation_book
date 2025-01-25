import pytest
from ..business.starting_page_object import StartingPage
from ..core.logger import get_logger
from ..data.conftest import user_data
from ..core.browser import page

# Initialize the logger
logger = get_logger(__name__)
logger.info("UI logger initialized successfully!")
logger.info("This is an info message.")
logger.debug("This is a debug message.")


@pytest.mark.ui
def test_text_box(page, user_data):
    logger.debug("Starting log for test_text_box")
    home_page = StartingPage(page)
    home_page.navigate(user_data)
    home_page.fill_user_data(user_data)
    output = home_page.get_output()
    assert user_data["full_name"] in output["name_output"]
    assert user_data["email"] in output["email_output"]
    assert user_data["current_address"] in output["current_address_output"]
    assert user_data["permanent_address"] in output["permanent_address_output"]
    logger.debug("test_text_box successfully passed")
