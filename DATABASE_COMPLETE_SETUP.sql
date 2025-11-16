-- ============================================================================
-- AUTOCRAFT CENTER - COMPLETE ORACLE DATABASE SETUP
-- ============================================================================
-- Version: 1.0
-- Date: November 2025
-- Purpose: Complete database setup for AutoCraft Center Django Application
-- ============================================================================

-- STEP 1: CONNECT AS SYSTEM USER
-- Execute: sqlplus system/<your-password>@localhost:1521/XE

-- Drop existing user and tablespace if they exist (CAUTION: This deletes all data!)
DROP USER autocraft CASCADE;
DROP TABLESPACE autocraftdata INCLUDING CONTENTS AND DATAFILES;

-- Create dedicated tablespace for AutoCraft
CREATE TABLESPACE autocraftdata
  DATAFILE 'autocraftdata.dbf' 
  SIZE 500M 
  AUTOEXTEND ON 
  NEXT 50M 
  MAXSIZE UNLIMITED;

-- Create autocraft user with strong password
CREATE USER autocraft IDENTIFIED BY AutoCraft2025!
  DEFAULT TABLESPACE autocraftdata
  TEMPORARY TABLESPACE temp
  QUOTA UNLIMITED ON autocraftdata;

-- Grant comprehensive privileges
GRANT CONNECT, RESOURCE TO autocraft;
GRANT CREATE SESSION TO autocraft;
GRANT CREATE TABLE TO autocraft;
GRANT CREATE VIEW TO autocraft;
GRANT CREATE SEQUENCE TO autocraft;
GRANT CREATE TRIGGER TO autocraft;
GRANT CREATE PROCEDURE TO autocraft;
GRANT UNLIMITED TABLESPACE TO autocraft;

-- Verify user creation
SELECT username, default_tablespace, account_status 
FROM dba_users 
WHERE username = 'AUTOCRAFT';

-- EXIT;

-- ============================================================================
-- STEP 2: CONNECT AS AUTOCRAFT USER
-- Execute: sqlplus autocraft/AutoCraft2025!@localhost:1521/XE
-- ============================================================================

-- Django will create tables via migrations
-- Expected tables after migrations:
-- 1. django_migrations
-- 2. django_content_type
-- 3. auth_permission, auth_group, auth_group_permissions
-- 4. customusers (Custom User Model)
-- 5. businessinfo
-- 6. contactmessages
-- 7. servicecategories
-- 8. services
-- 9. timeslots
-- 10. bookings
-- 11. gallerycategories
-- 12. galleryimages
-- 13. reviews
-- 14. blogcategories
-- 15. blogposts

-- ============================================================================
-- STEP 3: INITIAL DATA INSERTION (Run AFTER Django migrations)
-- ============================================================================

-- Insert Business Information
INSERT INTO businessinfo (
  id, businessname, tagline, description, phone, email, address, city, country,
  metadescription, metakeywords, 
  mondayhours, tuesdayhours, wednesdayhours, thursdayhours, fridayhours, saturdayhours, sundayhours,
  facebookurl, instagramurl, twitterurl, linkedinurl,
  createdat, updatedat
) VALUES (
  1,
  'AUTOCRAFT CENTER',
  'Your Trusted Auto Repair Partner in Nairobi',
  'Professional automotive repair and maintenance services in Nairobi, Kenya. Expert mechanics, quality service, and customer satisfaction guaranteed.',
  '+254 712 345 678',
  'info@autocraftcenter.co.ke',
  'Mombasa Road, Industrial Area',
  'Nairobi',
  'Kenya',
  'Professional auto repair services in Nairobi. Engine diagnostics, brake services, transmission repair.',
  'auto repair, car service, mechanics, Nairobi, Kenya',
  '8:00 AM - 6:00 PM',
  '8:00 AM - 6:00 PM',
  '8:00 AM - 6:00 PM',
  '8:00 AM - 6:00 PM',
  '8:00 AM - 6:00 PM',
  '9:00 AM - 4:00 PM',
  'Closed',
  'https://facebook.com/autocraftcenter',
  'https://instagram.com/autocraftcenter',
  'https://twitter.com/autocraftcenter',
  'https://linkedin.com/company/autocraftcenter',
  SYSTIMESTAMP,
  SYSTIMESTAMP
);

-- Insert Service Categories
INSERT ALL
  INTO servicecategories (id, name, slug, description, icon, "ORDER", isactive, createdat, updatedat)
    VALUES (1, 'Engine Diagnostics & Repair', 'engine-diagnostics-repair', 'Comprehensive engine diagnostics', 'fas fa-cog', 1, 1, SYSTIMESTAMP, SYSTIMESTAMP)
  INTO servicecategories (id, name, slug, description, icon, "ORDER", isactive, createdat, updatedat)
    VALUES (2, 'Brake System Services', 'brake-system-services', 'Complete brake system service', 'fas fa-car-crash', 2, 1, SYSTIMESTAMP, SYSTIMESTAMP)
  INTO servicecategories (id, name, slug, description, icon, "ORDER", isactive, createdat, updatedat)
    VALUES (3, 'Transmission Services', 'transmission-services', 'Manual and automatic transmission', 'fas fa-gears', 3, 1, SYSTIMESTAMP, SYSTIMESTAMP)
  INTO servicecategories (id, name, slug, description, icon, "ORDER", isactive, createdat, updatedat)
    VALUES (4, 'Suspension & Steering', 'suspension-steering', 'Suspension and steering repair', 'fas fa-car-side', 4, 1, SYSTIMESTAMP, SYSTIMESTAMP)
  INTO servicecategories (id, name, slug, description, icon, "ORDER", isactive, createdat, updatedat)
    VALUES (5, 'Electrical System Repairs', 'electrical-system-repairs', 'Electrical system diagnostics', 'fas fa-bolt', 5, 1, SYSTIMESTAMP, SYSTIMESTAMP)
  INTO servicecategories (id, name, slug, description, icon, "ORDER", isactive, createdat, updatedat)
    VALUES (6, 'General Vehicle Servicing', 'general-vehicle-servicing', 'Routine maintenance', 'fas fa-wrench', 6, 1, SYSTIMESTAMP, SYSTIMESTAMP)
SELECT * FROM dual;

COMMIT;

-- Verification Query
SELECT 'Setup Complete!' as status FROM dual;
