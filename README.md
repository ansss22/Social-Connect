# SocialConnect Django Project

Monface is a Django-based web application that manages user profiles, including students and employees, along with a messaging system and other related functionalities. Users can log in, create their profiles, and interact with other users, including managing friendships and sending messages.

## Features
* Login & Registration: Users can log in using their email and password.
* Profile Management: Both students and employees can create and edit their profiles.
* Messaging System: Users can send and receive messages.
* Friendship Management: Users can connect with each other as friends.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/monface.git
cd monface
```

2. Create a virtual environment:
```bash
python -m venv env
```
3. Activate the virtual environment:
* On Windows:
```bash
env\Scripts\activate
```
* On macOS/Linux
```bash
source env/bin/activate
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
5. Apply database migrations:
```bash
python manage.py migrate
```
6. Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to create the superuser.

7. Run the server:
```bash
python manage.py runserver
```
8. Open your browser and visit http://127.0.0.1:8000/ to view the application.

## Usage

- Login: Users can log in by entering their email and password.
- Create Profile: Students and employees can fill out a form to create or update their profiles.
- Messaging: Users can send and receive messages through the messaging system.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
