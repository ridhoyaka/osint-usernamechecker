import os
import time
import sys
import requests
import pyfiglet

def clear_screen():
    os.system('clear') 

def loading_bar(duration=3, length=20):
    print("Please wait (Loading for tools):")
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = "#" * i + "-" * (length - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / length)
    print()

if __name__ == "__main__":
    loading_bar()
    clear_screen()
    
    white = "\033[97m"
    reset = "\033[0m"
    ascii_art = pyfiglet.figlet_format("Username Checker", font="small")
    print(f"{white}{ascii_art}{reset}")
    print("                                                    v1.0 coded by Akay")
    print(" ")

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def load_platforms(username):
    return {
        "GitHub": f"https://github.com/{username}",
        "X": f"https://x.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Tumblr": f"https://{username}.tumblr.com",
        "Medium": f"https://medium.com/@{username}",
        "Flickr": f"https://www.flickr.com/people/{username}/",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "About.me": f"https://about.me/{username}"
    }


def check_username(username):
    platforms = load_platforms(username)
    session = requests.Session()

    print(f"\n[+] Checking for username: {username}\n")
    for platform, url in platforms.items():
        try:
            response = session.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{GREEN}[FOUND]{RESET} {username} exists on {platform}: {url}")
            elif response.status_code == 404:
                print(f"{YELLOW}[NOT FOUND]{RESET} {username} not found on {platform}")
            else:
                print(f"{RED}[UNKNOWN]{RESET} {platform} returned status code {response.status_code}")
        except requests.RequestException as e:
            print(f"{RED}[ERROR]{RESET} Could not check {platform}: {e}")


if __name__ == "__main__":
    user_input = input("Enter a username to check: ").strip()
    if user_input:
        check_username(user_input)
    else:
        print("[!] Username cannot be empty.")


