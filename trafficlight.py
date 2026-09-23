signal = "green"
match signal:
    case "red":
        print("stop")
    case "yellow":
        print("Get Ready");
    case "green":
        print("Go")
    case _:
        print("Invalid signal")
