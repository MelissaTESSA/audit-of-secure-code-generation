import os
import json

def create_service_account(account_name, service_permissions, config_dir):
    account_data = {
        "account_name": account_name,
        "service_permissions": service_permissions
    }
    
    config_file = os.path.join(config_dir, f"{account_name}_config.json")
    
    with open(config_file, "w") as file:
        json.dump(account_data, file)
    
    print(f"Service account {account_name} created with permissions {service_permissions} and configuration stored in {config_file}")

# Example usage
create_service_account("my_service_account", ["read", "write"], "/path/to/config/dir")