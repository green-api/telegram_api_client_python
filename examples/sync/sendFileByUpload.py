from telegram_api_client_python import API

greenAPI = API.GreenAPI(
    "4100000000", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

def main():
    response = greenAPI.sending.sendFileByUpload(
        "79876543210@c.us",
        "data/logo.jpg",
        "logo.jpg",
        "Available rates"
    )

    print(response.data)

if __name__ == '__main__':
    main()