function transformInfo(title, meetups) {
  let list = ``;
  const icon = {
    'python': '/static/map/icons/python.png',
    'pyladies': '/static/map/icons/pyladies.png',
    'pydata': '/static/map/icons/pydata.png'
  }

  for (meetup in meetups) {
    list += `<li><a href=` + meetups[meetup].url + ` target="blank_" ><img src=` + icon[meetups[meetup].icon] + ` class="icon" /><p> ` + meetups[meetup].name + `</p></a></li>`;
  }

  return `
    <b>${title}</b>
    <ul>${list}</ul>
  `
}