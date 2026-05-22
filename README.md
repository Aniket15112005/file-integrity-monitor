File Integrity Monitoring System (FIM)

A real-time cybersecurity monitoring system built using Python that detects unauthorized file changes, generates alerts, logs security events, and automatically recovers deleted files.


Features

### Core Features

- Real-time file monitoring
- SHA-256 file hashing
- File modification detection
- File deletion detection
- New file creation detection
- Security logging
- Ignore rules support
- Error handling

### Advanced Security Features

- Email alert notifications
- Automatic file backup system
- Automatic file recovery
- Multi-folder monitoring
- Threat severity classification
- SQLite database logging
- Colorized terminal alerts

## Technologies Used

- Python
- watchdog
- hashlib
- SQLite
- logging
- colorama

## Project Structure


file-integrity-monitor/
│
├── app.py
├── monitor.py
├── scanner.py
├── alerts.py
├── recovery.py
├── email_alert.py
├── threat_levels.py
├── db_logger.py
├── database.py
├── requirements.txt
├── ignore_rules.txt
│
├── backups/
├── configs/
├── critical-data/
├── data/
├── logs/
├── reports/
├── screenshots/
└── watched-files/


## Installation

### Clone Repository

bash:
git clone https://github.com/Aniket15112005/file-integrity-monitor.git


### Install Dependencies

bash
pip install -r requirements.txt


## Run the Application

bash
python app.py


## How the System Works

1. The application scans monitored folders and generates SHA-256 hashes for all files.
2. Baseline hashes are stored locally.
3. The watchdog library continuously monitors folders in real time.
4. If any file is modified, deleted, or newly created, the system generates an alert.
5. Security events are logged into both a log file and SQLite database.
6. Email alerts are sent for suspicious activity.
7. Backup copies are created automatically for recovery purposes.
8. Deleted files can be restored from backups.

## Security Features Demonstrated

- File Integrity Monitoring (FIM)
- Threat Detection
- Real-Time Monitoring
- Incident Logging
- Security Alerting
- File Recovery
- Database Event Logging
- Threat Severity Analysis

## Example Alerts


[MEDIUM] File modified: watched-files/config.txt

[CRITICAL] File deleted: configs/settings.conf

[RECOVERY] File restored: configs/settings.conf


## Testing Performed

The following tests were successfully completed:

- File modification testing
- File deletion testing
- File creation testing
- Email alert testing
- File recovery testing
- Multi-folder monitoring testing
- Database logging testing
- Threat severity testing

## Screenshots

Screenshots and logs are available in the `screenshots/` folder.

## Future Improvements

Possible future upgrades include:

- Web dashboard using Flask
- Telegram or Discord alerts
- Dark mode UI
- Cloud log storage
- User authentication
- Advanced malware detection



Aniket

Cybersecurity and Python-based File Integrity Monitoring project created for learning and practical security monitoring demonstration.