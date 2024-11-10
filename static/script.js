// JavaScript functionalities for the Local Crime Reporting (LCR) project

// Smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault(); // Prevent default anchor behavior
    const targetId = this.getAttribute('href');
    const targetSection = document.querySelector(targetId);
    if (targetSection) { // Check if the target section exists
      targetSection.scrollIntoView({
        behavior: 'smooth'
      });
    }
  });
});

// Crime report submission handler
document.getElementById('crime-report-form').addEventListener('submit', function (e) {
  e.preventDefault(); // Prevent the form from submitting the default way
  
  // Collect form values
  const username = document.getElementById('username').value;
  const location = document.getElementById('crime-location').value;
  const crimeType = document.getElementById('crime-type').value;
  const description = document.getElementById('crime-description').value;
  const crimeTime = document.getElementById('crime-time').value;

  // Validate form fields
  if (username && location && crimeType && description && crimeTime) {
    alert(`Thank you, ${username}! Your report has been submitted successfully.`);
    // Here you would usually send the report to your server or API
    // For example: sendReportToServer({username, location, crimeType, description, crimeTime});
    
    // Reset the form fields
    document.getElementById('crime-report-form').reset();
  } else {
    alert('Please fill in all fields.');
  }
});

// Set interval for updating date and time
setInterval(updateDateTime, 1000);

// Initialize the live date and time on page load
updateDateTime();
