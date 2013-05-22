$.mobile.ajaxEnabled = false;
$(document).on("pagebeforecreate", function(){
	var formselector = ".formControls span";
	if ($(formselector ).length == 0){
		formselector = ".formControls";
	}
	if ($(formselector).attr("data-role").length == 0){
		$(formselector).attr("data-role", "controlgroup").attr("data-type", "horizontal");
		$(formselector + " input[type='submit'][name='form.actions.save']").attr("data-theme", "b");
	}
});

$( document ).on( "pageinit", ".page", function() {
	$( document ).on( "swipeleft swiperight", ".page", function( e ) {
		if ( $.mobile.activePage.jqmData( "panel" ) !== "open" ) {
            if ( e.type === "swipeleft"  ) {
            	$( "#panel-right" ).panel( "open" );
            } else if ( e.type === "swiperight" ) {
                $( "#panel-left" ).panel( "open" );
            }
        }
    });
});