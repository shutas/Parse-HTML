"""Demo for Maintaining Order of PDF Documents in HTML."""

import config
from bs4 import BeautifulSoup


def load_content(filepath):
    """Read content from file and return content as string."""
    try:
        file_obj = open(filepath, "r")
        return file_obj.read()
    except Exception:
        raise Exception("Can't open the file. Check the path.")


def process_content(content):
    """Parse HTML and create the ordered list of PDF filenames."""
    soup = BeautifulSoup(content, "html.parser")

    # Get all <a> tags
    for link in soup.find_all("a"):

        # Sanitize filename by removing directory names
        href_value = link.get("href").split("/")[-1]

        # If PDF file found, add it to order list
        if ".pdf" in href_value:
            config.ORDER_LIST.append(href_value)
            config.COUNTER += 1


def print_order_list():
    """Print items in list in order."""
    print "=== HTML Document Starts Here ==="

    for item in config.ORDER_LIST:
        print item

    print "=== HTML Document Ends Here ==="


def main():
    """Driver for Demo."""
    # Load content of specified HTML file
    html_content = load_content(config.TARGET_FILE_PATH)

    # Parse HTML and create list of PDF filenames in order of appearance
    process_content(html_content)

    # Print PDF filenames in the ordered list
    print_order_list()


if __name__ == "__main__":
    main()