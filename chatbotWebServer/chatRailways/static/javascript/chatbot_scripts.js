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

var isRecording = false;
function togglePlayPause() {
    /**
     * The function toggles between starting and stopping a recording, changing the icon and state
     * accordingly.
     */
    var button = document.getElementById('playPauseButton');
    var icon = document.getElementById('icon');

    if (!isRecording) {
        // Change to pause icon
        icon.src = pauseIconUrl;
        // Start recording
        startRecording();
        isRecording = true;
    } else {
        // Change to play icon
        icon.src = recordIconUrl;
        // Stop recording
        stopRecording();
        isRecording = false;  
    }
}

let mediaRecorder;
let audioChunks = [];

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then((stream) => {
            mediaRecorder = new MediaRecorder(stream);

            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    audioChunks.push(event.data);
                }
            };

            mediaRecorder.onstop = () => {
                if (audioChunks.length > 0) {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                    const audioUrl = URL.createObjectURL(audioBlob);

                    // Send the audioBlob to Django using a fetch request
                    sendAudioToDjango(audioBlob);

                    audioChunks = [];
                } else {
                    console.warn('No audio data recorded.');
                }
            };

            mediaRecorder.start();
            // startRecordingBtn.disabled = true;
            // stopRecordingBtn.disabled = false;
        })
        .catch((error) => {
            console.error('Error accessing microphone:', error);
        });
}

function stopRecording() {
    if (mediaRecorder) {
        mediaRecorder.stop();
    }
}

function sendAudioToDjango(audioBlob) {
    // Create a FormData object to send the audio file
    const formData = new FormData();
    formData.append('audio', audioBlob, 'voice_input.wav');

    // Send the FormData to your Django server using fetch
    fetch('/speech/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token here
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response:', data);
        document.getElementById('user-query').value = data.text;
        var selectElement = document.getElementById('language-select');
        // Set the value to 'based on the input voice' (Urdu)
        selectElement.value = data.langCode;
    })
    .catch(error => {
        console.error('Error sending audio to Django:', error);
    });
}

function takeUserQuery() {
    /*Takes user's input query as request from frontend then send to the backend server in Json to resolve the query
    then backend server responses in json, finally display the response  */
    const userQuery = document.getElementById('user-query').value;
    // Translation values
    const selectedLanguage = document.getElementById('language-select').value;
    console.log(document.getElementById('language-select').value);
    // AJAX request to Django view
    fetch('/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token here
        },
        body: JSON.stringify({ "userQuery": userQuery, "selectedLanguage": selectedLanguage})
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