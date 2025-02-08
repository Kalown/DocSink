import subprocess
import shutil
import requests
import os
import random
import time
from multiprocessing import Process

def run_command(command):
    """Run a shell command and handle errors."""
    try:
        subprocess.check_call(command, shell=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def is_installed(command):
    """Check if a command is available in the system's PATH."""
    return shutil.which(command) is not None

def install_tools():
    """Install waybackurls and httpx if they are not installed."""
    print("Installing 'waybackurls' and 'httpx'...")

    # Command to install waybackurls
    waybackurls_install = "sudo go install github.com/tomnomnom/waybackurls@latest && sudo cp /root/go/bin/waybackurls /usr/bin"
    run_command(waybackurls_install)

    # Command to install httpx
    httpx_install = "sudo go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest && sudo cp /root/go/bin/httpx /usr/bin"
    run_command(httpx_install)

def create_download_folder():
    """Create the DOC folder if it doesn't exist."""
    if not os.path.exists("DOC"):
        os.makedirs("DOC")

def download_file(url, folder="DOC"):
    """Download the file from the URL and save it to the specified folder."""
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, stream=True)
        
        # Extract the file name from the URL
        file_name = os.path.join(folder, url.split("/")[-1])
        
        # Save the file content to the folder
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_documents_concurrently(urls):
    """Download documents concurrently with a random delay between requests."""
    processes = []
    for url in urls:
        delay = random.randint(2, 4)
        print(f"Waiting for {delay} seconds before downloading {url}...")
        time.sleep(delay)

        # Start a new process for each download
        process = Process(target=download_file, args=(url,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

def run_waybackurls_and_filter(website_url):
    """Run waybackurls and filter URLs ending with specific document types."""
    waybackurls_command = f"waybackurls {website_url} | grep -E '\.(docx|pdf|xls|ppt)$' > urls.txt"
    print("\nRunning waybackurls and filtering document URLs...")
    run_command(waybackurls_command)
    print("Filtered URLs have been saved to 'urls.txt'.")

def run_httpx_and_check(urls_file="urls.txt"):
    """Run httpx to check the URLs from the file."""
    httpx_command = f"httpx -l {urls_file} -sc -o httpx_results.txt"
    print("\nRunning httpx to check the URLs...")
    run_command(httpx_command)
    print("\nThe results of httpx have been saved to 'httpx_results.txt'.")

def download_documents_from_httpx_results(file_path="httpx_results.txt"):
    """Download documents from URLs found in the httpx_results.txt file."""
    # Read the httpx_results.txt file to get all the URLs
    with open(file_path, "r") as f:
        urls_to_download = [line.split()[0] for line in f]

    # Create the DOC folder
    create_download_folder()

    # Download documents concurrently
    print(f"\nDownloading {len(urls_to_download)} documents...")
    download_documents_concurrently(urls_to_download)
    print("\nAll downloads completed.")

def main():
    # Check if waybackurls is installed
    if not is_installed("waybackurls"):
        print("waybackurls is not installed. Installing...")
        install_tools()
    else:
        print("waybackurls is already installed.")

    # Check if httpx is installed
    if not is_installed("httpx"):
        print("httpx is not installed. Installing...")
        install_tools()
    else:
        print("httpx is already installed.")
    
    # Ask for the website URL
    website_url = input("Enter the website URL to check: ")

    # Run waybackurls to extract document URLs
    run_waybackurls_and_filter(website_url)

    # Run httpx to check the URLs
    run_httpx_and_check()

    # Now download documents from the httpx results
    download_documents_from_httpx_results()

if __name__ == "__main__":
    main()
