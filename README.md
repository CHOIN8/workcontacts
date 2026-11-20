# WorkContacts
[![Tests](https://github.com/CHOIN8/workcontacts/actions/workflows/tests.yml/badge.svg)](https://github.com/CHOIN8/workcontacts/actions/workflows/tests.yml)

A Python command-line application for managing personal and professional contacts.

WorkContacts provides an interactive terminal interface to create, search, update, delete, import, and export contacts.

## Features

- **Contact management:** Add, list, search, update, and delete contacts.
- **Category filtering:** Organize contacts into personal and professional categories.
- **Statistics:** View contact statistics and summaries.
- **JSON persistence:** Automatically save and load contact information.
- **Backup and restore:** Create backups and restore saved contact data.
- **CSV export:** Export contacts to CSV files compatible with Excel.
- **CSV import:** Import contacts from CSV files with duplicate detection and invalid-record handling.
- **Input validation:** Validate contact information before saving.

## Technologies

- Python
- Rich
- Pytest
- JSON
- CSV
- Git and GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/CHOIN8/workcontacts.git
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

Start the application:

```powershell
workcontacts
```

Follow the interactive menu to manage your contacts.

## Running tests

Run the complete test suite:

```powershell
python -m pytest
```

The project includes automated tests covering contact management, validation, JSON storage, and CSV import/export.

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

WorkContacts is an actively developed Python learning and software engineering project.

Contributions, suggestions, and feedback are welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.