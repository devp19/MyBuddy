![Screenshot 2024-01-28 at 3 57 34 PM](https://github.com/devp19/MyBuddy/assets/146687531/b1d8f92d-bf05-4fca-9805-cf702c7e2ad5)
<img width="1468" alt="Screenshot 2024-01-29 at 7 18 59 PM" src="https://github.com/devp19/MyBuddy/assets/146687531/4d1c89c5-33f7-4373-8983-d97eddefedd3">


## Aspirations
To provide a comforting mental-health aid to those who are unable to journal and talk to others about their issues. Many people tend to struggle with talking to other people and our goal was to overcome this problem through the use of a generative model that documents your journey to a healthier lifestyle. 

## What It Does
MyBuddy uses Google-Cloud-Speech-Recognition to interpret voice data and then sends it off to the OpenAI GPT-Model API. With a generative-model fixated with a mental-health support prompt, MyBuddy will automatically journal your conversations with it live on the website for you to reflect on. 

## How We Built It
We used a multitude of libraries/programming languages to develop MyBuddy. 
For the frontend, we used HTML, CSS, JavaScript and the Bootstrap 5 framework for a seamless and interactive website. Backend wise, we used Python, Flask (script-running) and the following advanced libraries: OpenAI API (GPT-3.5-Turbo) and Google-Cloud-Speech-Recognition.

To use the GPT-model, we integrated the Google-Cloud-Speech-Recognition library to convert speech to text and then send a request to the OpenAI API using the transcribed text. Our innovate prompt also gets passed through the parameters to remove the non-humane response that GPT-Models are curated for. With a returned JSON dump file, we targeted the response and used Flask to run all the scripts in the background through a simple click of a button. With a static-refresh of 5 seconds, the journal-entry will automatically update with the conversation between the user and MyBuddy.

## Challenges We Faced
Initially, we had planned to use an Arduino ESP32 module that would act as a receiver point for speech-to-text, which would also output GPT responses using a human-voice API. With countless hours of debugging and hardware testing, we came into day 2 with a non-functional project. We then decided to move everything towards a script that would run locally, ideally simulating the Arduino module. When doing this, we came across connectivity issues, frontend/backend communication delays and API errors. 

We diverted to documentation for the errors we faced and spent countless hours doing so. In the end, we were able to make everything work out!

## Accomplishments
We're proud of our whole project! Most importantly our dedication and the ability to integrate a GPT-Model into our project, followed by learning Flask all starting at 4AM on Day 2, we were able to get everything working seamlessly in under 12 hours. 

## Learning
Throughout this hackathon, we learned the skills of working in a team, communication and most importantly the hardworking mindset. Throughout it all we worked all the way to the end, despite all the issues we faced. Software wise, we're proud to have learned API integration and Flask backend script running to help make a website even more interactive.

## What's Next?
For MyBuddy, we aim to convert it into a FullStack application and store the journal-entires in a database! In addition, we'd like for it to have daily check-in reminders, all while using these conversations to train a machine-learning model on human habits and mindset progressions when directed to the right path!

## Team Members
- Dev Patel
- Darsh Kansara
- Krish Munshi
- Dhruvil Patel
- Jay Patel
