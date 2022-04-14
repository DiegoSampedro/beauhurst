# Technical Assessment

We've included a tiny Django web app which is a wiki(-ish) of UK companies and
their employees. There's currently no front end views, and everything is getting
created, updated and deleted through the admin.

We want you to extend this app by implementing some of the changes outlined below. Pick the ideas that interest you most and allow you to demonstrate your skills.

It would be good to see some evidence of both backend and frontend work and some examples of handling more complex logic. Feel free to make any other changes or improvements that you think are necessary: the rest is up to you.

### Ideas

1. Create an API end point which allows authenticated users (no need to handle
API keys, just assume they're logged in) to pass in the id of a company to
monitor.
2. Create an API end point which allows authenticated users to see which
companies they're currently monitoring.
3. Create an unauthenticated API end point which returns:
    * The 10 most recently founded companies
    * Breakdown of number of companies founded per quarter for the last five years
    * Average employee count
    * User who has created the most companies
    * User with the greatest total number of employees at all companies they have created
    * Average deal amount raised by country (i.e. deals for companies in those countries)
4. Create a frontend interface to this API, displaying and visualising these stats. You can build this however you like - see the `company_stats.html` template for a very basic prototype.

## Expectations

- Please use Git to record the changes you make.
- We would appreciate it if you did not publish this assessment on public
  repositories.
- To submit just send us back a zip containing the repository (including the `.git` directory) or share it as a private repository with us on Github

## Installation

1. Clone the repo
2. Install python: we recommend `pyenv`
    ```
    curl https://pyenv.run | bash
    pyenv install 3.9.5
    pyenv local 3.9.5
    ```
3. Set up a virtual env or equivalent to isolate your environment: we recommend `pipenv`
    ```
    python -m pip install -U pipenv
    pipenv install -r requirements.txt
    pipenv shell
    ```
4. `./manage.py migrate`
5. `./manage.py loaddata assessment/fixtures.json` or `./manage.py populate_database`
6. `./manage.py createsuperuser`
7. `./manage.py runserver 0.0.0.0:8000`

## Testing

If testing is your thing, then 👍 we've set this repo up so you can use Django's builtin `unittest` or `pytest`, and we've set up `factory_boy` to help with some of the boilerplate to get you started.

## References

- https://virtualenvwrapper.readthedocs.io
- https://docs.djangoproject.com/en/1.11/topics/testing/
- https://docs.pytest.org
- https://pytest-django.readthedocs.io
- https://faker.readthedocs.io
- http://flake8.pycqa.org
