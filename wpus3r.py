import subprocess
import json
import sys

# Check for required tools
def check_required_tools():
    try:
        subprocess.check_call(['curl', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.check_call(['jq', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Error: This script requires 'curl' and 'jq' to be installed.")
        sys.exit(1)

# Normalize domain and construct full URL
def normalize_domain(domain):
    # Check if the domain already has 'http', 'https' or 'www'
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain  # Default to https if none provided

    # Ensure that 'www.' is included for common convention
    if not domain.startswith('www.') and '.' in domain.split('//')[-1]:
        domain = domain.replace("://", "://www.", 1)  # Add 'www.' if it's not present

    return domain

# Prompt for site URL (just the domain)
site = input("Enter the domain (e.g., example.com): ").strip()

# Normalize URL
site = normalize_domain(site)

# Set API endpoint
endpoint = f"{site}/wp-json/wp/v2/users"

# Check for required tools
check_required_tools()

# Fetch JSON and extract slug values
try:
    # Connect and fetch data from the endpoint
    print("Connecting...")
    response = subprocess.check_output(['curl', '-s', endpoint])

    # Parsing the response
    print("\nData retrieved successfully.\n-----------------------------------------------")
    data = json.loads(response)

    if data:
        print("User found:")
        for idx, user in enumerate(data, start=1):
            print(f"{idx}. {user.get('slug')}")
    else:
        print(f"Error: No valid data found at {endpoint}")
        sys.exit(1)

except subprocess.CalledProcessError:
    print(f"\nError: Failed to fetch data from {endpoint}")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"\nError: Failed to decode JSON response from {endpoint}")
    sys.exit(1)
