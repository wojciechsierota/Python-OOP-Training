import datetime

class TaskScheduler:
    def __init__(self):
        self._tasks = []

    def add(self, run_time, callback):
        self._tasks.append((run_time, callback))

    def run_pending(self):
        now = datetime.datetime.now()

        for run_time, callback in self._tasks:
            if run_time <= now:
                try:
                    callback()
                except Exception as e:
                    print(f"Error executing task: {e}")

        self._tasks = [task for task in self._tasks if task[0] > now]

    def clear(self):
        self._tasks.clear()

    def get_task_count(self):
        return len(self._tasks)
    

# Demonstration and Testing
if __name__ == "__main__":
    s = TaskScheduler()
    now = datetime.datetime.now()
    s.add(now, lambda: print("Executing task 1 ...."))
    s.add(now, lambda: 1/0) 
    s.add(now + datetime.timedelta(minutes=30), lambda: print("Should not run now"))

    print(f"Tasks before: {s.get_task_count()}")
    s.run_pending()
    print(f"Tasks left: {s.get_task_count()}")

    