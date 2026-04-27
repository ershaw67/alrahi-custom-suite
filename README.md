**Custom Odoo Suite**  
Blueprint Package for Enterprise Customization  This repository serves as a technical demo for customizing Odoo using Python-based model  and XML view definitions. 

### Core Architecture
Module Logic: Developed for Odoo 17.0+ using the native Python framework.  
Frontend Design: XML-based   
Package added for Database(Postgressql)
### Module Components
Manifest (__manifest__.py): Acts as the "Instruction Manual," defining module metadata, dependencies (Accounting & Inventory), and data loading sequences.  
Initialization (__init__.py): Configured to ensure Python treats directories as executable packages during the Odoo registry phase.  
Data Models (models/): Defines the structural schema for data storage, including 6 custom fields for tax compliance and logistics.  
Interface Views (views/): Manages the UI design, providing a seamless user experience through inherited XML layouts.  
### Deployment & CI/CD  
This package is optimized for Odoo.sh integration. By utilizing Webhooks and Deployment Keys, the code is automatically validated and synced from this GitHub repository  
