// This function loads events from the server and updates the list
async function getEvents() {
  const res = await fetch('/events');  // Ask the Flask server for the data
  const data = await res.json();       // Convert response into usable JSON

  const list = document.getElementById('events');
  list.innerHTML = '';  // Clear current list

  data.forEach(e => {
    let line = '';
    const time = new Date(e.timestamp).toUTCString();

    if (e.type === 'push') {
      line = `${e.author} pushed to ${e.to_branch} on ${time}`;
    } else if (e.type === 'pull_request') {
      line = `${e.author} submitted a pull request from ${e.from_branch} to ${e.to_branch} on ${time}`;
    } else if (e.type === 'merge') {
      line = `${e.author} merged ${e.from_branch} to ${e.to_branch} on ${time}`;
    }

    const li = document.createElement('li');
    li.textContent = line;
    list.appendChild(li);
  });
}

// Run getEvents every 15 seconds
setInterval(getEvents, 15000);

// Also run it immediately when page loads
window.onload = getEvents;
