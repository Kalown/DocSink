# DocSink

**DocSink** is a powerful and efficient tool designed for crawling websites, extracting document links (PDF, DOCX, PPT, XLS, etc.), checking if the links are live, and downloading the documents concurrently. Built using a combination of `waybackurls` and `httpx`, **docSink** helps you quickly gather and store documents from a given website with ease.

## Features

- **Crawl websites** for document links: PDF, DOCX, PPT, XLS, etc.
- **Check link status**: Using `httpx` to verify if URLs are alive and reachable.
- **Download documents concurrently**: Using multiprocessing for fast, parallel downloads.
- **Randomized delay**: Introduces a random delay of 2-4 seconds between each download to avoid overwhelming the server.
- **Automatic tool installation**: Installs the necessary tools (`waybackurls` and `httpx`) if they are not present on the system.

## Prerequisites

Before running **docSink**, you need to have the following installed:

- Python 3.x
- `go` (for installing `waybackurls` and `httpx` tools)

You can check if Python is installed by running:

```bash
python3 --version
```

To check if `go` is installed, run:

```bash
go version
```

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Kalown/DocSink.git
cd DocSink
```

2. **Install required tools:**

If the required tools (`waybackurls` and `httpx`) are not installed, the script will automatically install them for you. However, if you'd like to install them manually, you can use:

```bash
sudo go install github.com/tomnomnom/waybackurls@latest
sudo go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

## Usage

1. **Run the script:**

Once everything is set up, run the script to start crawling and downloading documents:

```bash
python3 docSink.py
```

2. **Provide the website URL:**

The script will prompt you to enter the website URL you want to crawl for document links. For example:

```
Enter the website URL to check: https://example.com
```

3. **Documents Downloaded:**

The script will find all document links on the website, check their status using `httpx`, and download any valid documents (with a `200 OK` status code) into the `DOC` folder. All downloaded files will be saved in the `DOC/` directory.

## How It Works

1. **Waybackurls Crawl**:  
   The tool first uses `waybackurls` to extract historical URLs of documents from a given website.

2. **Filtering Documents**:  
   The script filters URLs to include only specific document types, such as `.pdf`, `.docx`, `.ppt`, `.xls`.

3. **Checking URLs**:  
   It then uses `httpx` to check the status of the filtered URLs and writes the results to `httpx_results.txt`.

4. **Downloading Documents**:  
   Finally, the script downloads the documents concurrently, introducing a random delay between each download to avoid overwhelming the server.

## Example

Here’s a simple example of how **docSink** works:

1. **User Input:**
   ```
   Enter the website URL to check: https://example.com
   ```

2. **Waybackurls Crawl:**
   The tool finds document URLs from `https://example.com`:
   ```
   http://example.com/file1.pdf
   http://example.com/file2.docx
   ```

3. **httpx Check:**
   The script checks the status of these URLs and confirms that the documents are live.

4. **Downloading Files:**
   The files are downloaded concurrently and saved in the `DOC` folder:
   ```
   DOC/
   ├── file1.pdf
   └── file2.docx
   ```

## Contributing

Contributions are welcome! If you want to improve or add features to **docSink**, feel free to:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Waybackurls**: A tool for discovering URLs archived in the Wayback Machine by [@tomnomnom](https://github.com/tomnomnom).
- **httpx**: A fast and flexible tool for testing HTTP endpoints and many more by [@projectdiscovery](https://github.com/projectdiscovery).
