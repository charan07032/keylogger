# Keylogger in Python

## Overview

This project is a **Python-based keylogger** that logs keystrokes and sends the logged data via email. It utilizes the `pynput` library for keylogging and includes optional persistence and stealth features.

## Features

- **Keylogging:** Captures all keystrokes, including special keys.
- **Email Reporting:** Sends logged data via email.
- **Persistence Mechanism (Optional):** Adds itself to the system startup.
- **Stealth Mode (Optional):** Runs in the background without a visible window.

## Prerequisites

Ensure you have Python installed on your system. Install the required dependencies using:

```bash
pip install pynput smtplib
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/keylogger-project.git
   cd keylogger-project
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure email settings:**

   - Edit `email_address`, `email_password`, and `target_email` in the script.
   - Enable **Less Secure Apps** in your email provider settings (if required).

## Usage

Run the script using:

```bash
python keylogger.py
```

To run it in the background (on Windows):

```bash
pythonw keylogger.py
```

To stop the script, manually terminate the process or use:

```bash
pkill -f keylogger.py  # Linux/MacOS
```

## Future Improvements

- **Clipboard Monitoring:** Implement clipboard tracking to capture copied text.
- **Screenshot Capture:** Add periodic screenshot functionality for enhanced monitoring.
- **Remote Log Retrieval:** Implement cloud storage integration for retrieving logs remotely.
- **Encrypted Log Files:** Ensure logs are securely stored and encrypted before transmission.
- **GUI Interface:** Develop a simple GUI for enabling/disabling the keylogger easily.
- **Multi-Platform Support:** Improve compatibility across different operating systems.

## Security & Ethical Disclaimer

This project is intended for **educational purposes** and **authorized testing** only. Using a keylogger without explicit permission is **illegal and unethical**. The developer is not responsible for any misuse.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it with proper attribution.

## Contributing

Pull requests and feature enhancements are welcome. Open an issue for bug reports or feature requests.

## Author

- **k sai charan **
- GitHub: charan07032
- Email: ksaicharanreddy07@gmail.com

