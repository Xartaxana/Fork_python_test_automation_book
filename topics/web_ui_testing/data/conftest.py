import pytest


@pytest.fixture
def user_data():
    base_url = "https://demoqa.com/text-box"
    full_name = "Donald Duck"
    email = "donald.duck@example.com"
    current_address = "56 Main St"
    permanent_address = "379 Apple Rd"
    return locals()
