# DjangoRestApiAssignment - Hotel Reservation System API

This repository contains a Django REST Framework application for managing hotel reservations. It includes API endpoints for retrieving a list of hotels and adding new hotels to the database.

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework
- Other dependencies listed in `requirements.txt`

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/A00476517/DjangoRestApiAssignment.git
cd DjangoRestApiAssignment/hotel_reservation
```

### 2. Install Dependencies

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Database

Run migrations to set up your database:

```bash
python manage.py migrate
```

### 4. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```
The server will start running on http://127.0.0.1:8000/.

### API Endpoints
The application provides the following API endpoints:

# GET /api/hotels/
Retrieve a list of all hotels in the database.

Example request:
```bash
curl -X GET http://127.0.0.1:8000/api/hotels/ -H "Accept: application/json"
```

# POST /api/hotels/

Add a new hotel to the database.

Example request:
```bash
curl -X POST http://127.0.0.1:8000/api/hotels/ \
     -H "Content-Type: application/json" \
     -d '{"name": "New Hotel", "location": "New Location", "stars": 4, "total_rooms": 75}'
```
# Screenshots
![Screenshot (1243)](https://github.com/A00476517/DjangoRestApiAssignment/assets/144840145/16767ecb-3910-46a7-9517-cf04d88a708f)
