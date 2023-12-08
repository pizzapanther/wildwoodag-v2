import { Calendar } from '@fullcalendar/core';
import iCalendarPlugin from '@fullcalendar/icalendar';
import dayGridPlugin from '@fullcalendar/daygrid';
import listPlugin from '@fullcalendar/list';
import momentPlugin from '@fullcalendar/moment';

function load_calendar(view) {
  var header = {left: '', right: ''};
  if (view == 'dayGridMonth') {
    header = {
      left: 'title',
      right: 'prev,next today'
    };
  }

  const calendarEl = document.getElementById('calendar-js');
  const calendar = new Calendar(calendarEl, {
    plugins: [
      iCalendarPlugin,
      dayGridPlugin,
      listPlugin,
      momentPlugin
    ],
    initialView: view,
    events: {
      url: 'https://faas-sfo3-7872a1dd.doserverless.co/api/v1/web/fn-67f34cf4-c3ed-479c-839e-2f7206029fcb/wildweb/calcache',
      format: 'ics' // important!
    },
    contentHeight: 'auto',
    height: 'auto',
    headerToolbar: header,
    listDayFormat: 'ddd, MMM Do',
    visibleRange: function(currentDate) {
      var startDate = new Date(currentDate.valueOf());
      var endDate = new Date(currentDate.valueOf());
      startDate.setDate(startDate.getDate());
      endDate.setDate(endDate.getDate() + 90);
      return { start: startDate, end: endDate };
    },
    eventClick: (info) => {
      var e = info.event;
      var title = e.title + '<br>' + e.start.toLocaleDateString() + ' ' + e.start.toLocaleTimeString();
      title = title.replace(":00 ", " ");
      document.querySelector('#dialog h3').innerHTML = title;
      document.querySelector('#dialog section p').innerHTML = info.event.extendedProps.description || "<strong>no details found</strong>";
      document.querySelector('#dialog').showModal();
      setTimeout(() => {
        document.querySelectorAll('#dialog section a').forEach((item) => {
          item.target = '_blank';
        });
      }, 0);
    }
  });

  calendar.render();
}

window.load_calendar = load_calendar;
