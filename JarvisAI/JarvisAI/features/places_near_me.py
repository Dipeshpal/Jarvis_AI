import webbrowser


def get_places_near_me(*args, **kwargs):
    inp_command = kwargs.get("query")
    map_base_url = f"https://www.google.com/maps/search/{inp_command}"
    webbrowser.open(map_base_url)

    return "Opening Google Maps"


if __name__ == "__main__":
    print(get_places_near_me("nearest coffee shop"))
