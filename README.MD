
│── network_monitor.py            # 🔹 Main script (runs all modules)
│── modules\
│   │── __init__.py               # 🔹 (Empty file to mark as a module)
│   │── network_scan.py           # 🔹 Scans connected devices
│   │── device_block.py           # 🔹 Blocks unknown devices
│   │── http_logger.py            # 🔹 Captures HTTP traffic
│   │── dns_logger.py             # 🔹 Captures DNS traffic
│   │── user_tracker.py           # 🔹 Detects logged-in users
│   │── alert_system.py           # 🔹 Sends email alerts
│   │── database_logger.py        # 🔹 Saves logs to InfluxDB (Optional)
│── logs\
│   │── known_devices.json        # 🔹 Stores detected devices
│   │── website_logs.txt          # 🔹 Logs visited websites
│   │── alerts.log                # 🔹 Stores alerts for review
