# MarkAnalyzer 🎯

## Basic Details
    Team Name: ByteBenders
    Team Members:
        Anshika Satish - Viswajyothi College of Engineering and Technology
        Arya Vijayakumar - Viswajyothi College of Engineering and Technology
Hosted Project Link:
(MarkAnalyzer):[https://22rr048.github.io/MarkAnalyzer/]

## Project Description:
   MarkAnalyzer is an innovative tool that transforms academic marks into valuable insights. It identifies trends, tracks performance, and provides personalized feedback. Designed for both students and educators, it improves learning and decision-making, making the academic evaluation process more transparent and effective.

## The Problem Statement:
    Grade and Mark Tracking: Allows students and teachers to input marks and get detailed insights into strengths and weaknesses.
    Progress Analysis: Provides trends and predictions based on past performance.
    Personalized Feedback: Suggests study plans or resources to improve weaker subjects.
    Comparison: Benchmarks performance against peers or standards.
## The Solution:
    Highlights weak subjects/topics.
    Provides study recommendations to improve performance!
## Technical Details:
    Technologies/Components Used:
    Languages:
        Frontend: HTML, CSS, JavaScript
        Backend: Python
        Database: SQL

    Frameworks:
        Backend: Flask (Python)

    Libraries:
        Frontend: Fetch API
        Backend: Pandas
## Tools:
    Git, VSCode

## Backend Implementation:
    The backend of MarkAnalyzer is built using Python and the Flask framework. It handles:
    Image upload and processing
    Data extraction from images using Pytesseract
    Performance analysis based on student marks
    Detailed feedback and study suggestions

## Installation:
    To install the necessary dependencies, use the following commands:
        bash
        Copy
        pip install blinker==1.9.0
        pip install certifi==2024.12.14
        pip install charset-normalizer==3.4.1
        pip install click==8.1.8
        pip install colorama==0.4.6
        pip install Flask==3.1.0
        pip install gunicorn==23.0.0
        pip install idna==3.10
        pip install itsdangerous==2.2.0
        pip install Jinja2==3.1.5
        pip install MarkupSafe==3.0.2
        pip install numpy==2.2.2
        pip install packaging==24.2
        pip install pandas==2.2.3
        pip install pillow==11.1.0
        pip install pip==24.3.1
        pip install pytesseract==0.3.13
        pip install python-dateutil==2.9.0.post0
        pip install pytz==2024.2
        pip install requests==2.32.3
        pip install six==1.17.0
        pip install tzdata==2025.1
        pip install urllib3==2.3.0
        pip install Werkzeug==3.1.3
## Run:
    To run the app locally, use the following commands:
        flask run
        gunicorn -w 4 -b 0.0.0.0:8000 app:app
        from PIL import image
        import pytesseract
        import requests

## Project Documentation:
This project includes both front-end and back-end components:
    Frontend: Built using HTML, CSS, and JavaScript. Provides an interactive UI for students and teachers.
    Backend: Powered by Flask. Handles data processing, including image uploads and text extraction.

## Technologies Used:
    HTML: For structuring the web pages.
    CSS: For styling the web pages and making them responsive.
    JavaScript: For adding interactivity (e.g., handling file uploads).
# Acknowledgments:
    Special thanks to the documentation of HTML, CSS, and JavaScript for making web development accessible.

## Screenshots:
![alt text](Markanalyzer_frontend-2.jpg)

## Diagram!
![alt text](<Screenshot 2025-01-26 224019.png>)

## Team Contributions:
    Anshika Satish: Research, testing, and reviewing the implementation. Provided feedback and suggestions for improvements.
    Arya Vijayakumar: Brainstorming ideas, discussing project structure, and contributing to the overall direction of the project.

Made with ❤️ at TinkerHub
