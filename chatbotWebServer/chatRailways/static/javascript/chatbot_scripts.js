// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie name starts with the specified name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function takeUserQuery() {
    /*Takes request user's input query from frontend send to the backend server in Json to resolve the query
    then backend server responses in json finally display the response  */
    const userQuery = document.getElementById('user-query').value;
    // AJAX request to Django view
    fetch('/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token here
        },
        body: JSON.stringify({ "userQuery": userQuery })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.response);
        document.getElementById('response').value = data.response;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function submitForm(event) {
    event.preventDefault(); // Prevent default form submission
    takeUserQuery(); // Call your existing function
}