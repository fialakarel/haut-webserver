;
$(document).ready(function() {
 
    $(".set").live('click',function(){
        $.ajax({
            url: '' + "set?value=" + $(this).attr("id")
        })
    });    
    
    $(".get").live('click',function(){
        id=$(this).attr("id");
        $.ajax({
            url: '' + "get?value=" + $(this).attr("id")
        }).done(function(msg1) {
            $("#" + id).text(msg1)
        });
    });    
    
}); 
