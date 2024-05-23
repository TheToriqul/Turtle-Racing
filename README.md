# Turtle Racing Game

This repository contains a simple turtle racing game implemented in Python using the `turtle` module. Players can choose the number of turtles to race, and the turtles will move forward a random distance until one of them crosses the finish line. The winner is announced at the end of the race.

## Features

- User input to select the number of racers (2 to 10).
- Randomly moving turtles using the `turtle` and `random` modules.
- Dynamic creation and positioning of turtles.
- Display of the winner at the end of the race.

## Requirements

- Python 3.x
- `turtle` module (usually included with Python standard library)

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/TheToriqul/Turtle-Racing.git
    cd Turtle-Racing
    ```

2. Run the Python script:
    ```bash
    python app.py
    ```

3. Follow the on-screen instructions to enter the number of players (between 2 and 10).

4. Watch the turtles race and see which one wins!

## Code Explanation

### Constants

```python
WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
```
- `WIDTH` and `HEIGHT` define the dimensions of the turtle racing window.
- `COLORS` is a list of colors that the turtles can have.

### Function Definitions

#### `get_number_of_racers()`

```python
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of players (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a numeric number between 2 and 10. Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter a numeric number between 2 and 10. Try again!")
            continue
```
- Prompts the user to enter the number of racers.
- Ensures the input is a numeric value between 2 and 10.

#### `race(colors)`

```python
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
```
- Starts the race and moves each turtle forward by a random distance.
- Checks if any turtle has crossed the finish line and returns the color of the winning turtle.

#### `create_turtles(colors)`

```python
def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles
```
- Creates and positions the turtles at the start line based on the number of racers.

#### `init_turtle()`

```python
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')
```
- Initializes the turtle screen with the specified width and height.
- Sets the title of the window to "Turtle Racing!"

### Main Execution

```python
racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
```
- Gets the number of racers from the user.
- Initializes the turtle screen.
- Shuffles the list of colors and selects a subset based on the number of racers.
- Starts the race and prints the color of the winning turtle.
- Pauses for 5 seconds before closing the window.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

- The `turtle` module documentation: https://docs.python.org/3/library/turtle.html
- Python's `random` module documentation: https://docs.python.org/3/library/random.html

Enjoy racing your turtles! 🐢🚀