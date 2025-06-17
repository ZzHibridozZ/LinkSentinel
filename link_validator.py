import os
import re
import requests
import argparse
from pathlib import Path

# Timeout for HTTP requests
REQUEST_TIMEOUT = 5

def find_links_in_file(filepath):
    links = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

        # Find Markdown links: [text](url)
        md_links = re.findall(r'\[.*?\]\((http[s]?://.*?)\)', content)
        links.extend(md_links)

        # Find reStructuredText links: `text <url>`_
        rst_links = re.findall(r'`[^`<]*<((http[s]?://[^>]*)?)>`_', content)
        links.extend(rst_links)

    return links

def check_link(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=REQUEST_TIMEOUT)
        if response.status_code >= 400:
            return False, response.status_code
        return True, response.status_code
    except requests.RequestException as e:
        return False, str(e)

def scan_directory(directory):
    broken_links = []
    for filepath in Path(directory).rglob('*'):
        if filepath.suffix.lower() in ['.md', '.rst']:
            links = find_links_in_file(filepath)
            for link in links:
                ok, detail = check_link(link)
                if not ok:
                    broken_links.append({
                        'file': str(filepath),
                        'link': link,
                        'error': detail
                    })
    return broken_links

def main():
    parser = argparse.ArgumentParser(description='Validate links in .md and .rst files.')
    parser.add_argument('path', type=str, help='Path to the documentation root')
    args = parser.parse_args()

    print(f"\n🔍 Scanning for broken links in: {args.path}\n")
    results = scan_directory(args.path)

    if not results:
        print("✅ No broken links found!")
    else:
        print("\n❌ Broken Links Found:")
        for result in results:
            print(f"- {result['file']} -> {result['link']} ({result['error']})")

        exit(1)

if __name__ == '__main__':
    main()
