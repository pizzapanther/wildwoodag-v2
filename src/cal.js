import { Calendar } from '@fullcalendar/core';
import iCalendarPlugin from '@fullcalendar/icalendar';
import dayGridPlugin from '@fullcalendar/daygrid';
import listPlugin from '@fullcalendar/list';
import momentPlugin from '@fullcalendar/moment';

var locale = {
  code: 'en-us',
  noEventsText: 'Events Loading ...'
};

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
    locale: locale,
    plugins: [
      iCalendarPlugin,
      dayGridPlugin,
      listPlugin,
      momentPlugin
    ],
    initialView: view,
    eventSources: [
      {
        url: 'https://faas-sfo3-7872a1dd.doserverless.co/api/v1/web/fn-67f34cf4-c3ed-479c-839e-2f7206029fcb/wildweb/calcache',
        format: 'ics' // important!
      },
      {
        url: 'https://api.called.app/rest/calendar/community/998',
        format: 'ics'
      }
    ],
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
      console.log(info.event.extendedProps.description);
      let desc = info.event.extendedProps.description || "<strong>no details found</strong>";
      if (desc.startsWith("[{")) {
        desc = desc.match(/"insert":"(.*)"/s)[1];
        desc = desc.replace("\\n", "<br>");
      }
      document.querySelector('#dialog section p').innerHTML = desc;
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
