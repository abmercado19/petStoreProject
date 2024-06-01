# Pet Store Testing Solution

## Setup

### Pre-requisites

- Install Git
- Install Python (Tested with Python 3.9)
- Install pipenv: https://pypi.org/project/pipenv
- Install the solution:
  - Open a command line in a folder where you want to store the testing solution and clone the petStoreProject solution

### Install testing solution dependencies
From root project folder execute the following command: ```pipenv install```

### To execute api tests:

- Ensure the Swagger Petstore Sample server is running. 
    Follow instructions here: https://github.com/swagger-api/swagger-petstore/blob/master/README.md

- Execute the following command:

    ```behave ./api_tests/features -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html```

- Once the execution is finished, you can find the report in reports/behave_report.html

### To execute api tests using tags:

- Each api test has a tag. To execute only the test having a specific tag, execute the following command:

    ```behave ./api_tests/features -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html -t <TAG>```

    where ```<TAG>``` is the tag of the test you want to execute. Eg: @PET
### To execute locust performance tests:

- Ensure the Swagger Petstore Sample server is running. 
    Follow instructions here: https://github.com/swagger-api/swagger-petstore/blob/master/README.md

- Execute the following command:

    ```locust -f ./performance_tests/locustfile.py```

- Click on 'http://0.0.0.0:8089' link in the console to open the Locust web interface
- In the Locust web interface set the following:
  - Number of users: Numbers of users you want to simulate (Eg: 50)
  - Ramp up: Number of users started/second (Eg: 10)
  - Host: http://localhost:8080
- Click on 'Start' button
- Once you want to finish the testing click on Stop button.
- Review the results in the different tabs: Statistics, Charts, Failures, Exceptions, etc.