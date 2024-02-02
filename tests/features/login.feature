Feature: Login Hotel Web App

    Background: Im on the login page

    Scenario: Login Hotel App With Valid Username & Password
        Given Launch Browser
        When Enter Username & Password
        Then Page Redirect to Search Hotel Page
        And Logout

    # Scenario: Login Hotel App With Invalid Username & Password
    #     Given Page Redirect To Home Page
    #     When Enter Invalid Username & Password
    #     Then Page Should Not Redirect To Search Hotel Page