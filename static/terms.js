document.addEventListener('DOMContentLoaded', () => {
    const checkbox = document.getElementById('terms-checkbox');
    const submitBtn = document.getElementById('submit-btn');

    checkbox.addEventListener('change', () => {
        if (checkbox.checked) {
            submitBtn.disabled = false;
            submitBtn.classList.add('enabled');
            submitBtn.classList.remove('disabled');
        } else {
            submitBtn.disabled = true;
            submitBtn.classList.remove('enabled');
            submitBtn.classList.add('disabled');
        }
    });
});
function updateDateTime() {
    const now = new Date();
    const datetimeElement = document.getElementById('datetime');
    const formattedDateTime = now.toLocaleString('en-IN', { dateStyle: 'long', timeStyle: 'medium' });
    datetimeElement.textContent = formattedDateTime;
}

setInterval(updateDateTime, 1000); // Updates the time every second

