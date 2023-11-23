$(document).on('click', '.readmore', function () {
  $('.hidden').text($(this).prev().text()).removeClass('hidden').addClass('visible')
  $('.hidden_button').removeClass('hidden_button');
  $('.med-article').css({"display": "none"});
});
$('#close').click(function () {
  $('.visible').addClass('hidden').removeClass('visible');
  $('.med-article').css({"display": "block"});
  $('#close').addClass('hidden_button');
});
