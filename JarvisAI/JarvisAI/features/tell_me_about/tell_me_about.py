import wikipedia


def tell_me(topic):
    try:
        ny = wikipedia.page(topic)
        res = ny.content[:500].encode('utf-8')
        return res
    except Exception as e:
        print(e)
        return False