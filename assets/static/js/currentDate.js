$(document).ready(function () {
  const end_time = $('#check-date').text();
  console.log(new Date(end_time) > Date.now())
});