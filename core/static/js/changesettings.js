
    $(document).ready(function() {

  $('#form2').on('submit', function(event) {

    $.ajax({
      data : {
        currentpassword: $('#InputcurrentPassword').val(),
        Newpassword:$('#InputNewPassword').val(),
        ConfirmNewpassword:$('#InputConfirmPassword').val()
      },
      type : 'POST',
      url : '/settings'
    })
    .done(function(data) {

      if (data.success) {
        $('#form2').trigger("reset");
        $('#successAlert1').text(data.success).fadeIn();
        setTimeout(function(){  
        $('#successAlert1').fadeOut("Slow");  
        }, 2000);
        $('#errorAlert1').hide();
      }
      else {
        $('#errorAlert1').text(data.error).show();
         setTimeout(function(){  
        $('#errorAlert1').fadeOut("Slow");  
        }, 2000);
        $('#successAlert1').hide();
        }

    });

    event.preventDefault();

  });

});