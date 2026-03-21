
import re
 
class LogParser:
    def __init__(self, pattern, callback):
        self.regex = re.compile(pattern)
        self.callback = callback
 
    def parse_lines(self, lines):
        for line in lines:
            m = self.regex.match(line)
            if m:
                if m.groupdict():
                    data = m.groupdict()
                else:
                    data = m.groups()

                self.callback(data)
    

def on_match(data):
    print("MATCHED:", data)
 
lines = [
    "INFO: System started",
    "DEBUG: Value=42",
    "ERROR: File not found"
]
 
parser = LogParser(r"(?P<level>[A-Z]+): (?P<msg>.+)", on_match)
parser.parse_lines(lines)