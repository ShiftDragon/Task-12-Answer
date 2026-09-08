## How to run

1. You need Python 3.
2. Open a terminal in the `Task_12_Python_Examples` folder.
4. Run these commands, one at a time:

   python Student_results.py

   python Computer_order.py

   python Weather_updates.py


## Expected output

### MVC Architecture

```text
Osama: 85/100 - Pass
Ali: 40/100 - Fail
```

The Controller asks the Model for each result and sends it to the View.

### Builder Pattern

```text
Computer order:
CPU: Intel Core i5
Memory: 16 GB
Storage: 512 GB SSD
```

The Builder adds the CPU, memory and storage step by step, then returns the
finished Computer object.

### Observer Pattern

```text
Phone display: 30 C
Window display: 30 C
```

The WeatherStation sends the new temperature to both registered displays.

## Why these patterns?

- MVC separates data, display and requests.
- Builder creates a complex object in clear steps.
- Observer updates several objects automatically.

