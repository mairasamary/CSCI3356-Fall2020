var open = document.querySelector('#open_system_buttom')
var close = document.querySelector('#close_system_buttom')


// On Click
open.addEventListener("click",function(){
  open.textContent = "Clicked On";
  open.style.color = 'blue';
  var openPressed = true;
  console.log(openPressed);
})

close.addEventListener("click",function(){
  close.textContent = "Clicked On";
  close.style.color = 'blue';
  var closePressed = true;
  console.log(closePressed);
})

// function change_system_status($this){
//     console.log("button clicke");
//     var request_data = $this.id;
//     console.log("data: " +request_data);
//     $.ajax({
//         url: "change_system_status/",
//         data : {request_data: request_data},
//         success : function(json) {
//             $("#request-access").hide();
//             console.log("requested access complete");
//         }
//     })
// }
