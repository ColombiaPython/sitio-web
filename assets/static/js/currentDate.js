$(document).ready(function () {
  const end_time = $('#check-date').text();
  if (new Date(end_time) > Date.now()) {
    $('#photos-event-dg').remove();
  }
  $('#check-date').remove();
});