<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]


## Project Example (May take a second or two to load)
<!-- PROJECT LOGO -->
<p align="center">
  <img src="https://github.com/ageltz07/WhatsAppBot/blob/main/whatsAppBot.GIF" alt="animated" />
</p>
<br />

<!-- ABOUT THE PROJECT -->
## About The Project

This is a flask web application for an Chatbot utilizing OpenAI's "Davinci" Language model that allows the user to do multiple things such as translate English to other language answer general questions and much more. The user uses WhatsApp to communicate with the bot their message is routed to Twilio which then routes to the Flask app hosted on Heroku which uses the OpenAI api to get a response from a Davinci model and then sends it back to the user.

I was intrigued by the new ChatGPT from OpenAI that was just opened up to the public but there is no API for that yet so I just used what was available in their current api. I also built this project because I wanted to learn a little more about using external API's from inside a web application. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
*  [![Python][python-shield]][python-url]
*  [![Flask][flask-shield]][flask-url]
*  [![Visual Studio Code][Visual Studio Code-shield]][Visual Studio Code-url]
### Deployed On
*  [![Heroku][Heroku-shield]][Heroku-url]
### API's Used
* [Twilio](https://www.twilio.com/)
* [OpenAI](https://openai.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- System Design -->
## Design
<p align="center">
  <img src="https://github.com/ageltz07/WhatsAppBot/blob/main/WhatsApp.drawio.png"/>
</p>

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/adam-geltz/
[product-screenshot]: images/screenshot.png
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[flask-shield]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Visual Studio Code-shield]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Visual Studio Code-url]: https://visualstudio.microsoft.com/
[Heroku-shield]: https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white
[Heroku-url]: https://id.heroku.com/login
