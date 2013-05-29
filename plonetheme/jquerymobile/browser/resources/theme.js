$.mobile.ajaxEnabled = false;
$(document).on("pagebeforecreate", function(){
	/*
	 * This function make formcontrols actions look nice in jqm
	 * */
	var formselector = ".formControls span";
	if ($(formselector ).length == 0){
		formselector = ".formControls";
	}
	if ($(formselector).length != 0){
		var attr = $(formselector).attr("data-role");
		$(formselector).attr("data-role", "controlgroup").attr("data-type", "horizontal");
		var actionsNames = ["form.actions.save", "form.button.Publish", "form.buttons.comment"];
		for (var i = 0; i < actionsNames.length; i++) {
			console.log(formselector + " input[type='submit'][name='"+actionsNames[i] + "']");
			$(formselector + " input[type='submit'][name='"+actionsNames[i] + "']").attr("data-theme", "b");
		}
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