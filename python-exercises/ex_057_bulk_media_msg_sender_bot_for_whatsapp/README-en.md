### <img src="https://cdn-icons-png.flaticon.com/512/197/197386.png" width="15" height="15" alt="Brazil" /> [Clique aqui para acessar a versão em português!](README.md)

<hr>

# Automated bot for sending bulk multimedia messages on WhatsApp

## Description:

* Mass message sender bot for WhatsApp using your contacts' and/or groups' names. 🤖
* Text message with an option to include an image or video, as well as automatic personalization of each message using the contact and/or group name.
* The bot has clear instructions and usage tips throughout its execution. 📝
* Available in: <img src="https://cdn-icons-png.flaticon.com/512/197/197386.png" width="15" height="15" alt="Brazil" /> **Portuguese** and <img src="https://cdn-icons-png.flaticon.com/512/323/323329.png" width="15" height="15" alt="United Kingdom" /> **English** .

> *I recommend sending a test message to yourself to understand how everything works. For those who don't know, just add your own number as a contact in your address book and you can send messages to your own WhatsApp user.*

<hr>

## Demo video of the app in action (in Portuguese):

**[Click here](https://youtu.be/Ha-t__BuUs4)** to watch a video on *YouTube* of the application in action.

<hr>

## Screenshots:
<table>
  <tr>
    <td>
       <img src="https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/blob/main/sample/screenshot_01_en.png" width="360" height="320" align="top" alt="Screenshot 01" />
     </td>
     <td rowspan="2">
        <img src="https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/blob/main/sample/screenshot_03_en.png" width="360" height="484" alt="Screenshot 03" />
     </td>
   </tr>
   <tr>
      <td> <img src="https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/blob/main/sample/screenshot_02_en.png" width="360" height="190" alt="Screenshot 02" />
      </td>
   </tr>
</table>

<hr>

## About the project:

* This is my first personal programming project.
* It was created in **Python** 🐍 for hobby to apply and demonstrate the skills and knowledge I have acquired so far in various programming topics, such as: *modularization, code organization, object-oriented programming, inheritance, input validation, error and exception handling, automation* among others. And also explore the use of the terminal as much as possible, trying to make it as pleasant as possible using good formatting, as well as animate and color the texts. It was a very "artisanal" process to make it as intuitive as possible, even without the use of a graphical interface.
* I did my best to make it "round", handling all the bugs I could find. If you find any bug, let me know! 🧑‍🔧

> *This is a tool created for educational purposes only. I am not responsible for any misuse of the app. Do not abuse it to send spam or bother your friends. 😉*

<hr>

## Requirements:

- Windows 10/11
- Chrome browser
- Python 3.10+ (if running directly from the source code)

<hr>

## How to use (from the executable):

### Run with a single click

* Download the executable **[here](https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/releases/tag/1.0)** and save it to your computer.

> **Your application is ready to use!**

<hr>

## How to use (from the source code):

### Downloading the source code

1. Download the folder with the source code  **[here](https://github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp/releases/tag/1.0)** .
2. Extract the contents of the compressed file on your computer.

### Installing Python

1. Visit the official **Python** website at [python.org](https://www.python.org/downloads/) and download the latest version of Python for your operating system.
2. Follow the installer instructions. Make sure to check the **"Add Python 3.xx to PATH"** option.

### Installing dependencies

1. Open your Terminal or PowerShell and navigate to the directory of your extracted application (replace **"C:\DOWNLOAD_FOLDER"** with the location where you extracted the zip file):
   ```
   cd C:\DOWNLOAD_FOLDER\bot-whatsapp-bulk-media-msgs-sender
   ```
2. Use the code below to install the necessary dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

### Running the application

1. Still inside the folder, run the main file of your application:
   ```
   python main.py
   ```
2. Follow the instructions that will appear on the screen to use your application.

<hr>

## 💡 Status known issues

- I personally only tested it on Windows 11 (CMD and PowerShell), but it should theoretically work well on most operating systems, including Linux and MacOS.

If the user corrects the inputs too many times, the terminal may start to slow down. I'm an amateur, so any tips regarding this will be welcome!

The app does not correctly verify if the user enters a non-existent contact or group name.

If something doesn't work for you or doesn't do what you expect, I would love to hear your feedback. You can contact me through any of the means below.

<hr>

## 👨‍💻 To developers:

- I hope the code is fairly readable. Sorry for the comments only in Portuguese!
- It's worth remembering that websites are reformulated from time to time, so I don't know if the bot will be working perfectly when you test it. If you know the basics of web scraping, simply update the CSS and XPATH selector variables of the msg_sender.py module to those that WhatsApp Web is using at the moment.
- To prevent WhatsApp Web from asking you to scan the QR code every time you use the application, you can "uncomment" this section of code within the "init_webdriver()" function of the "bot.py" module and replace the installation directory of my Chrome with yours:

  ```
  options = webdriver.ChromeOptions()
  options.add_argument(
              r'--user-data-dir=C:\\Users\\ferna\\AppData\\Local\\Google\\Chrome\\User Data\\')
  self.driver = webdriver.Chrome(
              executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
  ```

<hr>
<img width="200" height="25" src="https://img.shields.io/tokei/lines/github.com/fernandoaafonseca/bulk_media_msg_sender_bot_for_whatsapp?label=Total%20lines%20of%20code&logo=Python" alt="Lines of code" />
