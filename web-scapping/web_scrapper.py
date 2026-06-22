from playwright.sync_api import sync_playwright

def whois_lookup(domain_url: str | None = None) -> str | None:
    """
    Fetches WHOIS data for the given domain using whois.com via Playwright.
    
    Args:
        domain_url (str | None): Domain name to look up.

    Returns:
        str | None: List of text lines from the WHOIS page, or None on error.
    """
    if not domain_url:
        print("❌ Error: No Domain url provided")
        return None
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("http://www.whois.com/")
            page.get_by_placeholder("Enter Domain or IP").type(domain_url, delay=300)
            page.keyboard.press("Enter")
            contents = page.locator(".whois-data").inner_text().split('\n')
            browser.close()
            return contents
        except Exception as ex:
            print(f"❌❌ Failed due to the error:\n{str(ex).splitlines()[0]}")
            return None

def clean_whois_data(data: str | None = None) -> dict[str, str | list[str]] | None:
    """
    Processes raw WHOIS lines into a dictionary of registrar details.

    Args:
        data (str | None): Raw WHOIS data as list of text lines.

    Returns:
        dict[str, str | list[str]] | None: Parsed registrar information, or None on empty input.
    """
    if not data:
        return None
    registrar_details = {}
    current_key = None
    for line in data:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            current_key = line[:-1].lower().replace(" ", "_")
            registrar_details[current_key] = []
        else:
            if current_key:
                registrar_details[current_key].append(line)
    return registrar_details

def flatten_whois_data(data: dict[str, list[str]] | None = None) -> dict[str, str | list[str]] | None:
    """
    Flattens parsed WHOIS fields: converts single-item lists to strings.

    Args:
        data (dict[str, list[str]] | None): Parsed registrar info.

    Returns:
        dict[str, str | list[str]] | None: Flattened registrar info, or None on empty input.
    """
    if not data:
        return None
    final_data = {}
    for key, value in data.items():
        final_data[key] = value[0] if len(value) == 1 else value
    return final_data

def get_required_data(data: dict[str, str | list[str] | None]) -> dict[str, str | list[str]] | None:
    """
    Removes all fields except for a selected list of important WHOIS fields.

    Args:
        data (dict[str, str | list[str] | None]): WHOIS data.

    Returns:
        dict[str, str | list[str]] | None: Filtered WHOIS data with selected fields, or None if data is empty.
    """
    if not data:
        print("The data has no fields")
        return None
    FIELDS_TO_PERSERVE = [
        "domain", "registered_on",
        "expires_on", 
        "updated_on", 
        "registrar",
        "registrant_organization",
        "registrant_country",
        "status"
    ]
    filtered_results = {}
    for key, value in data.items():
        if key in FIELDS_TO_PERSERVE:
            filtered_results[key] = value
    return filtered_results

def end_product(domain_url):
    try:
        raw_whois_results = whois_lookup(domain_url)
        cleaned_data = clean_whois_data(raw_whois_results)
        flatten_results = flatten_whois_data(cleaned_data)
        final_product = get_required_data(flatten_results)
        print("✅✅✅ Success! Your request was processed")
        return final_product
    except Exception as ex:
        print(f"❌❌ Error: Failed due to the error:\n{str(ex).splitlines()[0]}")
        
if __name__ == "__main__":
    print(end_product("utoronto.ca"))
