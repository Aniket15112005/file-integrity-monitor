import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from scanner import generate_hash
from database import load_baseline, save_baseline
from alerts import alert


class FileMonitorHandler(FileSystemEventHandler):

    def __init__(self):

        self.baseline = load_baseline()

    def on_modified(self, event):

        try:

            if event.is_directory:
                return

            file_path = event.src_path

            current_hash = generate_hash(file_path)

            old_hash = self.baseline.get(file_path)

            if current_hash and old_hash:

                if current_hash != old_hash:

                    alert(
                        f"File modified: {file_path}",
                        "MEDIUM"
                    )

                    self.baseline[file_path] = current_hash

                    save_baseline(self.baseline)

        except Exception as e:

            print(f"[ERROR] {e}")

    def on_created(self, event):

        try:

            if event.is_directory:
                return

            file_path = event.src_path

            current_hash = generate_hash(file_path)

            self.baseline[file_path] = current_hash

            save_baseline(self.baseline)

            alert(
                f"New file created: {file_path}",
                "LOW"
            )

        except Exception as e:

            print(f"[ERROR] {e}")

    def on_deleted(self, event):

        try:

            if event.is_directory:
                return

            file_path = event.src_path

            if file_path in self.baseline:

                del self.baseline[file_path]

                save_baseline(self.baseline)

            alert(
                f"File deleted: {file_path}",
                "CRITICAL"
            )

        except Exception as e:

            print(f"[ERROR] {e}")


def start_monitoring(path):

    event_handler = FileMonitorHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        path,
        recursive=True
    )

    observer.start()

    print(f"[INFO] Monitoring started on: {path}")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print("\n[INFO] Monitoring stopped.")

        observer.stop()

    observer.join()