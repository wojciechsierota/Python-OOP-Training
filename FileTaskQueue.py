import os

class FileTaskQueue:
    def __init__(self):
        self._tasks = []

    def add_task(self, path, data):
        self._tasks.append((path, data))

    def add_tasks(self, tasks_list):
        for path, data in tasks_list:
            self.add_task(path, data)

    def is_empty(self):
        return len(self._tasks) == 0

    def run_all(self):
        for path, data in self._tasks:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            try:
                with open(path, "w") as f:
                    f.write(data)
                print(f"OK: {path}")
            except IOError:
                print(f"FAILED: {path}")

        self._tasks.clear()

# Quick Test 
if __name__ == "__main__":
    queue = FileTaskQueue()
    queue.add_task("out/test1.txt", "Hello")
    queue.add_tasks([("out/sub/test2.txt", "World"), ("out/test3.txt", "Data")])
    
    queue.run_all()