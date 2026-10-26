Feature: Authorization
  As a user
  I want to log in to the application
  So that I can access my account

  Background:
    Given the login page is opened

  Scenario: 1. Verify that the username input field is visible
    Then the username input field should be visible

  Scenario: 2. Verify that the password input field is visible
    Then the password input field should be visible

  Scenario: 3. Verify that the login button is visible
    Then the login button should be visible

  Scenario: 4. Verify that the password field is of type password
    Then the password field should be of type password

  Scenario: 5. Verify that the login page has correct title
    Then the page title should be "Playwright"

  Scenario: 6. Verify the placeholder text of the username field
    Then the username placeholder should be "Username"

  Scenario: 7. Verify the placeholder text of the password field
    Then the password placeholder should be "Password"

  Scenario: 8. Verify that the page has a "Log in" button text
    Then the login button text should be "Log in"

  Scenario: 9. Verify that empty form submission doesn't navigate away
    When the user clicks the login button without entering credentials
    Then the user should remain on the login page

  Scenario: 10. Verify that a validation error appears on empty submission
    When the user clicks the login button without entering credentials
    Then the validation error message should be visible
