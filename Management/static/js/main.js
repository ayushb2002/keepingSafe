$(document).ready(function(){
    setTimeout(function(){
        $("#show").css("display", "none");
        $("#hide").css("display", "block");
    }, 3500);

   $(document).scroll(function(){
    $('.fadeIn').each( function(i){
            
        var bottom_of_object = $(this).offset().top + $(this).outerHeight();
        var bottom_of_window = $(window).scrollTop() + $(window).height();
        
        console.log(bottom_of_object+" - "+bottom_of_window);
        /* If the object is completely visible in the window, fade it it */
        if(bottom_of_window > bottom_of_object-500 ){
            
            $(this).animate({'opacity':'1'},500);
                
        }
        
    }); 
   });

    $("#navbtn").draggable({ containment: "parent"});
    $("#navigation").click(function(){
        document.getElementById("mySidebar").style.width = "350px";
        document.getElementById("main").style.marginLeft = "350px";
    });
    $("#cbtn").click(function(){
        document.getElementById("mySidebar").style.width = "0";
        document.getElementById("main").style.marginLeft= "0";
    });
    $("#loginChoice").change(function(){
        choice = $("#loginChoice").val();
        if(choice == 'localUser'){
            $('#localUser').css("display", "block");
            $('#hospStaff').css("display" , "none");
            $('#volunteer').css("display" , "none");
        }
        else if(choice == 'hospStaff'){
            $('#localUser').css("display", "none");
            $('#hospStaff').css("display" , "block");
            $('#volunteer').css("display" , "none");
        }
        else if(choice == 'volunteer'){
            $('#localUser').css("display", "none");
            $('#hospStaff').css("display" , "none");
            $('#volunteer').css("display" , "block");
        }
    });

    $("#addDoc").click(function(){
        $("#docArea").css("display", "block");
        $("#choiceArea").css("display", "none");
        $("#slotArea").css("display", "none");
        $("#viewDocArea").css("display", "none");
        $("#viewSlotArea").css("display", "none");
        $("#appArea").css("display", "none");
    });
    $("#addSlot").click(function(){
        $("#docArea").css("display", "none");
        $("#choiceArea").css("display", "none");
        $("#slotArea").css("display", "block");
        $("#appArea").css("display", "none");
        $("#viewDocArea").css("display", "none");
        $("#viewSlotArea").css("display", "none");
    });
    $("#viewDoc").click(function(){
        $("#docArea").css("display", "none");
        $("#choiceArea").css("display", "none");
        $("#slotArea").css("display", "none");
        $("#appArea").css("display", "none");
        $("#viewDocArea").css("display", "block");
        $("#viewSlotArea").css("display", "none");
    });
    $("#viewSlot").click(function(){
        $("#docArea").css("display", "none");
        $("#choiceArea").css("display", "none");
        $("#slotArea").css("display", "none");
        $("#appArea").css("display", "none");
        $("#viewDocArea").css("display", "none");
        $("#viewSlotArea").css("display", "block");
    });
    $("#checkApp").click(function(){
        $("#docArea").css("display", "none");
        $("#choiceArea").css("display", "none");
        $("#slotArea").css("display", "none");
        $("#appArea").css("display", "block");
        $("#viewDocArea").css("display", "none");
        $("#viewSlotArea").css("display", "none");
    });
    $("#bookApp").click(function(){
        $("#defaultDisp").css("display", "none");
        $("#bookAppDisp").css("display", "block");
        $("#showAppDisp").css("display", "none");
    });
    $("#showApp").click(function(){
        $("#defaultDisp").css("display", "none");
        $("#bookAppDisp").css("display", "none");
        $("#showAppDisp").css("display", "block");
    });
});