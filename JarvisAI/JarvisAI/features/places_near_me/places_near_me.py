import webbrowser


def get_places_near_me(inp_command="petrol pump", *args, **kwargs):
    map_base_url = f"https://www.google.com/maps/search/{inp_command}"
    webbrowser.open(map_base_url)

    return "Opening Google Maps"


if __name__ == "__main__":
    print(get_places_near_me("nearest coffee shop"))
