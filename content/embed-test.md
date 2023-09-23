---
title: Embed Test
---

## Embed Test

<div id="stream-frame" style="width: 100%; height: 100%; color: white; background-color: black; display: flex; justify-content: center; align-items: center;">
  <h2>Waiting for Stream to Start</h2>
</div>
<script>
function fetch_status() {
  fetch('https://wildwoodag.herokuapp.com/stream-frame/status_1.json?channel=UCmo8zL1ZhvT4vYNzhSAuAEw&ts=' + Date.now())
    .then(response => response.json())
    .then((data) => {
      if (data.status == 'live') {
        document.querySelector("#stream-frame").innerHTML = data.embed;
      } else{
        setTimeout(fetch_status, 10000);
      }
    })
    .catch(e => alert('Error fetching stream status; refresh page.'));
}
fetch_status();
</script>
