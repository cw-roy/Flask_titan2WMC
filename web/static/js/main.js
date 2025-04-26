function updateListings() {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = 'Updating listings...';
    
    fetch('/update', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        messageDiv.textContent = `Status: ${data.status} - ${data.message}`;
        if (data.status === 'success') {
            setTimeout(() => location.reload(), 2000);
        }
    })
    .catch(error => {
        messageDiv.textContent = `Error: ${error}`;
    });
}