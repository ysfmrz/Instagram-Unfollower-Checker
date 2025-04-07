import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Set

# Constants
PROFILE_PATH_FILE = 'path.txt'
INSTAGRAM_URL = 'https://www.instagram.com/prettyland.onlineshop/'
FOLLOWERS_FILE = 'followers.txt'
ELEMENT_CLASS_NAME = '_a6hd'
DEFAULT_TIMEOUT = 160  # Default timeout in seconds for WebDriverWait

def read_profile_path(file_path: str) -> str:
    """Read the Firefox profile path from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise Exception(f"Profile path file '{file_path}' not found.")
    except Exception as e:
        raise Exception(f"Error reading profile path: {e}")

def initialize_driver(profile_path: str) -> webdriver.Firefox:
    """Initialize the Firefox WebDriver with the specified profile."""
    options = Options()
    options.add_argument("-profile")
    options.add_argument(profile_path)
    options.page_load_strategy = 'none'
    return webdriver.Firefox(options=options)

def extract_usernames(driver: webdriver.Firefox, timeout: int = DEFAULT_TIMEOUT) -> Set[str]:
    """Extract unique usernames from Instagram profile links."""
    text_set = set()
    try:
        # Wait for elements to load and extract them
        elements = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, ELEMENT_CLASS_NAME))
        )
        time.sleep(5)  # Brief pause to ensure stability
        for element in elements:
            href = element.get_attribute('href')
            username = href.split('/')[-2] if href and '/' in href else href
            print(username)
            text_set.add(username)
        return text_set
    except Exception as e:
        raise Exception(f"Error extracting usernames: {e}")

def write_to_file(file_path: str, data: Set[str]) -> None:
    """Write a set of data to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in sorted(data):  # Sorting for consistency
            file.write(f"{item}\n")

def compare_file_with_set(file_path: str, current_set: Set[str]) -> None:
    """Compare file contents with a set and print differences."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = set(file.read().splitlines())
        unfollowed = file_contents - current_set
        if unfollowed:
            print("\nYou were unfollowed by:")
            for item in sorted(unfollowed):
                print(item)
        else:
            print("\nNo changes detected in followers.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found for comparison.")
    except Exception as e:
        print(f"Error during comparison: {e}")

def main():
    """Main execution logic for the Instagram follower script."""
    # Initialize WebDriver
    firefox_profile_path = read_profile_path(PROFILE_PATH_FILE)
    driver = initialize_driver(firefox_profile_path)

    try:
        vz = input("Enter 'F' to create a follower file, 'C' to check changes: ").strip().upper()

        # Open Instagram page
        driver.get(INSTAGRAM_URL)
        time.sleep(10)  # Wait for initial page load

        # Wait for the first element to confirm page load
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, ELEMENT_CLASS_NAME))
        )
        print("Element found!\n")
        input("Press Enter to continue...")

        if vz == 'F':
            # Create a new follower file
            usernames = extract_usernames(driver)
            write_to_file(FOLLOWERS_FILE, usernames)
            print(f"Follower list saved to '{FOLLOWERS_FILE}'")

        elif vz == 'C':
            # Check for changes in followers
            usernames = extract_usernames(driver)
            compare_file_with_set(FOLLOWERS_FILE, usernames)
            
            rwt = input("Write updated list to file? (y/n): ").strip().lower()
            if rwt == 'y':
                write_to_file(FOLLOWERS_FILE, usernames)
                print(f"Updated follower list saved to '{FOLLOWERS_FILE}'")

        else:
            print("Invalid input. Please use 'F' or 'C'.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Closing driver...")
        driver.quit()

if __name__ == "__main__":
    main()
