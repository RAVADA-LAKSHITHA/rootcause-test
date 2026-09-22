import sys
import random

def simulate_crash():
    scenarios = ["oom", "unhandled_exception", "healthy"]
    choice = random.choice(scenarios)

    if choice == "oom":
        print("Container killed: out of memory", file=sys.stderr)
        sys.exit(137)  # standard OOM exit code
    elif choice == "unhandled_exception":
        raise RuntimeError("Unhandled exception: null pointer at line 42")
    else:
        print("Container ran successfully")
        sys.exit(0)

if __name__ == "__main__":
    simulate_crash()