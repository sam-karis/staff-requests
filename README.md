# Staff Expense Requests Application
This is a simple application where staffs request for expenses like transport, accommodation fee, subsistence and stationery . The request goes through two approvals , a line manager and HR manager. Then an email is send to requester once the two approvals are done.

## Key Application features

> - Register admin through terminal
> - Create employee roles by admin
> - Add employees by admin only
> - Log in employees
> - Add expense categories by Admin
> - Make expense request by employee
> - View all expense requests submitted by a specific employee
> - View all requests by all employees by Admin only
> - Approve or Disapprove request by Line and HR manager
> - View users tickets
> - View count of tickets in a flight on a specific day

## Development set up

- Check that python 3 is installed:

  ```
  python --v
  >> Python 3.7.4
  ```

- Install virtualenv:

  ```
  pip install virtualenv
  ```

- Check pipenv is installed:

  ```
  virtualenv --version
  >> 16.2.0
  ```

- Check that postgres is installed:

  ```
  postgres --version
  >> postgres (PostgreSQL) 11.4

  ```

- Clone the airtech repo and `cd`` into it:

  ```
  git clone https://github.com/sam-karis/staff-requests.git

  ```

- Create and activate the virtualenv:

  ```
  virtualenv virtualenv && source virtualenv/bin/activate
  ```

- Install dependencies:

  ```
  pip install -r requirements.txt
  ```

- Rename the .env_example file to .env and update the variables accordingly:

  ```
    export SECRET_KEY=<secret_key>
    export DATABASE_URL=postgresql://postgres@<host>:<port>/<db_name>
    export EMAIL_HOST='smtp.gmail.com'
    export EMAIL_USE_TLS=True
    export EMAIL_PORT=587
    export EMAIL_HOST_USER=<your_email_account>
    export EMAIL_HOST_PASSWORD=<email_password>
    export DEFAULT_FROM_EMAIL=<your_email_account>
  ```

- Create database

  ```
  createdb <db_name> # if you have psql installed
  ```

- Apply Migrations:

  ```
  python manage.py migrate
  ```

- Create admin
  ```
  python manage.py createsuperuser
  ```

* Run the application:

  ```
  python manage.py runserver
  ```

* Should you make changes to the database models, run migrations as follows

  ```
  python manage.py makemigration # when you create models or changes are made to existing model
  python manage.py migrate  # applying changes to the database
  ```

* Run tests

  ```
  tox # run all the tests and flake8
  flake8 # check if clean conventions have been followed
  pytest # run tests
  pytest --cov  # test coverage
  ```

* Deactivate the virtual environment once you're done:
  ```
  deactivate
  ```

## Running the API

Manually Test the endpoints with postman

[![Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/4000258/SW17RaWU?version=latest)

| **EndPoint**                                  | **Functionality**             |
| --------------------------------------------- | --------------------------    |
| POST `/api/v1/auth/add/`                      | Add an employee by admin      |
| POST `/api/v1/auth/login/`                    | login user                    |
| POST `/api/v1/auth/addrole`                   | Add employee roles            |
| POST `/api/v1/requests/category`              | Add expense category by admin |
| GET `/api/v1/requests/category`               | Get expense category by admin |
| POST `/api/v1/requests/staffs`                | Make expense request          |
| GET `/api/v1/requests/staffs`                 | Get all your expense request  |
| GET `/api/v1/requests/allstaffs`              | Get all requests by admin     |
| POST `/api/v1/requests/approve/<request_id>`  | Approve/Disapprove a request  |
| GET `/admin`                                  | Admin Dashboard               |
