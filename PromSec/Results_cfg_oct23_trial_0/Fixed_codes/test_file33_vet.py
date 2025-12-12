import os
from sydent.sydent import Sydent

test_config = {
    "general": {
        "server_name": "test_server",
        "server_port": 8090
    },
    "database": {
        "name": ":memory:"
    }
}

os.environ["SYDENT_CONFIG"] = "test_config"

sydent = Sydent()