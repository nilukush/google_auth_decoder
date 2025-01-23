def format_entries(input_file):
    with open(input_file, 'r') as f:
        content = f.read()

    entries = content.split('--------------------------------------------------')

    print("=== KeePassXC TOTP Entries ===")
    print("For each entry:")
    print("1. Create new entry")
    print("2. Set these standard settings:")
    print("   - Time step: 30 seconds")
    print("   - Code length: 6 digits")
    print("   - Algorithm: SHA-1\n")

    for entry in entries:
        if not entry.strip():
            continue

        lines = entry.strip().split('\n')
        entry_data = {}

        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                entry_data[key.strip()] = value.strip()

        if 'Name' not in entry_data or 'Secret' not in entry_data:
            continue

        print("\n=== New Entry ===")
        print(f"Title: {entry_data.get('Issuer', 'Unknown')} - {entry_data['Name']}")
        print(f"Username: {entry_data['Name']}")
        print(f"TOTP Secret (copy this exactly): {entry_data['Secret']}")
        print("-" * 40)


if __name__ == "__main__":
    format_entries("totp_entries.txt")  # Save your output in this file