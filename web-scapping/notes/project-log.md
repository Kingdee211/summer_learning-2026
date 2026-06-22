# Web Scraping Notes — June 21, 2026

## What I Learned

### Playwright & WSL

* Fixed Playwright browser launch issues caused by missing Linux dependencies.
* Learned that Playwright requires both browser binaries and system libraries.

### Playwright vs HTTPX

* **Playwright:** Used for JavaScript-rendered pages and browser interactions.
* **HTTPX:** Used for fast HTTP requests when browser rendering is unnecessary.

### WHOIS Scraper

* Automated WHOIS searches using Playwright.
* Located the search field, entered domains, and submitted searches.
* Extracted WHOIS data from the results page.

### Data Cleaning

* Converted raw WHOIS text into structured Python dictionaries.
* Removed unnecessary fields and kept only high-value information:

  * Domain
  * Registration Date
  * Expiry Date
  * Updated Date
  * Registrar
  * Status

### Pydantic Validation

* Created a `RegistrationData` model to validate scraped data.
* Learned that Pydantic can automatically convert ISO date strings (`YYYY-MM-DD`) into `date` objects.
* Debugged validation errors caused by passing single-item lists instead of strings.

## Current Output

```python
{
    "domain": "abc.com",
    "registered_on": "1996-05-22",
    "expires_on": "2027-05-23",
    "updated_on": "2026-04-23",
    "status": [
        "client transfer prohibited",
        "server delete prohibited",
        "server transfer prohibited",
        "server update prohibited"
    ],
    "registrar": "CSC Corporate Domains, Inc."
}
```

## Next Steps

* Flatten parser output consistently.
* Validate records using Pydantic.
* Store results in PostgreSQL.
* Add Redis caching.
* Build a FastAPI endpoint for WHOIS lookups.

## Key Accomplishment

Built the foundation of a **Domain Intelligence Service** that extracts, cleans, and validates WHOIS data for future storage and analysis.
