$(document).ready(function() {
    $.get("/companies/stats/", function(data) {
        $("#most-recently-founded").text(data.most_recently_founded[0].name);
        $("#average-employee-count").text(data.average_employee_count);
    });
});