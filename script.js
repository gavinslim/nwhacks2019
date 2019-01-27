let navSideBar = document.querySelector('nav.sidebar');
let navCloseButton = document.getElementById('nav-close');

// Adding event listeners
// Only add function names to event listeners and define the functions below.
// Avoid defining the function inside the addEventListener method call.
navCloseButton.addEventListener('click', closeNavSideBar);
document.addEventListener('mousemove', peekNavSideBarPopUp);

// Functions START
function closeNavSideBar (){
    navSideBar.classList.add('hide');
    navCloseButton.innerHTML = ">";
}

function peekNavSideBarPopUp(e) {
    if (!navSideBar.classList.contains('hide')) {
        return;
    }
    let mouseX = e.clientX;
    if (mouseX >= 20) {
        if (navSideBar.classList.contains('peek')) {
            navSideBar.classList.remove('peek');
            navSideBar.removeEventListener('click', showNavSideBarPopUp);
        }
    } else {
        if (!navSideBar.classList.contains('peek')) {
            navSideBar.classList.add('peek');
            navSideBar.addEventListener('click', showNavSideBarPopUp);
        }
    }
}

function showNavSideBarPopUp(){
    navCloseButton.innerHTML = "X";
    navSideBar.classList.remove('hide');
    navSideBar.removeEventListener('click', showNavSideBarPopUp);
}

// Functions END
