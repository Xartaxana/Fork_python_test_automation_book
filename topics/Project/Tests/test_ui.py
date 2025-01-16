import time
import pytest
from topics.Project.Business.guide_page_object import GuidePage
from topics.Project.Business.starting_page_object import StartingPage
from topics.Project.Core.logger import get_logger

# Initialize the logger
logger = get_logger(__name__)
logger.info("UI logger initialized successfully!")
logger.info("This is an info message.")
logger.debug("This is a debug message.")


@pytest.mark.ui
def test_try_it(page):
    logger.debug("Starting log for test_try_it")
    home_page = StartingPage(page)
    home_page.navigate()
    assert home_page.result_textbox_elements.count() == 2
    home_page.get_try_it_result()
    time.sleep(2)  # We are waiting for the elements to appear.
    assert home_page.result_textbox_elements.count() == 17
    logger.debug("test_try_it successfully passed")


@pytest.mark.parametrize(
    "number, expected_text",
    [
        ("1", "/posts/1/comments"),
        ("2", "/albums/1/photos"),
        ("3", "/users/1/albums"),
        ("4", "/users/1/todos"),
        ("5", "/users/1/posts"),
    ],
)
@pytest.mark.ui
def test_names_of_routes(page, number, expected_text):
    logger.debug(f"Starting log for test_try_it (input {number})")
    guid_page = GuidePage(page)
    guid_page.open_guide_page()
    assert guid_page.guide_header.inner_text() == "Guide"
    assert guid_page.get_list_item(number).inner_text() == expected_text
    logger.debug(f"test_try_it (input {number}) successfully passed")
