class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key][timestamp] = value
        else:
            self.map[key] = {}
            self.map[key][timestamp] = value


    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            if timestamp in self.map[key]:
                return self.map[key][timestamp]
            while timestamp not in self.map[key] and timestamp > -1:
                timestamp -= 1
            if timestamp == -1:
                return ""
            return self.map[key][timestamp]
        else:
            return ""
        
