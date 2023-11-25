---
title: "Calendar of Events"
menu:
  main:
    name: Events
    weight: -80
    params:
      icon: calendar-event
---
<style>
  .article-time {
    display: none;
  }

  h2.fc-toolbar-title {
    border-left: 0;
    margin: 0;
    padding: 0;
  }

  a.fc-list-day-text {
    color: #000;
    font-weight: bold;
    font-size: 120%;
  }

  .fc .fc-list-event:hover td {
    background-color: rgba(55, 136, 216, 0.5);
  }

  dialog[open] {
    opacity: 1;
    transform: scaleY(1);
  }

  dialog {
    opacity: 0;
    transform: scaleY(0);
    transition:
      opacity 0.3s ease-out,
      transform 0.3s ease-out,
      overlay 0.3s ease-out allow-discrete,
      display 0.3s ease-out allow-discrete;
    /* Equivalent to
    transition: all 0.7s allow-discrete; */
    background: var(--body-background);
    color: var(--card-text-color-main);
    width: 80%;
    max-width: 500px;
    height: 320px;
    max-height: 90%;
  }

  /*   Before-open state  */
  /* Needs to be after the previous dialog[open] rule to take effect,
      as the specificity is the same */
  @starting-style {
    dialog[open] {
      opacity: 0;
      transform: scaleY(0);
    }
  }

  /* Transition the :backdrop when the dialog modal is promoted to the top layer */
  dialog::backdrop {
    background-color: rgb(0 0 0 / 0);
    transition:
      display 0.3s allow-discrete,
      overlay 0.3s allow-discrete,
      background-color 0.3s;
    /* Equivalent to
    transition: all 0.7s allow-discrete; */
  }

  dialog[open]::backdrop {
    background-color: rgb(0 0 0 / 0.50);
  }

  /* This starting-style rule cannot be nested inside the above selector
  because the nesting selector cannot represent pseudo-elements. */

  @starting-style {
    dialog[open]::backdrop {
      background-color: rgb(0 0 0 / 0);
    }
  }
</style>

<div id="calendar-js"></div>
<script src='/cal.js'></script>

<div class="article-category">

[View on Google Calendar](https://calendar.google.com/calendar/embed?src=62da059a43acfa2924e50e6aaa43e3aed3728f7eda51af7d7a43f0313404e09c%40group.calendar.google.com&amp;ctz=America%2FChicago)

[iCal Calendar Subscription Link](webcal://calendar.google.com/calendar/ical/62da059a43acfa2924e50e6aaa43e3aed3728f7eda51af7d7a43f0313404e09c%40group.calendar.google.com/public/basic.ics)

</div>

<dialog id="dialog" class="main-article">
  <div class="article-category" style="float: right; display: block">
    <a href="javascript:void(0);" onclick="document.querySelector('#dialog').close();" style="font-weight: bold; border-radius: 30px; font-size: 12px;">X</a>
  </div>
  <h3>Narf</h3>
  <hr style="margin: 0; width: 100%;">
  <section class="article-content">
    <p>content</p>
  </section>
</dialog
