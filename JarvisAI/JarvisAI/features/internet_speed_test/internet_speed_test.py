import speedtest  # pip install speedtest-cli

st = speedtest.Speedtest()


def download_speed():
    down = round(st.download() / 10 ** 6, 2)
    return down


def upload_speed():
    up = round(st.upload() / 10 ** 6, 2)
    return up


def ping():
    servernames = []
    st.get_servers(servernames)
    results = st.results.ping
    return results


def speed_test(inp_command):
    try:
        print("Checking internet speed. Please wait...")
        # print('Download Speed: ' + str(download_speed()) + 'MB/s')
        # print('Upload Speed: ' + str(upload_speed()) + ' MB/s')
        # print('Ping: ' + str(ping()) + ' ms')
        return "Download Speed: " + str(download_speed()) + "MB/s" + "\n Upload Speed: " + str(
            upload_speed()) + " MB/s" + "\n Ping: " + str(ping()) + " ms"
    except Exception as e:
        print(e)
        return "Error in internet speed test"


if __name__ == '__main__':
    speed_test()
