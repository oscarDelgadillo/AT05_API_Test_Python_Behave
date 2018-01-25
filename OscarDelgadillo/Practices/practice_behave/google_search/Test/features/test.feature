Feature: Testing google main page
This is for practice

Scenario: When made a search should display a list of results
Given I navigate to google main page
When I enter the word "computer" for search
Then it should display a list of result related with the word "computer"

Scenario: When made a search using the keyword asterisk should be take like a wildcard
* I navigate to google main page
    and login with valid credentials
* I enter the word "com*uter" for search
* it should display a list of result related with the word "computer"

Scenario: When made a search using pictures with extension jpg should display a list of results
Given I navigate to google main page
    And go to images link
When I upload any image with the extension jpg
Then it should display a list of results related with the image

