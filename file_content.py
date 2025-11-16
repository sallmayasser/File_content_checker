import pandas as pd
import yaml
import os


def load_config():
    # Get directory of the Python script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.yaml")

    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def count_rows(file_path):
    if not os.path.exists(file_path):
        return None, "not_found"

    try:
        df = pd.read_csv(file_path)
        return len(df), "ok"
    except Exception:
        return None, "error"


def main():
    config = load_config()
    files = config["files"]

    for file_path in files:
        rows, status = count_rows(file_path)
        file_name = os.path.basename(file_path)

        if status == "not_found":
            # Use rows = -1 as signal for Grafana alerting
            print(
                f'file_content_check,file_name={file_name} rows=-1,status="not_found"')
            continue

        if status == "error":
            print(f'file_content_check,file_name={file_name} rows=-1,status="error"')
            continue

        # Normal case
        print(f'file_content_check,file_name={file_name} rows={rows},status="ok"')


if __name__ == "__main__":
    main()
