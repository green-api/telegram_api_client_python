from telegram_api_client_python import API

greenAPI = API.GreenAPI(
    "4100000000", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # DeleteMessage for sender
    response = greenAPI.serviceMethods.deleteMessage("79876543210@c.us", "1769676078000", True)

    # DeleteMessage for all (default)
    response = greenAPI.serviceMethods.deleteMessage("79876543210@c.us", "1769676078000")

    # EditMessage
    response = greenAPI.serviceMethods.editMessage("79876543210@c.us", "1769676078000", "New text")
    print(response.data) # new idMessage

if __name__ == '__main__':
    main()