import { Calendar } from '@fullcalendar/core';
import iCalendarPlugin from '@fullcalendar/icalendar';
import dayGridPlugin from '@fullcalendar/daygrid';
import listPlugin from '@fullcalendar/list';

const calendarEl = document.getElementById('calendar-js');
const calendar = new Calendar(calendarEl, {
  plugins: [
    iCalendarPlugin,
    dayGridPlugin,
    listPlugin
  ],
  initialView: 'listMonth',
  events: {
    url: '/basic.ics',
    format: 'ics' // important!
  },
  headerToolbar: {
    left: 'prev,next today',
    center: 'title',
    right: 'listYear,dayGridMonth'
  }
});

calendar.render();
