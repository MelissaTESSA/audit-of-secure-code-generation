import os
from sydent.sydent import Sydent

config = {
    "general": {
        "server_name": "test_server",
        "server_port": 8090,
        "request_timeout": 10,
        "pid_file": "/var/run/sydent.pid",
        "log_config": "/path/to/log_config.yaml",
        "terms_path": "/path/to/terms.html",
        "enable_metrics": False
    },
    "database": {
        "name": "sqlite3",
        "args": {
            "dbfile": ":memory:"
        }
    },
    "email": {
        "smtp_host": "localhost",
        "smtp_port": 25,
        "account_validity_duration": 86400,
        "address": "noreply@example.com",
        "password": os.getenv("EMAIL_PASSWORD")
    },
    "account": {
        "mau_limits": {
            "monthly_active_user_rate": 0.1,
            "max_mau_value": 1000
        }
    }
}

sydent = Sydent(config)
sydent.run()