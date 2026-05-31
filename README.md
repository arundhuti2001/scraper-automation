# scraper-automation

# AMC Notice Scraper Automation

## Overview

This project automates the collection and download of notices, addendums, and investor documents from multiple Asset Management Company (AMC) websites.

Using Selenium-based web scraping, the solution navigates dynamic websites, identifies PDF documents, and automatically downloads the latest files into organized folders for further processing and compliance tracking.

---

## Features

* Automated AMC website scraping
* Dynamic webpage handling using Selenium
* Automatic PDF link detection
* Bulk PDF download automation
* Multi-AMC support
* Folder-wise document organization
* Duplicate link removal
* Automatic scrolling for dynamic content loading

---

## Supported Asset Management Companies

* HSBC Mutual Fund
* Nippon India Mutual Fund
* Aditya Birla Sun Life Mutual Fund
* Axis Mutual Fund
* Quantum Mutual Fund

---

## Technologies Used

* Python
* Selenium
* Requests
* BeautifulSoup
* WebDriver Manager
* ChromeDriver

---

## Workflow

1. Open AMC websites automatically.
2. Load dynamic content using Selenium.
3. Scroll pages to retrieve all available documents.
4. Extract PDF links.
5. Remove duplicate URLs.
6. Identify latest available documents.
7. Download PDF files automatically.
8. Organize downloads by AMC.

---

## Project Structure

```text
AMC-Notice-Scraper/
│
├── input/
│
├── AMC_Notices/
│   ├── HSBC_AMC/
│   ├── Nippon_AMC/
│   ├── Birla_AMC/
│   ├── Axis_AMC/
│   └── Quantum_AMC/
│
└── main.py
```

## Installation

```bash
pip install selenium requests beautifulsoup4 webdriver-manager
```

## Requirements

* Python 3.x
* Google Chrome
* ChromeDriver (managed automatically)

## Run

```bash
python main.py
```

---

## Output

The automation downloads PDF documents into AMC-specific folders:

* HSBC_AMC
* Nippon_AMC
* Birla_AMC
* Axis_AMC
* Quantum_AMC

Each folder contains the latest notices and addendums available on the respective AMC website.

---

## Business Applications

* Mutual Fund Operations
* Compliance Monitoring
* Regulatory Document Collection
* Investment Research
* Financial Data Gathering
* Asset Management Reporting
* Document Archival Automation

---

## Benefits

* Eliminates manual document collection
* Saves research and compliance time
* Ensures timely access to latest notices
* Supports automated document monitoring
* Scalable for additional AMCs
