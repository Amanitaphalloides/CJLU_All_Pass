import time

def print_progress_bar(duration=5):
    print("Starting", end="")
    for i in range(10):
        print(".", end="")
        time.sleep(duration / 10)
    print("Done!")

print_progress_bar()
