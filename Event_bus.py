class EventBus:
    def __init__(self):
        self._listeners = {}


    def register(self, event_type, listener):
        if event_type not in self._listeners:
            self._listeners[event_type] = []

        self._listeners[event_type].append(listener)


    def unregister(self, event_type, listener):
        if event_type in self._listeners:
            if listener in self._listeners[event_type]:
                self._listeners[event_type].remove(listener)
 
    def emit(self, event_type, event):
        for listener in self._listeners.get(event_type,[]):
            listener.on_event(event)


class CoinCollectedEvent:
    def __init__(self, player_id, value):
        self.player_id = player_id
        self.value = value


class ScoreManager:
    def __init__(self):
        self.scores = {}
 
    def on_event(self, event):
        self.scores[event.player_id] = self.scores.get(event.player_id, 0) + event.value
        print(f"Player {event.player_id} score: {self.scores[event.player_id]}")


if __name__ == "__main__":
    bus = EventBus()
    score_mgr = ScoreManager()
    bus.register("coin", score_mgr)

    bus.emit("coin", CoinCollectedEvent(player_id=1, value=10))
    bus.emit("coin", CoinCollectedEvent(player_id=2, value=5))
    bus.emit("coin", CoinCollectedEvent(player_id=1, value=20))