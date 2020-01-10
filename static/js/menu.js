// Open/Close menu on click
$(".hamburger").click(function () {
    checkMenu();
});

// After user scrolls past 150px check if menu is open
$(window).scroll(function () {
    scrollCheck()
})


////////////////////////////////////////
//    Below here there be functions
////////////////////////////////////////



// Checks if the header is visible, if yes -> close it, if no -> open it
function checkMenu() {
    if ($("header").is(":visible")) {
        closeMenu();
    } else {
        openMenu();
    }
}

// Checks only if header is visible, if yes -> close it.
function scrollCheck() {
    if ($("header").is(":visible")) {
        closeMenu();
    }
}

// Open the menu and add active class
function openMenu() {
    $(".hamburger").addClass('is-active');
    $("header").slideDown();
}

// Close the menu and remove active class
function closeMenu() {
    $(".hamburger").removeClass('is-active');
    $("header").slideUp();
}