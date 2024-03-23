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
Embarking on this web scraping project, my journey began with a basic understanding of the concept. The learning curve was steep; every step forward revealed the vast expanse of knowledge and techniques yet to be mastered. The project unfolded as a captivating yet daunting adventure due to its complexity and the myriad of possibilities it presented.

Tool Selection and Learning Curve: Initiated my journey with BeautifulSoup, transitioning to Selenium upon realizing the limitations of BeautifulSoup with JavaScript-heavy websites like Amazon. The switch was based on extensive advice and research, including hours spent on Udemy courses to grasp the fundamentals of web scraping.

Technical Difficulties: Encountered significant hurdles with Selenium, particularly with maintaining the Chromedriver window open—a factor that seemed to impact the success of my code. This inconsistency in performance led to repeated troubleshooting and modifications. These technical hurdles were compounded by inconsistent results; scripts that worked once would inexplicably fail upon reruns. This unpredictability added to the challenge, leading me down various troubleshooting paths with limited success. In my quest for legality and best practices, I reached out to Amazon's technical support at api-services-support@amazon.com to request permission for web scraping. However, my attempts were met with silence as my emails bounced back, marked as delivery failures. This setback highlighted the complexities of navigating legal and ethical considerations in web scraping projects.

Exploring New Technologies: I ventured into the realm of Amazon's Developer services, creating an Amazon Developer account in hopes of leveraging their API Gateway. Despite my efforts, the complexity and lack of clear guidance on using their API Gateway left me stymied, unable to make significant progress. Additionally, my exploration led me to BrightData, venturing into their proxy solutions to bypass scraping restrictions. Although successful on one occasion, reproducing the success proved challenging, illustrating the volatile nature of web scraping techniques.

Perseverance Amidst Setbacks: The project was characterized by multiple restarts and strategic shifts, from APIs to browser scraping and the use of Web Unlocker techniques. The vast array of methods and tools was overwhelming yet educational, illustrating the multifaceted approaches within web scraping.

Project Milestones: Despite the hurdles, a significant breakthrough was achieved with the BrightData API, marking a pivotal moment in the project's development. However, time constraints imposed by the challenge's deadline limited the project's completion and refinement.

Additional Features and Future Scope: Investigated SMTP and Twilio for notification systems and delved into data visualization possibilities. Each new avenue required time and learning, contributing to the overall complexity but also to the potential value of the completed project.

Nevertheless, the project remains a source of great interest and potential. I am eager to develop it further, aiming for a comprehensive tool that can monitor various products, incorporate data visualization, and implement an effective text message notification system. The journey has been challenging, but it is far from over.

## TESTING
Due to time constraints, the testing phase was abbreviated. Notifications were tested with a 1-minute interval instead of the intended 24-hour cycle. While this does not adhere to standard testing protocols, it served as a preliminary check to ensure basic functionality. Future testing phases will aim for a more thorough and time-appropriate evaluation to ensure reliability and effectiveness of the notification system.

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
