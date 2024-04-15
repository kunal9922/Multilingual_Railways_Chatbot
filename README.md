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
    ```
2. **Make an alias for Windows PowerShell** 
    ```powershell
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
  ### Voice-to-Text Transcriber Whisper also requires FFmpeg, an audio-processing library.
5. **Chocolatey a Windows package manager to install https://chocolatey.org/install**
    ```powershell
    choco install ffmpeg
    ```
6. **Homebrew a MacOS package manager to install https://brew.sh/**
    ```bash
    brew install ffmpeg
    ```
7. **For Linux OS**
   ```bash
   sudo apt update && sudo apt install ffmpeg
   ```
9. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6. **Shift to the Django Server Directory**
   ```bash
   cd chatbotWebServer\
   ```
7. **Download the LLAMA-2-7B Model from https://huggingface.co/meta-llama**
      Save the LLM model into this directory "\chatRailways\chatbotModule\models"
   
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
![Screenshot 2024-02-02 182717](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/a1e73eb6-d4a7-4e6a-b1be-bfb39a9c48fc)
![Screenshot 2024-02-02 183214](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/3103aaa1-d195-47c3-ab90-1fa9cf2cad8d)
![Screenshot 2024-02-03 133452](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/713a07d0-c09c-44d8-baa8-586af8802bd1)
![Screenshot 2024-02-03 201811](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/57fa3281-ed09-418b-82d7-bee438bc3c40)

# Multilingual Speech-Driven Chatbot Interaction Demo Videos

https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/2000bb13-b558-4627-aa7c-07b07168ece1

https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/fc0c5a69-ef84-4d99-9385-9104d74f223b

## Behavioral diagram
A web-based chatbot for train queries using Django. This UML Activity Diagram shows the steps and messages between a passenger, a chatbot, and a railway database. For example, the passenger asks "query about trains" and the chatbot replies with the answer.

![railwaysChatbotFlow](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/ccae208e-0b3a-485b-b1bc-5aa96f92b021)

## Chatbot that can interact with CSV files
This diagram shows how to build a chatbot that can interact with CSV files. The chatbot extracts data content from a CSV file and converts it into embeddings using a vector store. Then, it builds a semantic index based on FAISS to perform semantic search on the data. The chatbot can answer user queries by converting them into query embeddings and searching for the most relevant answers in the knowledge base.

![chatBot_arch](https://github.com/kunal9922/Multilingual_Railways_Chatbot/assets/53283003/54e1f9ef-0484-4fff-b773-cbac2789e577)

