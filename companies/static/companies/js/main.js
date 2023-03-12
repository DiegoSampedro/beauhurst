$(document).ready(function() {
    $.get("/companies/stats/", function(data) {
        const $recentlyFoundedContainer = $('#most-recently-founded');
        for (const company of data.most_recently_founded) {
            const $el = '<tr><td>' + company.name + '</td></tr>';
            $recentlyFoundedContainer.append($el);
        }

        $("#average-employee-count").text(data.average_employee_count);

        const $foundedPerQuarterContainer = $('#founded-per-quarter');
        for (const entity of data.companies_founded_per_quarter) {
            const $el = '<tr><td>' + entity.year + '</td><td>' + entity.quarter + '</td><td>' + entity.count + '</td></tr>';
            $foundedPerQuarterContainer.append($el);
        }

        $("#user-with-most-companies").text(data.user_created_most_companies);

        $("#user-with-most-employees").text(data.user_created_most_employees);

        const $avgDealBycountryContainer = $('#avg-deal-by-country');
        for (const entity of data.average_deal_amount_raised_by_country) {
            const $el = '<tr><td>' + entity.country + '</td><td>' + entity.avg_amount_raised + '</td></tr>';
            $avgDealBycountryContainer.append($el);
        }
    });
});