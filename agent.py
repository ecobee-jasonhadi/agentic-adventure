if __name__ == "__main__":
    print("Agentic Adventure - Type 'quit' to exit")
    while True:
        try:
            user_input = input("\n> ")
        except (EOFError, KeyboardInterrupt):
            print("\nFarewell, adventurer!")
            break
        if user_input.strip().lower() in ("quit", "exit"):
            print("Farewell, adventurer!")
            break
        if not user_input.strip():
            continue
