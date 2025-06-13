# :rocket: ProHabit
### Video Demo: [Final Project](URL)
### Description

## :thought_balloon: Why ProHabit?
I've always believed that discipline can outweigh talent. However, being disciplined requires commitment and consistency in forming habits.

Transforming an action into a daily habit is often a challenge at first. That's why I created **ProHabit**, a web application designed to facilitate the tracking and fulfillment of daily habits.

## :ledger: General Overview
**ProHabit** is the culmination of my learning in **CS50x - Introduction to Computer Science**. This web application, built with a combination of technologies and frameworks, showcases the skills I acquired throughout the course.

Developed with **HTML, CSS, and JavaScript**, and powered by frameworks like **Bootstrap** for responsive design and **SQLAlchemy** for data management, ProHabit adapts seamlessly to various screen sizes and devices. Behind the scenes, the application runs on **Python and Flask**, which handle requests, process data, and interact with the database.

My goal in creating **ProHabit** was to achieve a **simple, customizable, and functional** application. While it offers basic functionalities to get started, its design allows for future enhancements and the addition of new features to enrich the user experience.

## :open_file_folder: Project Structure

### Frontend: HTML, CSS, JavaScript
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="html5 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="css3 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" height="40" alt="bootstrap logo"  />
  <img width="12" />
</div>

ProHabit's frontend is designed to provide an intuitive and dynamic user experience.

#### Templates
- `login.html`: This is the first page rendered when you access the application. It presents a simple form for entering your username and password. It includes a navigation bar with options like **Register, Login**, and **Home Page**.
- `register.html`: A form designed for new user registration. It incorporates security validations to prevent duplicate usernames and confirm passwords. Once successfully registered, the user is automatically logged in.
- `index.html`: The main page of the web application. It dynamically displays a form to add new habits. Additionally, it shows a table with all the habits the user wants to track, along with a button for each habit to click every time a habit is completed at the established frequency. Once a habit is completed, it will be locked and highlighted in green, indicating its fulfillment.
- `layout.html`: Serves as the basic structure for the rest of the templates. It's called in every template rendered in the application to maintain a standard format and functionalities throughout the project.

#### Static
- `styles.css`: This file defines the visual appearance of the entire application, adding styles and elegant dynamism to some of the application's functions.

---

### Backend: Python and Flask
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" alt="flask logo"  />
  <img width="12" />
</div>

ProHabit's backend is the application's engine, managing logic, storage, and data processing.

- `app.py`: This file is the brain of the application. It's responsible for managing business logic, interacting with the database, and ensuring that information flows correctly between the user and the system. While **Flask** defines routes and handles requests, **SQLAlchemy** efficiently organizes and manipulates data, providing a smooth and intuitive frontend experience. Its main objective is to manage the database (with its **3 tables**) to correctly display information on the frontend, in addition to performing various validations and other essential application functionalities.

---

### Data Storage: SQL
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" height="40" alt="sqlite logo"  />

#### **ProHabit.db**: Database Structure
This database contains **three interconnected tables** that manage each user's data and personalize their experience.

- `users table`: Stores login information for each user.
  - `id`: Primary key, unique identifier for each registered user.
  - `username`: Username for logging in.
  - `password`: Password for logging in, stored in hash format.

- `habits table`: Contains information about each habit per user. This table is linked to the `users` table.
  - `id`: Primary key, unique identifier for each habit registered by the user.
  - `habit`: Description of the habit.
  - `frequency`: How often the habit should be performed (e.g., daily, weekly).
  - `times`: Number of times the habit should be performed within the specified frequency.
  - `user_id`: Foreign key referencing the ID of the logged-in user.

- `habit logs table`: Records the completion of each habit per user.
  - `id`: Primary key, unique identifier for each completion record.
  - `habit_id`: Foreign key referencing the habit's ID for the user.
  - `date`: Date on which the habit's completion was recorded.

## :iphone: Contact
If you have any questions or suggestions, contact me at

- **Gmail:** javier.alvarado3011@gmail.com
- **LinkedIn:** www.linkedin.com/in/carlos-menesess
