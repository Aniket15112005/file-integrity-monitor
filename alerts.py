import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def alert(message, severity="MEDIUM"):

    final_message = f"[{severity}] {message}"

    print(final_message)

    logging.warning(final_message)