# University of Ghana Campus Job Market Platform

**ICT Project Plan: Integration and Scope Management – Group 15**

## Team Members
| Name | ID |
| :--- | :--- |
| Ebenezer Fuachie | 22129348 |
| Richmond Nkansah Duodu | 22122528 |
| Horaya Razak | 22236215 |
| Opoku Ransford | 22041329 |
| Gyasi Amos Kwadwo | 22245133 |
| Nartey Godwin Odimera | 22016934 |
| Vordey Dzidzor Adzo | 22052103 |
| Apeagyei Nathaniel Nana Yaw Asare | 11248990 |

## 1. Project Description
This project aims to design and develop a web-based job marketplace specifically for students and employers within the University of Ghana campus. The system will allow students to create profiles, upload CVs, and apply for part-time, internship, and campus-based job opportunities. Employers (campus units and verified businesses) can post job listings and manage applications. The platform will enhance employability, reduce information gaps, and create structured access to opportunities within the university environment.

### b) Stakeholders and Roles
- **Project Sponsor:** University authority or department providing approval
- **Project Manager:** Oversees planning, execution, and monitoring.
- **Development Team:** Designs and builds the platform.
- **Students:** End users applying for jobs.
- **Employers:** Post job opportunities.
- **System Administrator:** Manages platform operations.

## 2. Project Scope Management

### a) Detailed Scope Statement
**Included:**
- User registration and authentication system.
- Job posting and application management.
- Admin dashboard.
- Profile management and CV upload.

**Excluded:**
- Payment processing system.
- Mobile native application.
- Integration with external national job platforms.

### c) Key Project Requirements
1. Secure authentication with encrypted passwords.
2. Role-based access control.
3. Search and filter job listings.
4. Application tracking feature.
5. Administrative reporting dashboard.



## 4. Project Structure
The platform is built using the Django framework.
- `manage.py`: Django's command-line utility for administrative tasks.
- `ugjobs/`: Main project configuration directory (settings, urls, wsgi/asgi).
- `users/`: Django app managing user registration, authentication, and profiles.
- `requirements.txt`: Project dependencies list.
- `.env_example.py`: Environment variables template (copy this to `.env` or set manually).

## 5. Setup and Installation

### Prerequisites
- Python 3.8+
- PostgreSQL (or an equivalent database depending on configuration)
- pip and virtualenv

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd UG-Student-Job
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables Configuration:**
   Copy the structure provided in `.env_example.py` to create your own configuration. Set your `SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT`.

5. **Run Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

## 6. How to Run

1. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```
2. **Access the platform:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.
