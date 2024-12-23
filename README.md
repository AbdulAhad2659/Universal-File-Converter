
# Universal File Converter and Media Editor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)

## Overview

The Universal File Converter and Media Editor is a powerful and versatile Python application designed to handle a wide range of file conversion and media editing tasks. It provides a user-friendly graphical interface (GUI) built with PyQt, making it easy to convert documents, images, audio, and video files between various formats. Additionally, it offers essential media editing capabilities such as trimming, merging, adding audio/subtitles, and more. The tool also supports integration with Google Drive for seamless cloud-based file management.

## Features

*   **Extensive File Conversion Support:**
    *   **Document Conversion:**
        *   Excel (XLSX) to Word (DOCX)
        *   Word (DOCX) to Excel (XLSX)
        *   PDF to Word (DOCX)
        *   Word (DOCX) to PDF
        *   Excel (XLSX) to PDF
        *   PDF to Excel (XLSX)
        *   Text (TXT) to Word (DOCX)
        *   Word (DOCX) to Text (TXT)
        *   CSV to Excel (XLSX)
        *   Excel (XLSX) to CSV
        *   HTML to PDF
        *   PDF to HTML
        *   Markdown (MD) to PDF
        *   PDF to Markdown (MD)
        *   PowerPoint (PPT) to PDF
        *   PDF to PowerPoint (PPT)
    *   **Image Conversion:**
        *   JPEG to PNG
        *   PNG to JPEG
        *   JPEG to BMP
        *   BMP to PNG
        *   PNG to WebP
        *   WebP to PNG
        *   SVG to PNG
        *   PNG to SVG
        *   PDF to Images (JPEG/PNG per page)
        *   Images to PDF (JPEG/PNG into a single PDF)
    *   **Media Conversion:**
        *   MP4 to MP3
        *   MP3 to WAV
        *   WAV to MP3
        *   MP4 to GIF
        *   GIF to MP4
        *   AVI to MP4
        *   MP4 to AVI
        *   FLAC to MP3
        *   MP3 to FLAC
        *   AAC to MP3
        *   MP3 to AAC
    *   **Miscellaneous Conversion:**
        *   JSON to CSV
        *   CSV to JSON
        *   YAML to JSON
        *   JSON to YAML
        *   XML to JSON
        *   JSON to XML
        *   HTML to Markdown
        *   Markdown to HTML
*   **Media Editing Capabilities:**
    *   **Video Editing:**
        *   Trim Video: Extract specific time intervals.
        *   Remove Sound: Remove audio tracks from video files.
        *   Merge Videos: Combine multiple video clips into one.
        *   Add Audio: Add or replace audio in a video file.
        *   Change Video Resolution: Resize video resolution (e.g., 1080p to 720p).
        *   Add Subtitles: Embed subtitles into video files.
        *   Extract Frames: Extract specific frames or sequences from videos.
    *   **Audio Editing:**
        *   Trim Audio: Extract specific sections from an audio file.
        *   Remove Noise: Reduce or remove background noise.
        *   Change Speed: Increase or decrease playback speed.
        *   Merge Audio Files: Combine multiple audio clips into one.
        *   Extract Audio from Video: Extract audio tracks from video files.
    *   **Image Editing:**
        *   Resize Images: Change image dimensions.
        *   Compress Images: Reduce file size without significant quality loss.
        *   Rotate/Flip Images: Rotate or flip images.
        *   Add Watermarks: Overlay watermarks on images.
        *   Convert to Grayscale: Convert images to black and white.
*   **User-Friendly GUI:**
    *   Intuitive interface built with PyQt.
    *   Drag-and-drop file selection.
    *   Clear conversion and editing options.
    *   Progress bars for monitoring tasks.
    *   Log display for detailed information.
*   **Batch Processing:** Convert or edit multiple files simultaneously.
*   **Google Drive Integration:**
    *   Authenticate with your Google account.
    *   Upload and download files directly from Google Drive.
    *   Process files stored in your Google Drive folders.
*   **Error Handling and Logging:**
    *   Graceful handling of unsupported formats and other potential errors.
    *   Detailed error messages and logging for troubleshooting.

## Requirements

*   **Python:** 3.7 or higher
*   **Libraries:**
    *   `pandas`
    *   `python-docx`
    *   `pdfplumber`
    *   `reportlab`
    *   `Pillow`
    *   `markdown`
    *   `html2text`
    *   `openpyxl`
    *   `moviepy`
    *   `pydub`
    *   `opencv-python`
    *   `ffmpeg-python`
    *   `PyQt5`
    *   `PyYAML`
    *   `beautifulsoup4`
    *   `lxml`
    *   `google-api-python-client`
    *   `google-auth-httplib2`
    *   `google-auth-oauthlib`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/AbdulAhad2659/universal-file-converter.git
    cd universal-file-converter
    ```

2. **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv .venv
    ```

3. **Activate the virtual environment:**

    *   **Windows:**

        ```bash
        .venv\Scripts\activate
        ```

    *   **macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

4. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

## Google Drive Setup

1. **Create a Google Cloud Project:**
    *   Go to the [Google Cloud Console](https://console.cloud.google.com/).
    *   Create a new project or select an existing one.

2. **Enable the Google Drive API:**
    *   In your project, navigate to "APIs & Services" -> "Library."
    *   Search for "Google Drive API" and enable it.

3. **Create Credentials:**
    *   Go to "APIs & Services" -> "Credentials."
    *   Click "Create Credentials" -> "OAuth client ID."
    *   Choose "Desktop app" as the application type.
    *   Give it a name (e.g., "Universal Converter").
    *   Click "Create."

4. **Download `credentials.json`:**
    *   After creating the credentials, you'll see a "Download JSON" button.
    *   Download the `credentials.json` file and place it in the root directory of the project (the `universal-file-converter` folder).

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Using the GUI:**
    *   **Converter Tab:**
        *   Select input files or folders using the "Browse" button or drag and drop.
        *   Choose the output directory.
        *   Select the desired conversion type from the dropdown menu.
        *   Enable "Batch Processing" for multiple files.
        *   Optionally, enable "Use Google Drive" and authenticate.
        *   Click "Convert."
    *   **Media Editor Tab:**
        *   Select input files or folders.
        *   Choose the output directory.
        *   Select the editing type from the dropdown menu.
        *   Adjust editing options as needed.
        *   Click "Edit."

3. **Google Drive Integration:**
    *   In the "Converter" tab, check the "Use Google Drive" box.
    *   Click "Authenticate" to link your Google account.
    *   For input, provide either a file ID or a folder ID from your Google Drive.
    *   For output, provide a folder ID where converted files will be uploaded.

## Troubleshooting

*   **Authentication Errors:** If you encounter issues with Google Drive authentication, delete the `token.json` file and try authenticating again.
*   **Missing Libraries:** If you get an error about a missing library, make sure you have activated your virtual environment and installed all dependencies using `pip install -r requirements.txt`.
*   **Conversion/Editing Errors:** Check the "Log" section in the GUI for detailed error messages. These messages can help you identify the cause of the problem.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your branch to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

*   This project uses many excellent open-source libraries. See the `requirements.txt` file for a full list.
*   Special thanks to the developers of PyQt for creating such a powerful GUI framework.

