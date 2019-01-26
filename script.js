let navCloseButton = document.getElementById('nav-close');

// Adding event listeners
// Only add function names to event listeners and define the functions below.
// Avoid defining the function inside the addEventListener method call.
navCloseButton.addEventListener('click', closeNavSideBar);


// Functions START
function closeNavSideBar (){
    let navSideBar = document.querySelector('nav.sidebar');
    navSideBar.classList.add('hide');
}

// Functions END
