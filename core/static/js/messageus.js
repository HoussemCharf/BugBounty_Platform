
    $(document).ready(function() {

  $('#form1').on('submit', function(event) {

    $.ajax({
      data : {
        messageContent: $('#ContentInput').val()
      },
      type : 'POST',
      url : '/contactus'
    })
    .done(function(data) {

      if (data.success) {
        $('#successAlert').text(data.success).fadeIn();
        setTimeout(function(){  
        $('#successAlert').fadeOut("Slow");  
        }, 2000);
        $('#errorAlert').hide();
      }
      else {
        $('#errorAlert').text(data.error).show();
         setTimeout(function(){  
        $('#errorAlert').fadeOut("Slow");  
        }, 2000);
        $('#successAlert').hide();
        }

    });

    event.preventDefault();

  });

});