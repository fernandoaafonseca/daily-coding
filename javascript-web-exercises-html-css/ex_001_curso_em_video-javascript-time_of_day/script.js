function loadBody() {
  let { greetingTxtElement, imgElement, timeTxtElement } = getPageElements()
  let { rawHours, rawMinutes } = getCurrentTime();
  let timeOfDay = getTimeOfDay(rawHours);
  let ampm = formatAMPM(rawHours)
  let { hours, minutes } = formatTime(rawHours, rawMinutes)
  let imgPath = getImgPath(timeOfDay);
  setTimeColors(timeOfDay);
  setTimeTxt(timeTxtElement, ampm, hours, minutes);
  setImg(imgElement, imgPath);
  setGreetingTxt(greetingTxtElement, timeOfDay);
}

function getPageElements() {
  let greetingTxtElement = document.getElementById('greeting-txt');
  let imgElement = document.getElementById('time-img');
  let timeTxtElement = document.getElementById('time-txt');
  return {
    greetingTxtElement: greetingTxtElement,
    imgElement: imgElement,
    timeTxtElement: timeTxtElement
  }
}

function getCurrentTime() {
  let date = new Date();
  let rawHours = date.getHours();
  let rawMinutes = date.getMinutes();
  return {
    rawHours: rawHours,
    rawMinutes: rawMinutes
  }
}

function getTimeOfDay(hours) {
  let timeOfDay;
  if (hours >= 6 && hours < 12) {
    timeOfDay = 'morning';
  }
  else if (hours >= 12 && hours < 18) {
    timeOfDay = 'afternoon';
  }
  else {
    timeOfDay = 'night';
  }
  return timeOfDay
}

function formatAMPM(hours) {
  let ampm;
  if (hours < 12) {
    ampm = 'a.m';
  }
  else {
    ampm = 'p.m';
  }
  return ampm;
}

function formatTime(rawHours, rawMinutes) {
  let hours;
  let minutes;
  rawHours = rawHours % 12;
  if (rawHours == 0) {
    hours = 12;
  }
  else {
    hours = rawHours;
  }
  if (rawMinutes <= 9) {
    minutes = '0' + rawMinutes;
  }
  else {
    minutes = rawMinutes;
  }
  return {
    hours: hours,
    minutes: minutes
  }
}

function getImgPath(timeOfDay) {
  const IMG_MORNING = 'imgs/morning.png';
  const IMG_AFTERNOON = 'imgs/afternoon.png';
  const IMG_NIGHT = 'imgs/night.png';
  let imgPath;
  if (timeOfDay == 'morning') {
    imgPath = IMG_MORNING
  }
  else if (timeOfDay == 'afternoon') {
    imgPath = IMG_AFTERNOON;
  }
  else {
    imgPath = IMG_NIGHT;
  }
  return imgPath
}

function setTimeColors(timeOfDay) {
  const BG_COLOR_MORNING = '#D9BD1A'
  const BG_COLOR_AFTERNOON = '#D97F45'
  const BG_COLOR_NIGHT = '#1F4E8C';
  const SECTION_COLOR_MORNING = '#DFD391'
  const SECTION_COLOR_AFTERNOON = '#DFAC8A';
  const SECTION_COLOR_NIGHT = '#3079D9'
  let bodyStyle = document.body.style;
  let mainSection = document.getElementById('main-section');
  if (timeOfDay == 'morning') {
    bodyStyle.backgroundColor = BG_COLOR_MORNING;
    mainSection.style.backgroundColor = SECTION_COLOR_MORNING;
  }
  else if (timeOfDay == 'afternoon') {
    bodyStyle.backgroundColor = BG_COLOR_AFTERNOON;
    mainSection.style.backgroundColor = SECTION_COLOR_AFTERNOON;
  }
  else {
    bodyStyle.backgroundColor = BG_COLOR_NIGHT;
    mainSection.style.backgroundColor = SECTION_COLOR_NIGHT;
  }
}

function setGreetingTxt(greetingTxtElement, timeOfDay) {
  let greetingTxt = `Good ${timeOfDay}!`;
  greetingTxtElement.textContent = greetingTxt;
}

function setImg(imgElement, imgPath) {
  imgElement.src = imgPath;
}
function setTimeTxt(timeTxtElement, ampm, hours, minutes) {
  let timeTxt = `It's ${hours}:${minutes} ${ampm}.`;
  timeTxtElement.textContent = timeTxt;
}
