# Multilingual_Railways_Chatbot

## Railways Chatbot using Large Language Model

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

6. **Run the Chatbot:**
    ```bash
    python chatbot.py
    ```

7. **Interact with the Chatbot:**
    - Open a web browser and go to `http://localhost:5000` to interact with the chatbot through a simple web interface (currently under development).

## Contribution Guidelines

We welcome contributions! If you would like to contribute to the development of the Railways Chatbot (This project is continuously evolving).

## License

This project is licensed under the [MIT License](https://github.com/kunal9922/Multilingual_Railways_Chatbot/blob/main/LICENSE).

## Acknowledgments

Feel free to reach out with any questions or feedback!

Happy chatting! 🚂🤖

## Behavioral diagram
Request and response between the passenger and the chatbot with the help of the Django web framework on the web. This diagram is an **Activity Diagram** in the UML Behavioral Diagram category. This diagram shows how a passenger, a chatbot, and a railway database handle a train query. The diagram uses lines and arrows to show the flows and interactions of each component. The messages are labeled with the information or operation. For example, the first message is a user (passenger) request \"query about trains\", from the passenger to the chatbot, followed by the AI (chatbot) response to resolve the query.

![railwaysChatbotFlow](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/ccae208e-0b3a-485b-b1bc-5aa96f92b021)
