# Dice Roller Function
```python
def roll_dice(num_dice: str, num_faces: str) -> str:
    """
    Rolls a specified number of dice with a specified number of faces.

    Args:
        num_dice: The number of dice to roll as a string.
        num_faces: The number of faces per die as a string.

    Returns:
        A string describing the results of the rolls or an error message.
    """
    try:
        n = int(num_dice)
        f = int(num_faces)

        if n <= 0 or f <= 0:
            return "Error: Number of dice and faces must be positive integers."

        rolls = [random.randint(1, f) for _ in range(n)]
        print(
            f"Rolled {n} dice with {f} faces: {', '.join(map(str, rolls))} (Total: {sum(rolls)})"
        )
        return f"Rolled {n} dice with {f} faces: {', '.join(map(str, rolls))} (Total: {sum(rolls)})"
    except ValueError:
        return "Error: Invalid input. Both number of dice and faces must be integers."
```