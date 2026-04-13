# Food Factory Management System (FFMS)
A web-based system to manage ingredient inventory, production batches, quality inspections, and shipment workflows in a food manufacturing unit, ensuring safety compliance and operational traceability.

## Project Overview
The Food Factory Management System (FFMS) is a web-based application designed to manage ingredient inventory, production activities, quality inspections, and shipment processes within a food manufacturing unit. The system provides a centralized platform to monitor and control the complete workflow from raw material receipt to finished goods dispatch.

## Problem it Solves
Food factories often rely on manual records or disconnected tools to manage inventory and quality checks. This creates challenges in tracking ingredient expiry dates, enforcing safety inspections, maintaining batch traceability, and monitoring production status. FFMS addresses these issues by introducing a structured digital workflow that improves operational control and reduces the risk of human error.

## Target Users 
- Inventory Supervisor – manages ingredient batches and stock levels
- Production Manager – plans and monitors production schedules  
- Quality Inspector – performs and records safety inspections  
- Shipping Clerk – handles dispatch of approved finished goods  
- System Administrator – manages users and maintains system records  

## Vision Statement
To develop a centralized system that enforces food safety checkpoints, tracks ingredient freshness, and provides clear visibility into production and inventory operations through an organized digital workflow.

## Key Features
- Ingredient batch tracking with expiry date monitoring  
- Production scheduling based on available inventory  
- Mandatory quality inspection before dispatch  
- Shipment allowed only for approved batches  
- Role-based access control and audit logging  
- Dashboard for monitoring operational activities  

## Success Metrics
- Accurate tracking of ingredient batches and expiry details  
- Enforcement of inspection checkpoints before shipment  
- Improved visibility of inventory and production status  
- Complete traceability of production batches  

## Assumptions & Constraints
- Developed as an academic project using open-source tools  
- Focus on process modeling rather than industrial automation  
- Users have basic computer literacy and internet access  
- Project completion within the academic timeline

## MoSCoW Prioritization

| Must Have | Should Have | Could Have | Won’t Have |
|---|---|---|---|
| Ingredient batch entry with expiry date | Near-expiry ingredient alerts | Generate basic reports | Barcode / QR code scanning |
| View ingredient stock levels | View production batch status | View inspection history | Temperature sensor integration (cold chain) |
| Create production schedule | Generate shipping label | Audit logs for activities | Mobile application support |
| Check ingredient availability before scheduling | Dashboard for monitoring operations |  |  |
| Approve production schedule | Search batch details |  |  |
| Perform quality inspection for each batch |  |  |  |
| Record inspection results |  |  |  |
| Approve or reject batch |  |  |  |
| Update finished goods inventory |  |  |  |
| Dispatch only approved batches |  |  |  |
| Secure role-based login |  |  |  |

## Branching Strategy
- The project adopts the GitHub Flow model for managing development
- The main branch holds the latest stable version of the project
- Separate feature branches are created from main for implementing new features
- Feature branches are named using the format: feature-name (for example, feature-login-ui)
- Changes are developed and tested in the feature branch before creating a Pull Request
- After review, the feature branch is merged into the main branch
- This workflow keeps development organized and maintains code reliability

## Local Development Tools

- **Frontend** – HTML with internal CSS is used to design the user interface for the Food Factory Management System, including login and dashboard screens.

- **Backend** – Python with Flask framework is used to handle routing, request processing, and core business logic of the system.

- **Database** – MySQL is used for storing ingredient batches, production records, inspection results, shipment logs, and user details.

- **Containerization** – Docker Desktop is used to run the backend application in a containerized environment for easy local development.

- **Version Control** – Git and GitHub are used to manage source code, branching, and project workflow.

- **Development Environment** – Visual Studio Code is used as the code editor, and Windows Command Prompt / PowerShell is used to run development commands.

- **Operating System** – Windows 10 / Windows 11

## Software Design

The Food Factory Management System follows a layered client–server architecture
with modular backend services for inventory, production, quality inspection, and
shipping. The design emphasizes high cohesion and low coupling by separating
core functionalities into independent modules. This approach improves system
maintainability, scalability, and ease of future enhancements.

### Architecture Diagram
<img width="932" height="729" alt="image" src="https://github.com/user-attachments/assets/e3ff69ac-0dc2-4b7a-b479-2dce39dbcdc1" />

### Design Artifacts

- **Architecture Diagram:**  
  [View Diagram](design/System_archi_diagram_(draw.io).png)

- **ER Diagram:**  
  [View Diagram](design/ER_diag.jpeg)

- **Use Case Diagram:**  
  [View Diagram](design/use_case_diagram.png)

- **Activity Diagram:**  
  [View Diagram](design/Activity_diagram.png)

- **UI Wireframes:**
  - [Login Screen](design/Figma_Login_screen.png)
  - [Inventory Dashboard](design/Figma_Inventory_dashboard_screen.png)
  - [Production Schedule](design/Figma_Production_Schedule_Screen.png)
  - [Quality Inspection](design/Figma_Quality_Inspection_screen.png)
  - [Shipping & Dispatch](design/Figma_Shipping_Dispatch_Screen.png)
  - [Admin Panel](design/Figma_Admin_Panel_Screen.png)

## Quick Start – Local Development

Follow these steps to run the Food Factory Management System on your local machine using Docker.


### Prerequisites

- Install Docker Desktop
- Install Git
- Web Browser (Chrome/Edge/Firefox)

### Step 1 – Clone the repository

```
git clone https://github.com/vars16/Food_Factory_Management_System.git
cd Food_Factory_Management_System
```

### Step 2 – Navigate to backend folder

```
cd backend
```

### Step 3 – Build Docker image

```
docker build -t ffms-backend .
```

### Step 4 – Run Docker container

```
docker run -p 5000:5000 ffms-backend
```

### Step 5 – Open in browser

Open your browser and go to:

```
http://127.0.0.1:5000
```

The Food Factory Management System should now be running successfully on your local machine.




