🗂️ Task Manager
A command-line based task management system for assigning, tracking, editing, and completing tasks. This application supports admin and regular user roles, enabling efficient task delegation and monitoring in a multi-user environment.

📦 Features
User Authentication
Login system using a user.txt file for storing credentials.

Admin Capabilities

Register new users

Delete tasks

View completed tasks

View user/task statistics

Generate reports

General User Capabilities

Add new tasks

View all tasks

View and edit your tasks

Mark tasks as complete

Reporting
Auto-generates task_overview.txt and user_overview.txt with detailed task statistics.

📁 File Structure
task_manager.py – Main Python script.

user.txt – Stores user credentials in username, password format.

tasks.txt – Stores all tasks.

task_overview.txt – Auto-generated report on all tasks.

user_overview.txt – Auto-generated report on all users and their tasks.

🛠️ How It Works
📥 Login
Upon running, users are prompted to enter their credentials. They are allowed 3 attempts. Admins have access to additional features.

➕ Add Task
Users can add tasks by inputting:

Username of assignee

Task title

Description

Due date (format: dd-mm-yyyy)

👁️ View Tasks
All Tasks: Displayed for review by any user.

My Tasks: Logged-in user can view, edit, or mark as complete.

Completed Tasks: Deleted tasks tracked for future reference.

📊 Reports
Admins can generate and display:

Total tasks

Completed, incomplete, and overdue tasks

Per-user statistics including percentage breakdowns

✅ Requirements
Python 3.7+

No external libraries (uses built-in modules only)

