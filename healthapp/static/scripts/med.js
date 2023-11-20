$(document).on('click', '.readmore', function () {
  $('.hidden').text($(this).prev().text()).removeClass('hidden').addClass('visible')
  $('.hidden_button').removeClass('hidden_button');
  $('.med-article').css({"visibility": "hidden"});
});
$('#close').click(function () {
  $('.visible').addClass('hidden').removeClass('visible');
  $('.med-article').css({"visibility": "visible"});
  $('#close').addClass('hidden_button');
});
