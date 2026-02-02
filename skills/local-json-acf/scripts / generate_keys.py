#!/usr/bin/env python3
"""
ACF Key Generator
Generates unique keys for ACF field groups, fields, and layouts
"""

import random
import string
import sys

def generate_hash(length=6):
    """Generate a random alphanumeric hash"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def to_snake_case(text):
    """Convert text to snake_case"""
    # Replace spaces and common separators with underscores
    text = text.replace(' ', '_').replace('-', '_')
    # Remove special characters except underscores
    text = ''.join(c for c in text if c.isalnum() or c == '_')
    # Convert to lowercase
    text = text.lower()
    # Remove multiple consecutive underscores
    while '__' in text:
        text = text.replace('__', '_')
    return text.strip('_')

def generate_group_key(name):
    """Generate a unique group key"""
    snake_name = to_snake_case(name)
    hash_suffix = generate_hash()
    return f"group_{snake_name}_{hash_suffix}"

def generate_field_key(name):
    """Generate a unique field key"""
    snake_name = to_snake_case(name)
    hash_suffix = generate_hash()
    return f"field_{snake_name}_{hash_suffix}"

def generate_layout_key(name):
    """Generate a unique layout key"""
    snake_name = to_snake_case(name)
    hash_suffix = generate_hash()
    return f"layout_{snake_name}_{hash_suffix}"

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_keys.py <type> <name>")
        print("Types: group, field, layout")
        print("Example: python generate_keys.py field 'Hero Title'")
        sys.exit(1)
    
    key_type = sys.argv[1].lower()
    name = ' '.join(sys.argv[2:])
    
    if key_type == 'group':
        print(generate_group_key(name))
    elif key_type == 'field':
        print(generate_field_key(name))
    elif key_type == 'layout':
        print(generate_layout_key(name))
    else:
        print(f"Unknown type: {key_type}")
        print("Valid types: group, field, layout")
        sys.exit(1)

if __name__ == "__main__":
    main()