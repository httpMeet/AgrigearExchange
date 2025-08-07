# AgriGear Exchange

**AgriGear Exchange** is a web application developed to modernize and simplify how agricultural tools and equipment are exchanged or distributed among users.

---

## About

AgriGear Exchange is designed to facilitate the seamless exchange of agricultural tools and machinery. Whether you're lending, renting, or trading, this platform is tailored to the needs of the agri-community.

---

## Features

- User authentication (optional: registration, login, profile)
- Listings of agricultural equipment (rent, borrow, exchange)
- Location-based search (leveraging `locations` data)
- Account management (`accounts`)
- Interactive UI with templates & static assets (HTML, CSS/SCSS, JavaScript)

---

## Tech Stack

- Backend: **Python**, **Django** (inferred from `manage.py`, `db.sqlite3`)
- Frontend: **HTML**, **CSS/SCSS**, **JavaScript**
- Database: **SQLite3**
- Additional files:  
  - `states.csv` for state-level data  
  - Media templates and default profile images  
  - `requirements.txt` captures Python dependencies

---

## Getting Started

### Prerequisites

- Python 3.x  
- pip (Python package installer)  
- (Optional) Virtual environment setup tool (`venv`, `virtualenv`)

### Installation

1. Clone this repo:  
   ```bash
   git clone https://github.com/httpMeet/AgrigearExchange.git
   cd AgrigearExchange
   ```
2. Set up a virtual environment and activate it:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

