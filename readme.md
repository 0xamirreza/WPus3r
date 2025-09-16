# WordPress User Enumeration Tool

A simple Python script that enumerates user accounts on WordPress sites by querying the REST API endpoint.

## Features

- Automatically normalizes domain names (adds https:// and www. if needed)
- Checks for required dependencies (curl and jq)
- Extracts and displays WordPress user slugs from the API response
- Provides clear error messages for common issues

## Prerequisites

- Python 3.x
- curl (command-line tool)
- jq (JSON processor)

### Install Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get install curl jq
```

**macOS:**
```bash
brew install curl jq
```

## Usage

1. Clone or download the script
2. Run the script:
```bash
python3 wpus3r.py
```
3. Enter the target domain when prompted (e.g., `example.com`)

## Example

```bash
$ python3 wordpress_user_enum.py
Enter the domain (e.g., example.com): example.com
Connecting...

Data retrieved successfully.
-----------------------------------------------
User found:
1. admin
2. editor
3. author
```

## Note

This tool is for educational and security assessment purposes only. Only use it on websites you own or have permission to test.

## License

This project is provided for educational purposes.
