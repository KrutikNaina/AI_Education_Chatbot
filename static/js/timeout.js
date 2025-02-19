// // static/js/timeout.js
// let idleTime = 0;
// const idleLimit = 1 * 60; // 5 minutes in seconds

// // Reset idle time on any user interaction
// window.onload = resetTimer;
// window.onmousemove = resetTimer;
// window.onkeypress = resetTimer;

// function resetTimer() {
//     idleTime = 0;
// }

// // Check idle time every second
// setInterval(function() {
//     idleTime++;
//     if (idleTime >= idleLimit) {
//         alert("You have been idle for 5 minutes, please log in again.");
//         window.location.href = "{% url 'login' %}";  // Redirect to login
//     }
// }, 1000);
