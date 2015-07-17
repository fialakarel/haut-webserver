;
$(document).ready(function() {
    
    // takhle lze JS nastavit hodnotu
    $("#teplota").html("--");
    
    // nactenim ajaxem funguje
    /*
        $ *.ajax({
        url: '/temp'
}).done(function( msg ) {
$( "#teplota" ).html( msg );
});
*/
    
    $(".temp_button").live('click',function(){
        //$( "#content" ).html( "<strong>Loading ...</strong>" );
        $.ajax({
            url: '' + "temp"
        }).done(function( msg ) {
            $( "#teplota" ).html( msg );
        });
    });
}); 
