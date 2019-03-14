function ban_user(){
	// toggle between badge banned and active
}
$('#switch').bootstrapSwitch();
function toggle_tabs(target){
    var dashboard,userboard,reportboard,title;
    title= document.getElementById('Tab');
    dashboard = document.getElementById('content1');
    userboard = document.getElementById('content2');
    reportboard = document.getElementById('content3');
    settings = document.getElementById('content4');
    if (target=="user"){
      title.textContent="Users";
      dashboard.style.display="none";
      reportboard.style.display="none";
      userboard.style.display="";
      settings.style.display="none";
    }
    else if (target=="dash"){
      title.textContent="Dashboard";
      dashboard.style.display="";
      reportboard.style.display="none";
      userboard.style.display="none";
      settings.style.display="none";

    }
    else if (target=='settings'){
      title.textContent="Settings";
      dashboard.style.display="none";
      reportboard.style.display="none";
      userboard.style.display="none";
      settings.style.display="";
    }
    else{
      title.textContent="Reports"
      dashboard.style.display="none";
      reportboard.style.display="";
      userboard.style.display="none";
      settings.style.display="none";
    }
  }