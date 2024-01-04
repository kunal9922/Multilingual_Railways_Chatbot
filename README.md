# Multilingual_Railways_Chatbot

## Overview

This repository contains the source code and resources for a railway's chatbot built using a Large Language Model. The chatbot is designed to assist railway passengers by providing information on train schedules, platform details, delays, and other related inquiries. It leverages a state-of-the-art large language model to understand natural language queries and deliver accurate responses.

## Features

- **Natural Language Understanding:** Utilizes advanced language processing to understand user queries conversationally.
  
- **Multilingual Support:** Supports various languages to cater to diverse passenger needs.

- **Real-time Information:** Provides up-to-date information on train schedules, delays, and platform changes.

- **Interactive Interface:** Engages users in a chat-like interface for a seamless and user-friendly experience.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/kunal9922/Multilingual_Railways_Chatbot.git
    cd Multilingual_Railways_Chatbot
    ```
2. **Make an alias for Windows PowerShell** 
    ```bash
   New-Alias -Name python310 -value "yourPython3.10.exe path"
   ```
3. **Create a Python Virtual Environment**
    ```bash
    python310 -m venv venvChatbotRailways
    ```
4. **Activate the virtual environment**
    ```bash
    venvChatbotRailways\Scripts\activate
    ```
5. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6. **Shift to the Django Server Directory**
   ```bash
   cd chatbotWebServer\
   ```
7. **Download the LLAMA-2-7B Model from https://huggingface.co/meta-llama**
      Save the LLM model into this "\chatRailways\chatbotModule\models"
   
9. **Run the Django Server for the Chatbot:**
    ```bash
    python manage.py runserver
    ```
10. **Interact with the Chatbot:**
    - Open a web browser and go to `http://localhost:8000` to interact with the chatbot through a simple web interface.

## Contribution Guidelines

We welcome contributions! If you would like to contribute to the development of the Railways Chatbot (This project is continuously evolving).

## License

This project is licensed under the [MIT License](https://github.com/kunal9922/Multilingual_Railways_Chatbot/blob/main/LICENSE).

## Acknowledgments

Feel free to reach out with any questions or feedback!

Happy chatting! 🚂🤖

## Screenshots
![Screenshot 2024-01-04 194234](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/d4025116-1d4f-4940-ab5c-40cf6fefa04b)
![Screenshot 2024-01-04 194518](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/3ee47b74-3216-4699-8b00-f010bd8687ec)
![Screenshot 2024-01-04 200511](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/a2baa679-4cc9-4827-953e-6b4e6cb3ef99)


## Behavioral diagram
A web-based chatbot for train queries using Django. This is a UML Activity Diagram that shows the steps and messages between a passenger, a chatbot, and a railway database. For example, the passenger asks "query about trains" and the chatbot replies with the answer.

![railwaysChatbotFlow](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/ccae208e-0b3a-485b-b1bc-5aa96f92b021)
