Django web app which is a wiki(-ish) of UK companies and their employees.

1. Created an API end point which allows authenticated users to pass in the id of a company to monitor.
2. Created an API end point which allows authenticated users to see which companies they're currently monitoring.
3. Created an unauthenticated API end point which returns:
    * The 10 most recently founded companies
    * Breakdown of number of companies founded per quarter for the last five years
    * Average employee count
    * User who has created the most companies
    * User with the greatest total number of employees at all companies they have created
    * Average deal amount raised by country (i.e. deals for companies in those countries)
4. Created a frontend interface to this API, displaying and visualising these stats. You can build this however you like - see the `company_stats.html` template for a very basic prototype.
