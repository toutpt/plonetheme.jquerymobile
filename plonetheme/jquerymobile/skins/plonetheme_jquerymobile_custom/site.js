

// Show a specific submenu UL
function showSubMenus(menu_id) {
  $("#site_globalnav_submenu ul").each(function(index, elem) { $(elem).css('display', 'none'); });
  selected_submenu = $(menu_id);
  selected_submenu.css('display', 'block');
}

// After the page is loaded
$(document).ready(function() {
  
  // Menu navigation: menus and submenus
  $("#site_globalnav li").hover(
    function () {
      // onmouseover
      var selected_menu = $(this);
      
      // Add the class "selected" only on this element
      $("#site_globalnav li").each(function(index, elem) { $(elem).removeClass("selected"); });
      selected_menu.addClass("selected");
      
      // Show the corresponding submenu listing
      showSubMenus('#' + selected_menu.attr('id') + '-subsection');
    },
    function () {
      // onmouseout
      // $(this).removeClass("selected");
    }
  );
  
  // Show the current corresponding submenu
  showSubMenus('#' + $('#site_globalnav li.selected').attr('id') + '-subsection');

});

