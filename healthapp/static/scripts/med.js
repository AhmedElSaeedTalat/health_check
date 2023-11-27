$(document).on('click', '.readmore', function () {
  $('.hidden').text($(this).prev().text()).removeClass('hidden').addClass('visible');
  $('.hidden_button').removeClass('hidden_button');
  $('.med-article').css({"display": "none"});
});
$('#close').click(function () {
  $('.visible').addClass('hidden').removeClass('visible');
  $('.med-article').css({"display": "block"});
  $('#close').addClass('hidden_button');
});

// function to show diagnosis when symptoms are selected
$('.form-symptoms button').click(function(e){
  e.preventDefault();
  // get data from form
  const date_birth = $('#age').val();
  if (date_birth == "") {
    $('#birth_warning').css({'display': 'block'});
    return;
  } else {
    $('#birth_warning').css({'display': 'none'});
  }
  const date = new Date(date_birth)
  const year = date.getFullYear()
  const gender = $('#gender').val()
  const symptoms = []
  $('#select_options option:selected').each(function(){
  symptoms.push($(this).attr('idvalue'))
  });
  if (symptoms.length == 0) {
    $('#symptom_warning').css({'display': 'block'});
    return;
  } else {
    $('#symptom_warning').css({'display': 'none'});
  }
  data = {
    year: year,
    gender: gender,
    symptoms: symptoms
  }
  // request diagnosis - api to back end
  fetch("/medicines/diagnosis", {
    method: "POST",
    headers: {
    "Content-Type": "application/json",
    },
    body: JSON.stringify(data)
  }).then(r => r.text()).then(data => {
    if (data === 'failed') {
		$('.request_error').css({'display': 'block'});
		return;
	}
    data = JSON.parse(data);
    if (data.length > 0) {
      $('.diagnosis').css({'display': 'block'});
      $('#close_diagnosis').css({'display': 'block'});
      $('.form-symptoms').css({'display': 'none'});
      $('.img').css({'display': 'none'});
      // empty populated div incase it was full befor request
      $('#diagnosis_content').empty()
      $('#specialisation').empty()
      const list_diagnosis = []
      for (let i = 0; i < data.length; i++) {
        $('#diagnosis_content').append(`<li>${data[i]['Issue'].ProfName} </li>`);
        for (let y = 0; y < data[i]['Specialisation'].length; y++) {
			if (list_diagnosis.indexOf(data[i]['Specialisation'][y].Name) >= 0 ){
				continue;
		    } else {
              list_diagnosis.push(data[i]['Specialisation'][y].Name)
              $('#specialisation').append(`<li>${data[i]['Specialisation'][y].Name} </li>`);
			}
        }
      }
    } else {
      // if no diangosis for symtom
      $('.no_diagnosis').css({'display': 'block'});
    }
  })
  $('.form-symptoms form')[0].reset();
})
// click event to close opened tab for diagnosis
$('#close_diagnosis').click(function() {
  $('.diagnosis').css({'display': 'none'});
  $('#close_diagnosis').css({'display': 'none'});
  $('.form-symptoms').css({'display': 'block'});
  $('.img').css({'display': 'block'});
});

// show load image when form subimtted
$('.searchme_drug').click(function () {
  $('.load_img').css({'display': 'block'});
});


// add the animate rotatin to logo when loading in search page
$('.search .btn').click(function() {
	$('.logo_searchPage').animate(
		{deg: 180},
		{
			duration: 1200,
			step: function(now) {
				$(this).css({ transform: 'rotateY(' + now + 'deg)' });
			}
		}
	)
});


// get list of drugs when hovered over the clicked button
let response;
$('#my_drugs').on("mouseover", function() {
  if (response) {
    $('.list_drugs').css({"display": "block"});
    return
  }
  $.get("/user/saved-drug", function (data, textSatus){
    response = data
    for (let i = 0; i < data.length; i++) {
      $('.list_drugs').append(`<li>${data[i]}</li>`)
    }
  });
});

// hide list of drugs when not hovered over the button
$('#my_drugs').mouseout(function() {
	$('.list_drugs').css({"display": "none"});
});
// request data of clicked drug from the list
// and redirect to another page with the data
$('.list_drugs').on('click', 'li', function() {
  const search_data = $(this).text();
	fetch("/medicines/drug-deatails", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({name: search_data})
	}).then(r => r.text()).then(data => {
	  if (data == 'success') {
		  window.location.replace("/medicines/display-med");
	  } else {
		  alert('cant obtain data at the moment')
	  }
	})
});

// send a request on click to save a drug name on db
// based on name of drug clicked on, if success received
// alert is sent
$('.save_drug').click(function() {
    const name = $('#drug_name').val()
	fetch("/medicines/save-drug", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
	  },
	  body: JSON.stringify(name)}).then(res => res.text()).then(data => {
			if (data == "success") {
				alert('successfully added the drug to list of faviourite')
				$('.save_drug').css({'display': 'none'})
			}
	  });
});
