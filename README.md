# WorkContacts

A command-line contact management application built with Python.

WorkContacts allows users to manage personal and professional contacts through an interactive terminal interface powered by Rich.

## Features

- **Add contacts:** Create contacts with personal and professional information.
- **List contacts:** Display contacts in an organized table.
- **Search contacts:** Find contacts using their email address.
- **Update contacts:** Modify existing contact information.
- **Delete contacts:** Remove contacts from the application.
- **Category filtering:** Filter contacts by personal or work category.
- **Statistics:** View contact statistics and summaries.
- **JSON persistence:** Automatically save and load contact information.
- **Backup and restore:** Create backups and restore previously saved contacts.
- **CSV export:** Export contacts to CSV files compatible with Excel.
- **CSV import:** Import contacts from CSV files, avoiding duplicates and rejecting invalid records.

## Technologies

- Python
- Rich
- Pytest
- CSV
- JSON
- Git

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd workcontacts
```

Create and activate a virtual environment:

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the project:

```powershell
python -m pip install -e .
```

## Usage

Launch the application:

```powershell
workcontacts
```

Follow the interactive menu to manage your contacts.

## Running tests

Run the complete test suite:

```powershell
python -m pytest
```

## Project structure

```text
workcontacts/
├── src/
│   └── workcontacts/
│       ├── models/
│       ├── utils/
│       ├── cli.py
│       ├── manager.py
│       ├── storage.py
│       └── export.py
├── tests/
├── README.md
├── pyproject.toml
└── requirements.txt
```

## Project status

Actively developed as a Python learning and software engineering project.

The project includes automated tests covering contact management, validation, storage and CSV functionality.