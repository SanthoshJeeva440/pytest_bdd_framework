import environment
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import conftest
from pages.login_page import LoginPage
from pages.search_page import SearchPage


@scenario(conftest.feature_path()+'/login.feature', 'Login Hotel App With Valid Username & Password')
def test_login_hotel_app_with_valid_username__password():
    """Login Hotel App With Valid Username & Password."""


@given('Launch Browser')
def test_launch_browser():
    LoginPage(conftest.driver).login_screen()


@when('Enter Username & Password')
def test_enter_username_password():
    LoginPage(conftest.driver).login(environment.USERNAME, environment.PASSWORD)
    
@then('Page Redirect to Search Hotel Page')
def test_page_redirect_to_search_hotel_page():
    SearchPage(conftest.driver).search_hotel_screen()

@then('Logout')
def test_logout():
    SearchPage(conftest.driver).logout()
    SearchPage(conftest.driver).again_login()