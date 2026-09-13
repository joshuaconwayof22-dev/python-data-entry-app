# Python Data Entry App

A Python coursework application built with Tkinter that collects contact information, performs basic validation, and saves accepted entries to a CSV file.

## Features

- Collect name, email, phone, address, city, state, and ZIP code.
- Reject blank required fields.
- Check that emails contain an @ symbol and a period.
- Require at least 10 digits in phone numbers.
- Require two letters for the state and five digits for the ZIP code.
- Append accepted entries to people_data.csv.
- Display a success message and clear the form after saving.

These are basic format checks; they do not verify that contact details exist.

## Requirements

- Python 3 with Tkinter support.
- No third-party Python packages required.

Tkinter is normally included with Python on Windows.
Tested with Python 3.13 on Windows using PyCharm.

## How to Run

Open data_entry_app.py in PyCharm and select Run.

Alternatively, open a terminal in the project folder and run:

```text
python data_entry_app.py
```

## Saved Data

The application creates people_data.csv in the current working directory when the first valid entry is submitted.

Each submission adds a row in this order:

Name, email, phone, address, city, state, ZIP code.

The CSV does not include a header row. Existing records are preserved.

Generated records are excluded from Git tracking through .gitignore.

## Skills Practiced

- Tkinter widgets and grid layouts
- Button callbacks
- Functions and conditional logic
- String validation
- CSV file writing
- File error handling

## Limitations

This is a learning project. Records are stored as plain text in a local CSV file. It does not provide encryption, user accounts, or tools for editing saved records.