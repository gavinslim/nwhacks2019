const SERVICE_URL = 'http://localhost:8085/';

let navSideBar = document.querySelector('nav.sidebar');
let navCloseButton = document.getElementById('nav-close');
let dayTab = document.getElementById('day');
let monthTab = document.getElementById('month');
let yearTab = document.getElementById('year');
let cachedData = null;
let canvasParent = document.getElementById('chart-container');

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
function closeNavSideBar() {
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

function showNavSideBarPopUp() {
    navCloseButton.innerHTML = "X";
    navSideBar.classList.remove('hide');
    navSideBar.removeEventListener('click', showNavSideBarPopUp);
}


function filterDayData() {
    // to and from day stamp
    timeFrom = new Date();
    timeTo = new Date();

    // Setting the extremes of the day
    timeFrom.setHours(0, 0, 0, 0);
    timeTo.setHours(11, 59, 59, 0);
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24];
    filterData("Views for the Today", timeFrom = timeFrom, timeTo = timeTo, labels, 'day');
}

function filterMonthData() {
    // to and from day stamp
    timeFrom = new Date();
    timeTo = new Date();

    // Setting the extremes of the day
    timeFrom.setHours(0, 0, 0, 0);
    timeFrom.setDate(1)

    timeTo.setHours(11, 59, 59, 0);
    timeTo.setDate(30)

    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];

    filterData("Views for Month", timeFrom, timeTo, labels, 'month');

}

function filterYearData() {
    // to and from day stamp
    timeFrom = new Date();
    timeTo = new Date();

    // Setting the extremes of the day
    timeFrom.setHours(0, 0, 0, 0);
    timeFrom.setMonth(0)

    timeTo.setHours(11, 59, 59, 0);
    timeTo.setMonth(11);

    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

    filterData("View for Year", timeFrom, timeTo, labels, 'year')
}

function filterData(label, timeFrom, timeTo, labels, unit_type) {
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
    if (reactions.length == 0) {
        reactions = null;
    }

    let hairColors = [];
    for (option of document.querySelector('select[name="hair-color"]').options) {
        if (option.selected === true) {
            reactions.push(option.value);
        }
    };
    if (hairColors.length == 0) {
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
        showChart(label, labels, json, unit_type);
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

function showChart(label, labels, data, unit_type) {
    data.forEach((item) => {
        let unit = new Date(item['timestamp']);
        if (unit_type == 'day') {
            unit = unit.getHours();
        } else if (unit_type == 'month') {
            unit = unit.getDate();
        } else if (unit_type == 'year') {
            unit = unit.getMonth();
        }
        debugger;
        if (cachedData[unit] === undefined) {
            cachedData[unit] = []
        }
        cachedData[unit].push(item);
    });

    // debugger;
    data = [];
    Object.keys(cachedData).forEach((key) => {
        data.push(cachedData[key].length);
    });

    // Creates new canvas each time.
    for (el of document.querySelectorAll('iframe')) {
        el.remove();
    }
    document.getElementById('myChart').remove();
    let canvas = document.createElement('canvas');
    canvas.id = 'myChart';
    canvasParent.appendChild(canvas);

    let ctx = document.getElementById('myChart').getContext('2d');
    let prev_config = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 252)',
                data: data
            }]
        },
        options: {
            events: ['click']
        }
     }
    let chart = new Chart(ctx, prev_config);
    document.getElementById('myChart').addEventListener('click', function(e){
        index = chart.getElementAtEvent(e)[0]['_index'];
        let dataSet = cachedData[index];
        if (dataSet == undefined) {
            index = 0;
            dataSet = cachedData[index];
        }
        while (dataSet === undefined) {
            index++;
            dataSet = cachedData[index];
        }
        showDetailChart(dataSet);
    })
}

function showDetailChart(dataSet){
    let ctx = document.getElementById('myChart').getContext('2d');
    
    let males = 0;
    let females = 0;

    let positive = 0;
    let negative = 0;
    let neutral = 0;
    
    let blondes = 0;
    let redHair = 0;
    let blackHair = 0;
    let brownHair = 0;
    let grayHair = 0;
    let otherHair = 0;

    let glasses = 0;
    let eyeMakeup = 0;
    let lipMakeup = 0;

    let mustache = 0;
    let beard = 0;
    let eyeOccluded = 0;
    let mouthOccluded = 0;
    let foreheadOccluded = 0;

    for (item of dataSet) {
        switch (item['gender']) {
            case 'male': males++; break;
            case 'female': females++; break;
        }

        switch(item['hair']['color']) {
            case 'blonde': blondes++; break;
            case 'gray': grayHair++; break;
            case 'red': redHair++; break;
            case 'brown': brownHair++; break;
            case 'black': blackHair++; break;
            case 'other': otherHair++;
        }

        switch(item['reaction']) {
            case 'positive': positive++; break;
            case 'negative': negative++; break;
            case 'neutral': neutral++; break;
        }

        if (item['facial_hair']['mustache'])
            mustache++;
        
        if (item['facial_hair']['beard'])
            beard++;

        if (item['makeup']['eyeMakeup']) {
            eyeMakeup++;
        }
        if (item['makeup']['lipMakeup'])
            lipMakeup++;
       
        if (item['accessories']['glasses'])
            glasses++;
        
        if (item['occlusion']['foreheadOccluded'])
            foreheadOccluded++;
        
        if (item['occlusion']['eyeOccluded']) 
            eyeOccluded++;
        
        if (item['occlusion']['mouthOccluded'])
            mouthOccluded++;
    }

    let stackedBar = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Gender', 'Reaction', 'Hair Color', "Facial Hair", "Makeup", "Occlusions"],
            datasets: [
                {
                    label: 'Male',
                    data: [males],
                    backgroundColor: 'red'
                }, {
                    label: 'Female',
                    data: [females],
                    backgroundColor: 'green'
                }
            ]
        },
        options: {
            scales: {
                xAxes: [{
                    stacked: true
                }],
                yAxes: [{
                    stacked: true
                }]
            }
        }
    });
}

function formatTime(date) {
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() + ' '
        + date.getHours() + ':'
        + date.getMinutes() + ':'
        + date.getSeconds() + '.'
        + date.getMilliseconds();
}
// Functions END
