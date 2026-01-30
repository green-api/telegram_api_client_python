import asyncio
from telegram_api_client_python import API

greenAPI = API.GreenAPI(
    "4100000000", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        greenAPI.serviceMethods.checkAccountAsync(79876543210),
        greenAPI.serviceMethods.getContactsAsync(),
        greenAPI.serviceMethods.deleteMessageAsync("79876543210@c.us", "1769676078000", True),
        greenAPI.serviceMethods.deleteMessageAsync("79876543210@c.us", "1769676078000"),
        greenAPI.serviceMethods.editMessageAsync("79876543210@c.us", "1769676078000", "Edited message text")
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

if __name__ == '__main__':
    asyncio.run(main())