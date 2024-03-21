# Price Alert System
This project contains a Python script designed to monitor the price of a product using the Bright Data API.
If the product price falls below a specified threshold, the script sends a desktop notification alerting the user to the price drop.
This system is set to check the price every 24 hours, but it can be configured to any interval.

## Getting Started
Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need Python 3.x installed on your machine. Additionally, ensure you have the following Python libraries installed:

- `requests`
- `plyer`
- `apscheduler`
- `pytz`

BRIGHTDATA ACCOUNT
You'll also need to obtain an authorization token from Bright Data and set it as an environment variable named AUTH on your system.
Be mindful that it can take a few days for your account to get verified and permition given.

## CHALLENGES FACED
I just had a general idea of what web scraping was, I've learned a lot to get to where I did and yet seems like I'm barely scraping the surface.
A very interesting tool, endless possibilities, very exciting and at the same time very intimidating for it's endless rabbit holes.
After a few hours of Udemy courses, I've started with BeautifulSoup, tried Selenium after repeatedly being advised that a JavaScript websites like Amazon would only work with Selenium and not BeautifulSoup.
I had challenges with chromedriver window not staying open, giving me the impression that it was the reason the code wasn't working. I've got the window to open and stay open at one point and noticed that many times something would work for once and then not work as I would try again.
Just yesterday I found a BrightData tutorial using their proxy approach, that got me what I wanted but just once. Gave me a .csv file with the product price - Another gitHub repository.
I've got discouraged many times, tried many different routes.... Lost track of how many start overs. The good news (just today), going back to one of the projects and finally could accomplish what I wanted with BrightData API.
When I finaly saw that I've got the data I was looking for, I didn't have much time to finish the project in time for the challenge's time frame.
I took a look at SMTP and Twilio but again would need more time to implement those notifications.
Also looked into data visualization options... again, so many routes and as a early career got pretty overwhelmed.
Very interesting project, looking forward to finish and actually use it with the hability to choose different products, with data visualization and a text message notification system.

## TESTING
Tested notification applying a 1 minute interval instead of 24 hours.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
License
Distributed under the MIT License. See LICENSE for more information.

## Acknowledgments
Inspired by a technical challenge for a job interview process, thank you Levi Siebens!

A tutorial that was very helpful: https://youtu.be/7ahUnBhdI5o?si=xSPQ9XUsJns7tCz3)https://youtu.be/7ahUnBhdI5o?si=xSPQ9XUsJns7tCz3
