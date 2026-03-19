import os
import time

class DirectoryWatcher:
    def __init__(self, path, interval, callback):
        self.path = path
        self.interval = interval
        self.callback = callback
        self.snapshot = {}

    def watch(self, cycles=None):
        counter = 0
        while True:
            files = os.listdir(self.path)
            for f in files:
                full_path = os.path.join(self.path, f)
                mtime = os.path.getmtime(full_path)
                
                if f not in self.snapshot or self.snapshot[f] != mtime:
                    self.callback(f)
                self.snapshot[f] = mtime
                
            if cycles is not None:
                counter += 1
                if counter >= cycles:
                    break

            time.sleep(self.interval)

def on_change(filename):
    print(f"Changed: {filename}")

if __name__ == "__main__":
    watcher = DirectoryWatcher("my_dir", 1, on_change)
    watcher.watch(cycles=20)