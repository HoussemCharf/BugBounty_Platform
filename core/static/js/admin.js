function ban_user(){
	// toggle between badge banned and active
}
function filter(){
      // Please dont play with this code ... -____-
      var input,filter,table,td,textvalue;
      input=document.getElementById('searchField');
      filter=input.value.toUpperCase();
      table=document.getElementById('reportList');
      // i am soo over ; god dam it why everything isnt GOPY
      tr=document.getElementsByClassName('reportList');
      // Looping part
      for (i = 1; i < tr.length; i++) {
          a = tr[i].getElementsByTagName('td')[0];
          // grabbing that text from da ***** (wink wink trump lol)
          txtValue = a.textContent || a.innerText;
          // checking if it matches
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";} 
          else {
              tr[i].style.display = "none";}
      }
    }
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

  //$("[name='switch']").bootstrapSwitch();