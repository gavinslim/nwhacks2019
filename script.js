const SERVICE_URL = 'http://localhost:8085/';

let navSideBar = document.querySelector('nav.sidebar');
let navCloseButton = document.getElementById('nav-close');
let dayTab = document.getElementById('day');
let monthTab = document.getElementById('month');
let yearTab = document.getElementById('year');
let cachedData = null;

// Adding event listeners
// Only add function names to event listeners and define the functions below.
// Avoid defining the function inside the addEventListener method call.
navCloseButton.addEventListener('click', closeNavSideBar);
document.addEventListener('mousemove', peekNavSideBarPopUp);
dayTab.addEventListener('click', filterDayData);
monthTab.addEventListener('click', filterMonthData);
yearTab.addEventListener('click', filterYearData);

// Initials Function calls
filterDayData();

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


function filterDayData(){
    // to and from day stamp
    timeFrom = new Date();
    timeTo = new Date();

    // Setting the extremes of the day
    timeFrom.setHours(0,0,0,0);
    timeTo.setHours(11, 59, 59, 0);
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24];
    filterData("Views for the Today", timeFrom=timeFrom, timeTo=timeTo, labels)
}

function filterMonthData(){
    // to and from day stamp
    timeFrom = new Date();
    timeTo = new Date();

    // Setting the extremes of the day
    timeFrom.setHours(0,0,0,0);
    timeFrom.setDate(1)

    timeTo.setHours(11, 59, 59, 0);
    timeTo.setDate(30)

    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];

    filterData("Views for Month", timeFrom, timeTo, labels);

}

function filterYearData(){
    // to and from day stamp
    timeFrom = new Date();
    timeTo = new Date();

    // Setting the extremes of the day
    timeFrom.setHours(0,0,0,0);
    timeFrom.setMonth(0)

    timeTo.setHours(11, 59, 59, 0);
    timeTo.setMonth(11);

    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

    filterData("View for Year", timeFrom, timeTo, labels)
}

function filterData(label, timeFrom, timeTo, labels) {
    cachedData = {};

    let ageFrom = document.querySelector("input[name='min-age']").value;
    let ageTo = document.querySelector("input[name='max-age']").value;

    if ((ageFrom == "" || null) || (ageTo == "" || ageTo == null)) {
        ageFrom = 0;
        ageTo = 999;
    }
    
    let genders = [];
    for (option of document.querySelector('select[name="gender"]').options) {
        if (option.selected === true) {
            genders.push(option.value);
        }
    }
    if (genders.length == 0) {
        genders = null;
    }

    let reactions = [];
    for (option of document.querySelector('select[name="reaction"]').options) {
        if (option.selected === true) {
            reactions.push(option.value);
        }
    }
    if (reactions.length == 0){
        reactions = null;
    }

    let hairColors = [];
    for (option of document.querySelector('select[name="hair-color"]').options) {
        if (option.selected === true) {
            reactions.push(option.value);
        }
    };
    if (hairColors.length == 0){
        hairColors = null;
    }

    let bald = document.querySelector('input[type="checkbox"][name="bald"]').checked;
    
    let mustache = null;
    let beard = null;
    let sideburns = null;
    for (option of document.querySelector('select[name="facial-hair"]').options) {
        if (option.selected) {
            if (option.value == 'mustache') {
                mustache = true;
            } else if (option.value == 'beard') {
                beard = true;
            } else if (option.value == 'sideburns') {
                sideburns = true;
            }
        }
    };


    let glasses = null;
    let eyeMakeup = null;
    let lipMakeup = null;
    
    for (option of document.querySelector('select[name="accessories"]').options) {
        if (option.selected) {
            if (option.value == 'glasses') {
                glasses = true;
            } else if (option.value == 'eyeMakeup') {
                eyeMakeup = true;
            } else if (option.value == 'lipMakeup') {
                lipMakeup = true;
            }
        }
    };


    let foreheadOcclusion = null;
    let mouthOcclusion = null;
    let eyeOcclusion = null;
    
    for (option of document.querySelector('select[name="occlusions"]').options) {
        if (option.selected) {
            if (option.value == 'forehead') {
                foreheadOcclusion = true;
            } else if (option.value == 'eye') {
                eyeOcclusion = true;
            } else if (option.value == 'mouth') {
                mouthOcclusion = true;
            }
        }
    };

    // Building the URL
    params = `from=${formatTime(timeFrom)}&to=${formatTime(timeTo)}&` +
    `age_from=${ageFrom}&age_to=${ageTo}&genders=${JSON.stringify(genders)}&reactions=${JSON.stringify(reactions)}&` + 
    `mustache=${mustache}&beard=${beard}&hair_colors=${JSON.stringify(hairColors)}&bald=${bald}&` +
    `glasses=${glasses}&eye_makeup=${eyeMakeup}&lip_makeup=${lipMakeup}&` +
    `forehead_occlusion=${foreheadOcclusion}&mouth_occlusion=${mouthOcclusion}&` + 
    `eye_occlusion=${eyeOcclusion}`;
    url = `${SERVICE_URL}?${params}`;

    console.log(url)

    // Getting the DATA
    get(url, (json) => {
        showChart(label, labels, json);
    })
}

function get(url, cb) {
    fetch(url)
        .then((res) => {
            return res.json()
        })
        .then((data) => {
            cb(data);
        })

}

function showChart(label, labels, data) {    
    data.forEach((item) => {
        let hour = new Date(item['timestamp']).getHours();
        if (cachedData[hour] === undefined) {
            cachedData[hour] = []
        }
        cachedData[hour].push(item);
    });

    data = [];
    Object.keys(cachedData).forEach((key) => {
        data.push(cachedData[key].length);
    });

    let ctx = document.getElementById('myChart').getContext('2d');
    let chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: labels,
        datasets: [{
            label: label,
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 252)',
            data: data
        }]
    },

    // Configuration options go here
    options: {}
});
}

function formatTime(date){
    return date.getFullYear() + '-' + (date.getMonth()+1) + '-' + date.getDate() + ' '
        + date.getHours() + ':'
        + date.getMinutes() + ':'
        + date.getSeconds() + '.'
        + date.getMilliseconds();
}
// Functions END
