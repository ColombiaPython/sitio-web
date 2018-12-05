$(document).ready(function () {
  const currentDate = new Date();

  $('.tag-event').each(function () {
    const eventDate = new Date($(this).text());
    
    if ( eventDate > currentDate) {
      $(this).text('Próximo');
    } else {
      $(this).remove();
    }
  });
});