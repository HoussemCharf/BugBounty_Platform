  var timeout = setInterval(reloadChat, 10000);    
  function reloadChat () {

     $('#reloadChat').load(window.location.href + " #reloadChat");
    }