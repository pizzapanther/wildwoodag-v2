---
image: /img/cover.jpg
menu:
  main:
    name: Home
    weight: -100
    params:
      icon: home
template: post
categories: []
tags: []
---
<style>
.article-details {
    display: none;
}

.article-image {
    position: relative;
}


.banner {
  background-color: rgba(255, 255, 255, 0.5);
  width: 100%;
  height: 100%;
  position: absolute;
  white-space: pre-wrap;
  font-size: 3em;
  color: #000;
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
  padding: 0 20px;
  text-shadow: 2px 2px 5px #A6B939;
  white-space: nowrap;
}

@media (max-width: 550px) {
    .banner {
        font-size: 2em;
    }
}

.banner > div:first-child {
    font-weight: bold;
}


.nav-btns {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;

  a {
    font-size: 1.4rem;
    margin: 5px;
    border: 1px solid;
    border-radius: 5px;
    display: flex;
    width: 150px;
    max-width: 150px;
    min-width: 150px;
    align-items: center;
    justify-content: center;
    white-space: no-wrap;

    svg {
      height: 1.8rem;
    }
  }
}
</style>

<template id="banner-tpl">
    <div class="banner">
        <div>Wildwood Assembly</div>
        <div>Welcome Home</div>
    </div>
</template>

<script>
function showContent() {
  let temp = document.getElementById("banner-tpl");
  let clon = temp.content.cloneNode(true);
  document.querySelector(".article-image").prepend(clon);
}

showContent();
</script>

<!--<div>
  <img src="img/not-bob-bennett-2024.jpg" alt="Claude Butch Morgan - Community Concert">
  <br>
  <br>
</div>-->
<div class="app-buttons" style="text-align: center; display: none;">
  <a href="https://apps.apple.com/us/app/wildwood-assembly/id6465793721" target="_blank">
    <img src="/img/apple-store.png" alt="Download on the App Store" style="height: 40px;">
  </a>
  &nbsp;&nbsp;
  <a href="https://play.google.com/store/apps/details?id=com.wildwoodag.church&pli=1" target="_blank">
    <img src="/img/google-store.png" alt="Get it on Google Play" style="height: 40px;">
  </a>
</div>


<br>
<div class="nav-btns">
  <a href="/about/">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-question-mark" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M8 8a3.5 3 0 0 1 3.5 -3h1a3.5 3 0 0 1 3.5 3a3 3 0 0 1 -2 3a3 4 0 0 0 -2 4"></path>
      <path d="M12 19l0 .01"></path>
    </svg>
    <span>About</span>
  </a>
  <a href="/events/">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-calendar-event" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
       <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
       <path d="M4 5m0 2a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2z"></path>
       <path d="M16 3l0 4"></path>
       <path d="M8 3l0 4"></path>
       <path d="M4 11l16 0"></path>
       <path d="M8 15h2v2h-2z"></path>
    </svg>
    <span>Events</span>
  </a>
  <a href="/watch/">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-brand-youtube" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
       <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
       <path d="M2 8a4 4 0 0 1 4 -4h12a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-12a4 4 0 0 1 -4 -4v-8z"></path>
       <path d="M10 9l5 3l-5 3z"></path>
    </svg>
    <span>Watch</span>
  </a>
  <a href="/donate/">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-heart-handshake" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
       <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
       <path d="M19.5 12.572l-7.5 7.428l-7.5 -7.428a5 5 0 1 1 7.5 -6.566a5 5 0 1 1 7.5 6.572"></path>
       <path d="M12 6l-3.293 3.293a1 1 0 0 0 0 1.414l.543 .543c.69 .69 1.81 .69 2.5 0l1 -1a3.182 3.182 0 0 1 4.5 0l2.25 2.25"></path>
       <path d="M12.5 15.5l2 2"></path>
       <path d="M15 13l2 2"></path>
    </svg>
    <span>Donate</span>
  </a>
  <a href="/blog/">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-notebook" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
       <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
       <path d="M6 4h11a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-11a1 1 0 0 1 -1 -1v-14a1 1 0 0 1 1 -1m3 0v18"></path>
       <path d="M13 8l2 0"></path>
       <path d="M13 12l2 0"></path>
    </svg>
    <span>Pastor's Pen</span>
  </a>
  <a href="/contact/">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-phone-call" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
       <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
       <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2"></path>
       <path d="M15 7a2 2 0 0 1 2 2"></path>
       <path d="M15 3a6 6 0 0 1 6 6"></path>
    </svg>
    <span>Contact</span>
  </a>
  <a href="/chat/">
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-messages" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path stroke="none" d="M0 0h24v24H0z"></path>
      <path d="M21 14l-3 -3h-7a1 1 0 0 1 -1 -1v-6a1 1 0 0 1 1 -1h9a1 1 0 0 1 1 1v10"></path>
      <path d="M14 15v2a1 1 0 0 1 -1 1h-7l-3 3v-10a1 1 0 0 1 1 -1h2"></path>
    </svg>
    <span>Group Chat</span>
  </a>
</div>
<hr>

<br>
<img alt="Cross" src="/img/cross.jpg" style="width: 40%; float: right; border-radius: 10px;">

## Location

227 Charter Oak Drive<br>
Canyon Lake, Texas 78133

## Service Times

**Sunday**:<br>
Bible Study: 9:15 AM<br>
Service: 10:30 AM

**Wednesday:**<br>
Dinner: 6:00 PM in the Dining Hall<br>
Service: 7:00 PM

For more events see our [calendar page](/events/).

## Map

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4760.43977184077!2d-98.24970147546678!3d29.83540784247989!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x865c9c438d3f3315%3A0xa308a4af0a430fa3!2sChurch%20In%20the%20Wildwood%20Assembly!5e0!3m2!1sen!2sus!4v1693251391775!5m2!1sen!2sus" width="600" height="450" style="width: 100%; border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

## Who We Are

- Called to His Plan
- Caring for His People
- Committed to His Purpose

We have been called to Worship our Lord in spirit mind soul and body. Caring, we step forward to the ministry of meeting the needs of individuals, families and our community. We are comitted to the task that He has set before us. We are his workmanship created in Christ Jesus our LORD. We are being fitly framed together as a habitation of the Holy Ghost exalting the Lordship of Jesus Christ.

Those who enter here are being saved, baptized, healed, filled with the Holy Spirit! We are looking for His soon return. We will stand in His righteousness. Crucified with Christ, nevertheless living in the faith of the Son of God. What is your purpose? – Join us and find out what God’s Purpose is for your life.
