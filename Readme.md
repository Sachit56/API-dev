Django API Project
Overview
This is a Django-based REST API project designed to manage user registration, authentication, and specific forms related to wheel specifications and bogie checksheets. The API supports user management and form submissions with JWT-based authentication for secure access. The project is tested using a Postman collection, detailed in Api Dev.postman_collection.json.
Prerequisites

Python 3.8+
Django 4.x
Django REST Framework
PostgreSQL (or any preferred database)
Postman (for testing API endpoints)
Git

Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd <project-directory>

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file in the project root and add the following:
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
DEBUG=True

5. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Start the Development Server
python manage.py runserver

The API will be available at http://127.0.0.1:8000/.
API Endpoints
The API provides endpoints for user management and form submissions, as detailed in the Api Dev.postman_collection.json Postman collection. Below is a summary of the available endpoints:
User Management

Register User

Method: POST
URL: /api/forms/register/
Description: Registers a new user with details such as email, first name, last name, age, faculty, file upload, and password.
Body: Form-data (e.g., email, first_name, last_name, age, faculty, file, password)
Response: Returns user details on successful registration (HTTP 201).


Login User

Method: POST
URL: /api/forms/login/
Description: Authenticates a user and returns JWT access and refresh tokens.
Body: JSON (e.g., {"email": "user@example.com", "password": "admin"})
Response: Returns refresh_token and access_token (HTTP 200).


Single User Profile

Method: GET
URL: /api/forms/profile/
Description: Retrieves the profile of the authenticated user.
Authentication: Bearer Token (JWT)
Response: Returns user details including student_id, email, first_name, last_name, faculty, age, and file (HTTP 200).


All Users

Method: GET
URL: Not specified in JSON, but inferred as /api/forms/users/ (based on response structure)
Description: Retrieves a list of all registered users.
Authentication: Bearer Token (JWT)
Response: Returns a list of user objects with details (HTTP 200).



Form Submissions

Wheel Specifications (GET)

Method: GET
URL: /api/forms/wheel-specifications/
Description: Retrieves wheel specification details.
Authentication: Bearer Token (JWT)
Response: Returns wheel specification data including formNumber, submittedBy, submittedDate, and detailed fields (HTTP 200).


Wheel Specifications (POST)

Method: POST
URL: /api/forms/wheel-specifications/
Description: Submits a new wheel specification form.
Authentication: Bearer Token (JWT)
Body: JSON with formNumber, submittedBy, submittedDate, and fields (e.g., treadDiameterNew, wheelGauge, etc.)
Response: Returns success message and form details (HTTP 200).


Bogie Checksheet (GET)

Method: GET
URL: /api/forms/bogie-checksheet/
Description: Retrieves bogie checksheet details.
Authentication: Bearer Token (JWT)
Response: Returns a list of bogie checksheet data including formNumber, inspectionBy, inspectionDate, bogieDetails, bogieChecksheet, and bmbcChecksheet (HTTP 200).


Bogie Checksheet (POST)

Method: POST
URL: /api/forms/bogie-checksheet/
Description: Submits a new bogie checksheet form.
Authentication: Bearer Token (JWT)
Body: JSON with formNumber, inspectionBy, inspectionDate, bogieDetails, bogieChecksheet, and bmbcChecksheet.
Response: Returns success message and form details (HTTP 200).



Postman Collection
The Api Dev.postman_collection.json file contains a Postman collection for testing the API endpoints. It includes the following requests:

Register User: POST request with form-data for user registration.
Login User: POST request with JSON body for user authentication.
Single User Profile: GET request to fetch the authenticated user's profile (requires JWT).
All Users: GET request to list all users (requires JWT).
Wheel Specifications (GET): GET request to retrieve wheel specification data (requires JWT).
Wheel Specifications (POST): POST request to submit wheel specification data (requires JWT).
Bogie Checksheet (GET): GET request to retrieve bogie checksheet data (requires JWT).
Bogie Checksheet (POST): POST request to submit bogie checksheet data (requires JWT).

Importing the Postman Collection

Open Postman.
Click Import > File and select Api Dev.postman_collection.json.
Update the base URL if your server runs on a different host or port.
For authenticated endpoints, replace the token in the Bearer Token field with a valid JWT obtained from the Login User endpoint.

Project Structure
project/
├── manage.py
├── requirements.txt
├── .env
├── Api Dev.postman_collection.json
├── <app_name>/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── ...
├── <project_name>/
│   ├── settings.py
│   ├── urls.py
│   └── ...

Notes

Ensure the JWT tokens used in the Postman collection are updated as they expire.
The file upload functionality in the Register User endpoint expects a valid file path on the server.
The API runs on http://127.0.0.1:8000/ by default. Update the URLs in the Postman collection if deploying to a different environment.
The wheel specifications and bogie checksheet endpoints are specific to a domain (e.g., railway or mechanical engineering) and include detailed fields for technical specifications.

Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Create a Pull Request.

License
This project is licensed under the MIT License.