from telegram_api_client_python import API

greenAPI = API.GreenAPI(
    "4100000000", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # If no argument, the messages for 24 hours are returned.

    print("Incoming messages in the last 72 hours:")
    response = greenAPI.journals.lastIncomingMessages()
    print(response.data)

    print("Outgoing messages in the last 72 hours:")
    response = greenAPI.journals.lastOutgoingMessages()
    print(response.data)


if __name__ == '__main__':
    main()