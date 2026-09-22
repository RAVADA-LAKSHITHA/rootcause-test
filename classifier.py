import subprocess
import sys

def run_and_classify(command: list[str]) -> dict:
    """Run a command, capture output, classify the result."""
    result = subprocess.run(command, capture_output=True, text=True)

    exit_code = result.returncode
    stderr = result.stdout + result.stderr  # simulator prints traceback to stderr

    event = {
        "exit_code": exit_code,
        "anomaly": False,
        "type": "healthy",
        "details": None,
    }

    if exit_code == 137:
        event["anomaly"] = True
        event["type"] = "oom"
        event["details"] = "Container killed due to out-of-memory (exit 137)"
    elif exit_code != 0:
        event["anomaly"] = True
        event["type"] = "unhandled_exception"
        event["details"] = stderr.strip().splitlines()[-1] if stderr.strip() else "Unknown error"
    else:
        event["anomaly"] = False
        event["type"] = "healthy"
        event["details"] = "Container ran successfully"

    return event


if __name__ == "__main__":
    event = run_and_classify(["python", "simulator.py"])
    print(event)