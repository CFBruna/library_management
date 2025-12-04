# Library Management System

## About the Project

This is a Library Management System project developed with Django. The platform allows comprehensive management of books, authors, categories, patrons, and loan control, all with a robust authentication and permissions system.

The goal was to build a complete and functional web application, applying concepts learned in my journey with Python and Django, while exploring modern tools to optimize the development cycle.

## Main Features

* **Catalog Management:** Complete CRUD for Books, Authors, and Categories.
* **Patron Control:** Registration and management of patron information.
* **Loan System:**
    * New loan registration with automatic book inventory updates.
    * Return registration.
    * Separate listings for active and returned loans.
    * Smart search by book, patron name, or CPF (Brazilian ID).
* **Authentication and Permissions:** The system uses Django's authentication and permissions system to control access to different functionalities, ensuring only authorized users can perform certain actions.

## Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5
* **Database:** PostgreSQL (configured to run with Docker)
* **Testing:** Pytest, Pytest-Django
* **Containerization:** Docker, Docker Compose
  
[▶️ Click here to watch the video demonstration](https://youtu.be/Tbng-8h86uc)

## How to Run the Project Locally

The project is containerized with Docker, making environment setup easier.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CFBruna/library_management.git
    cd library_management
    ```

2.  **Configure environment variables:**
    * Rename the `.env.example` file to `.env`.
    * If desired, modify the values inside the `.env` file (not strictly necessary to run locally, but it's a good practice).

3.  **Start the containers with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

4.  **Access the application:**
    * Open your browser and navigate to `http://localhost:8000`.

## My Development Process and the Role of AI

From the beginning, my goal was not just to build a project, but also to optimize the process. I was responsible for the entire application architecture: I designed the `models`, structured the `views` with business logic, and defined permission rules.

In this process, I used Artificial Intelligence tools as a development assistant. Instead of spending time on repetitive tasks, I directed the AI to:

* **Generate automated tests:** With my knowledge of what needed to be tested, I guided the AI to create unit and integration tests with Pytest, which accelerated code quality assurance.
* **Structure the frontend:** The `base.html` template and other templates were generated with AI assistance, following the design guidelines I established.
* **Configure the deployment environment:** I used AI to help write the `Dockerfile` and `docker-compose.yml`, based on my project requirements.

I believe that the most important skill of a modern developer is knowing how to translate a business need into a functional technical solution, using the best and most efficient tools available. This project is a reflection of that philosophy.
