# Conduit App - Test Automation
#### Python - Selenium - Pytest

This repository contains Automated Web UI Tests for [Conduit React App](https://react-redux.realworld.io/).
The tests have been implemented using Python, Selenium, and Pytest. The test scenarios covered are:  
1. Signing In (with valid/invalid credentials)
2. Creating a new article/post.
3. Verifying the details of the newly created article.

Total Tests: 8

### Environment Setup
1. Download and install Python 3 from [here](https://www.python.org/downloads/). For Windows users, make sure to check the 'Add Python to Path' box during the setup.
2. Download the repository files.
3. Open a terminal/Command Prompt and cd into 'Conduit_Test_Project' directory:  
    `cd path-to-Conduit_Test_Project-directory`
4. Run the command (requires administrator/root privileges and an internet connection):  
   + Windows Users should run command prompt as Administrator and enter:  
   `pip3 install -r requirements.txt`
   + Linux/Mac users should enter:  
   `sudo pip3 install -r requirements.txt`
5. To run the tests, you will need to supply valid Conduit App credentials to the command-line. Please make sure that you have valid credentials to sign into the Conduit App.


### Executing Tests
1. Open a terminal/Command Prompt and cd into the Conduit_Test_Project directory.
  

2. To run all the tests, execute the command  
   `pytest --email your_registered@email.com --password your_password` (will execute in Firefox browser by default)  
    **Note: You will need to provide the email and password only when you run the tests for the first time. Or when you wish to change the credentials.**
  

3. To run only the smoke tests, use the switch, -m:  
      `pytest -m smoke`  
  

4. To run the tests in Google Chrome browser, use the switch, --browser:  
   `pytest --browser=chrome`
  

5. To run multiple tests in parallel, use the switch, -n. For example, to run 3 tests in parallel in Chrome at a time, use the command:  
   `pytest --browser chrome -n 3`
  

6. To run the tests on Selenium grid, use the switch --browser=grid or --browser=cloud-chrome to run the tests in chrome on grid.  
    You will also need to supply in the grid hub url via --gridhub switch if not using the default url.  
   `pytest -n 4 --browser grid --gridhub http://localhost:4444/wd/hub`
  

7. To generate an HTML report, use the switch, --html:  
   `pytest -n 5 --html report.html`

### Test Artifacts
Everytime test(s) are executed using the pytest command, a separate folder bearing a timestamp is created for that test-run inside TestRuns\ directory. All the logs, screenshots and test report generated during the test-run can be found in this directory.

## Framework Features
- Modular
    - Web Pages have been represented through a Page Object Model (POM).
    - No webdriver api in actual tests. Tests are created by only using aptly named functions. API is restricted to pages and elements classes.
    - Intuitive folder structure that keeps various aspects of the framework organized

- Automatic screenshot capture
    - The framework is intelligent enough to determine if a test has failed and automatically takes a screenshot on failure.
    - Also, an api has been provided to easily take full page screenshots with a predefined file name format.

- Hassle-free Webdriver Management
    - The framework automatically handles the driver dependencies for all the browsers.
    - No need to download and specify new drivers when you update your browsers. It will automatically download (and cache it) all the required webdriver files for the installed browser version.

- Reporting
    - A separate folder with timestamp is created for each test run containing logs, screenshots and an HTML report.
    - An HTML report can easily be generated that summarises passes, failures, logs, time taken by each test etc.

- Selenium Grid Integration
    - Tests can be run on any number of instances of different browsers connected through Selenium Grid

- Integration with CI/CD (Jenkins, Git, Docker)
    - Integrated with an example Jenkins Pipeline
    - The tests have been containerized to enable seemless execution from anywhere. Docker file is included.
    - Tests can also be executed on containerized instances of browsers connected to Selenium Grid.
