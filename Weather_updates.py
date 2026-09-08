"""Observer Pattern: update several displays when the temperature changes."""


class WeatherStation:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_temperature(self, temperature):
        # Notify every observer after the temperature changes.
        for observer in self.observers:
            observer.update(temperature)


class PhoneDisplay:
    def update(self, temperature):
        print(f"Phone display: {temperature} C")


class WindowDisplay:
    def update(self, temperature):
        print(f"Window display: {temperature} C")


station = WeatherStation()
station.add_observer(PhoneDisplay())
station.add_observer(WindowDisplay())

station.set_temperature(30)
