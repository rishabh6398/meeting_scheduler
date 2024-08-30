# Meeting Scheduler
## Description
The Meeting Scheduler is a web application designed to efficiently manage and schedule meetings. It supports single-person meetings, complex scenarios with multiple participants, and room bookings. Built with Flask and PostgreSQL, the application provides an intuitive interface for creating, viewing, updating, and deleting meeting schedules while minimizing scheduling conflicts.

## Features
Single-Person Meetings: Schedule meetings with individual participants.
Multi-Person Meetings: Manage meetings involving multiple participants.
Room Accommodations: Book and manage rooms for meetings.
CRUD Operations: Create, Read, Update, and Delete meetings.
Conflict Detection: Avoid scheduling conflicts with existing meetings.
User Interface: Simple and user-friendly web interface.
Technology Stack
Backend: Flask (Python)
Database: PostgreSQL
## Setup
### Prerequisites
Python 3.x
PostgreSQL
### Installation

Clone the Repository-

git clone <repository-url>  
cd meeting-scheduler  

Install Dependencies-

pip install -r requirements.txt  

Setup PostgreSQL Database-

Create a PostgreSQL database and user.  
Update the database connection settings in config.py.

Run Migrations-

flask db upgrade  

Run the Application-

flask run

### Configuration

Edit the config.py file to configure your PostgreSQL database credentials and other settings.  

### Usage

Navigate to http://localhost:5000 in your web browser to access the application.  
Use the interface to schedule and manage meetings.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with a clear description of your changes.

## Contact

For questions or support, contact Hrishabh Dubey at rishabh6398@gmail.com.

