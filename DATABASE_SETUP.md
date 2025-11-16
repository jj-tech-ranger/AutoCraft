# AUTOCRAFT CENTER - DATABASE SETUP GUIDE

## Overview
This document provides complete instructions for setting up the Oracle database for AutoCraft Center.

## Prerequisites
- Oracle Database 11g or higher (Oracle XE recommended for development)
- SQL*Plus or Oracle SQL Developer
- Admin/SYSTEM user access

## Part 1: Initial Database Setup

### Step 1: Create User and Tablespace

Connect as SYSTEM user:
```bash
sqlplus system/<your_password>@localhost:1521/XE
```

Run the following SQL:

```sql
-- Drop existing user if recreating (CAUTION: Deletes all data)
DROP USER autocraft CASCADE;
DROP TABLESPACE autocraftdata INCLUDING CONTENTS AND DATAFILES;

-- Create tablespace
CREATE TABLESPACE autocraftdata
  DATAFILE 'autocraftdata.dbf'
  SIZE 200M
  AUTOEXTEND ON
  NEXT 10M
  MAXSIZE UNLIMITED;

-- Create user
CREATE USER autocraft IDENTIFIED BY AutoCraft2025!
  DEFAULT TABLESPACE autocraftdata
  TEMPORARY TABLESPACE temp
  QUOTA UNLIMITED ON autocraftdata;

-- Grant privileges
GRANT CONNECT, RESOURCE TO autocraft;
GRANT CREATE SESSION TO autocraft;
GRANT CREATE TABLE TO autocraft;
GRANT CREATE VIEW TO autocraft;
GRANT CREATE SEQUENCE TO autocraft;
GRANT CREATE TRIGGER TO autocraft;
GRANT CREATE PROCEDURE TO autocraft;
GRANT UNLIMITED TABLESPACE TO autocraft;

-- Verify
SELECT username, default_tablespace, account_status
FROM dba_users WHERE username = 'AUTOCRAFT';

EXIT;
```

## Part 2: Django Models Will Create Tables

After setting up the user, Django migrations will create all necessary tables.

### Run Django Migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates:
- customusers (Custom user model with roles)
- businessinfo
- contactmessages  
- servicecategories
- services
- timeslots
- bookings
- gallerycategories
- galleryimages
- reviews
- blogcategories
- blogposts

## Part 3: Insert Sample Data

Connect as autocraft user:
```bash
sqlplus autocraft/AutoCraft2025!@localhost:1521/XE
```

See SAMPLE_DATA.sql file for complete data insertion scripts.

## Part 4: Create Test Users

After migrations, create test users using Django management command:

```bash
python manage.py shell
```

Then in Python shell:
```python
from django.contrib.auth import get_user_model
User = get_user_model()

# Create Admin
admin = User.objects.create_superuser(
    email='admin@autocraftcenter.co.ke',
    password='Admin2025',
    first_name='Admin',
    last_name='User',
    phone='+254700000001',
    role='admin'
)

# Create Staff
staff = User.objects.create_user(
    email='staff@autocraftcenter.co.ke',
    password='Staff2025',
    first_name='Staff',
    last_name='Member',
    phone='+254700000002',
    role='staff',
    is_staff=True
)

# Create Client
client = User.objects.create_user(
    email='client@autocraftcenter.co.ke',
    password='Client2025',
    first_name='Test',
    last_name='Client',
    phone='+254700000003',
    role='client'
)

exit()
```

## Database Connection Settings

In your .env file:
```
ORACLE_DB_NAME=XE
ORACLE_DB_USER=autocraft
ORACLE_DB_PASSWORD=AutoCraft2025!
ORACLE_DB_HOST=localhost
ORACLE_DB_PORT=1521
```

## Troubleshooting

### Connection Issues:
```sql
-- Check if Oracle is running
lsnrctl status

-- Test connection
sqlplus autocraft/AutoCraft2025!@localhost:1521/XE
```

### Check Tables:
```sql
SELECT table_name FROM user_tables ORDER BY table_name;
```

### Check Data:
```sql
SELECT COUNT(*) FROM customusers;
SELECT COUNT(*) FROM bookings;
SELECT COUNT(*) FROM services;
```

## Next Steps

1. ✅ Create Oracle user and tablespace
2. ✅ Configure Django settings with Oracle credentials  
3. ✅ Run Django migrations
4. ✅ Create test users
5. ✅ Insert sample data
6. ✅ Test application login

## Important Notes

- Default password for all test users: See above
- Change passwords in production
- Backup database regularly
- Use environment variables for credentials
- Never commit .env file to version control
