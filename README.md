# AutoCraft Garage Management System

A comprehensive garage management system built with Django and Oracle Database.

## Project Overview

AutoCraft is a full-featured garage management system that handles:

- **Customer Management** - Track customer information and their vehicles
- **Vehicle Tracking** - Maintain detailed vehicle records and service history
- **Service Catalog** - Manage available services with pricing
- **Repair Job Management** - Track repair jobs, assignments, and status
- **Parts Inventory** - Monitor spare parts stock levels and suppliers
- **Employee Management** - Manage staff, mechanics, and their specializations
- **Billing & Payments** - Generate invoices and track payment status

## Technology Stack

- **Backend**: Django 5.2
- **Database**: Oracle XE 21c
- **Frontend**: HTML5, CSS3, JavaScript
- **Database Driver**: cx-Oracle 8.3.0

## Brand Colors

- Primary: #160078 (Deep Purple)
- - Secondary: #5a6782 (Slate Gray)

### Prerequisites

- Python 3.8+
- Oracle Database XE 21c
- Virtual Environment

### Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/jj-tech-ranger/AutoCraft.git
cd AutoCraft
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure database settings in `AutoCraft/settings.py`

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Create user groups
```bash
python manage.py creategroups
```

8. Run development server
```bash
python manage.py runserver
```

## User Roles

### Admin
- Full system access
- User management
- All CRUD operations
- Reports and analytics

### Staff
- Customer CRUD operations
- Vehicle registration
- Repair job creation
- Parts inventory updates
- Bill generation

### Client
- View own vehicles
- View service history
- View bills and payment status
- Update contact information

## License

This project is licensed under the MIT License.

## Author

jj-tech-ranger
