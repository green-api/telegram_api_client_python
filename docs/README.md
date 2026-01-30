# telegram-api-client-python

![](https://img.shields.io/badge/license-CC%20BY--ND%204.0-green)
![](https://img.shields.io/pypi/status/telegram-api-client-python)
![](https://img.shields.io/pypi/pyversions/telegram-api-client-python)
![](https://img.shields.io/github/actions/workflow/status/green-api/telegram-api-client-python/python-package.yml)
![](https://img.shields.io/pypi/dm/telegram-api-client-python)

## Поддержка

[![Support](https://img.shields.io/badge/support@green--api.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@green-api.com)
[![Support](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/greenapi_support_ru_bot)
[![Support](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/79993331223)

## Руководства и новости

[![Guides](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@green-api)
[![News](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/green_api)
[![News](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaHUM5TBA1f7cG29nO1C)

telegram-api-client-python - библиотека для интеграции с мессенджером Telegram через API
сервиса [green-api.com](https://green-api.com/). Чтобы воспользоваться библиотекой, нужно получить регистрационный токен
и ID аккаунта в [личном кабинете](https://console.green-api.com/). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/docs/api/). Библиотека является обёрткой к REST API,
поэтому документация по ссылке выше применима и к самой библиотеке.

## Авторизация

Чтобы отправить сообщение или выполнить другие методы GREEN API, аккаунт Telegram в приложении телефона должен быть в
авторизованном состоянии. Для авторизации аккаунта перейдите в [личный кабинет](https://console.green-api.com/) и
сканируйте QR-код с использованием приложения Telegram.

## Установка

```shell
python -m pip install telegram-api-client-python
```

## Импорт

```
from telegram_api_client_python import API
```

## Примеры

### Как инициализировать объект

```
greenAPI = API.GreenAPI(
    "4100000000", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)
```

### Отправка текстового сообщения на номер Telegram

Ссылка на пример: [sendTextMessage.py](../examples/sync/sending/sendTextMessage.py).

```
response = greenAPI.sending.sendMessage("79876543210@c.us", "Message text")

print(response.data)
```


### Отправка текстового сообщения асинхронно

Ссылка на пример: [sendMessageAsync.py](../examples/async/sending/sendMessageAsync.py).

```
import asyncio

async def main():
    response = await greenAPI.sending.sendMessageAsync("79876543210@c.us", "Message text")
    print(response.data)

asyncio.run(main())
```

### Отправка картинки по URL

Ссылка на пример: [sendFileByUrl.py](../examples/sync/sending/sendFileByUrl.py).

```
response = greenAPI.sending.sendFileByUrl(
    "79876543210@c.us",
    "https://download.samplelib.com/png/sample-clouds2-400x300.png",
    "sample-clouds2-400x300.png",
    "Sample PNG"
)

print(response.data)
```

### Отправка картинки загрузкой с диска

Ссылка на пример: [sendFileByUpload.py](../examples/sync/sending/sendFileByUpload.py).

```
response = greenAPI.sending.sendFileByUpload(
    "79876543210@c.us",
    "data/logo.jpg",
    "logo.jpg",
    "Available rates"
)

print(response.data)
```


### Отправка картинки асинхронно загрузкой с диска

Ссылка на пример: [sendFileByUploadAsync.py](../examples/async/sending/sendFileByUploadAsync.py).

```
import asyncio

async def main():
    response = await greenAPI.sending.sendFileByUploadAsync(
        "79876543210@c.us",
        "data/logo.jpg",
        "logo.jpg",
        "Available rates"
    )
    print(response.data)

asyncio.run(main())
```

### Создание группы и отправка сообщения в эту группу

**Важно**. Если попытаться создать группу с несуществующим номером Telegram, то может заблокировать номер отправителя.
Номер в примере не существует.

Ссылка на пример: [createGroupAndSendMessage.py](../examples/sync/createGroupAndSendMessage.py).

```
create_group_response = greenAPI.groups.createGroup(
    "Group Name", ["79876543210@c.us"]
)
if create_group_response.code == 200:
    send_message_response = greenAPI.sending.sendMessage(
        create_group_response.data["chatId"], "Message text"
    )
```

### Получение входящих уведомлений через HTTP API

Ссылка на пример: [receiveNotification.py](../examples/sync/receiveNotification.py).

Общая концепция получения данных в GREEN API описана [здесь](https://green-api.com/docs/api/receiving/). Для старта
получения уведомлений через HTTP API требуется выполнить метод библиотеки:

```
greenAPI.webhooks.startReceivingNotifications(onEvent)
```

onEvent - ваша функция, которая должен содержать параметры:

| Параметр    | Описание                          |
|-------------|-----------------------------------|
| typeWebhook | тип полученного уведомления (str) |
| body        | тело уведомления (dict)           |

Типы и форматы тел уведомлений находятся [здесь](https://green-api.com/docs/api/receiving/notifications-format/).

Эта функция будет вызываться при получении входящего уведомления. Далее обрабатываете уведомления согласно бизнес-логике
вашей системы.


### Асинхронное получение входящих уведомлений через HTTP API

Ссылка на пример: [receiveNotificationAsync.py](../examples/async/receiveNotificationAsync.py).

```
import asyncio

async def main():
    await greenAPI.webhooks.startReceivingNotificationsAsync(onEvent)

asyncio.run(main())
```

## Список примеров

| Описание                                               | Модуль                                                                            |
|--------------------------------------------------------|-----------------------------------------------------------------------------------|
| Пример отправки текста                                 | [sendTextMessage.py](../examples/sync/sending/sendTextMessage.py)                 |
| Пример асинхронной отправки текста                     | [sendTextMessageAsync.py](../examples/async/sending/sendMessageAsync.py)          |
| Пример отправки картинки по URL                        | [sendFileByUrl.py](../examples/sync/sending/sendFileByUrl.py)             |
| Пример асинхронной отправки файла по URL               | [sendFileByUrlAsync.py](../examples/async/sending/sendFileByUrlAsync.py)          |
| Пример отправки картинки загрузкой с диска             | [sendFileByUpload.py](../examples/sync/sending/sendFileByUpload.py)         |
| Пример асинхронной отправки картинки загрузкой с диска | [sendFileByUploadAsync.py](../examples/async/sending/sendFileByUploadAsync.py)    |
| Пример создания группы и отправки сообщения в группу   | [createGroupAndSendMessage.py](../examples/sync/createGroupAndSendMessage.py)     |
| Пример асинхронных создания группы и отправки сообщения в группу | [createGroupAndSendMessageAsync.py](../examples/async/createGroupAndSendMessageAsync.py)  |
| Пример получения входящих уведомлений                  | [receiveNotification.py](../examples/sync/receiveNotification.py)                 |
| Пример асинхронного получения входящих уведомлений     | [receiveNotificationФынтс.py](../examples/async/receiveNotificationAsync.py)      |
| Пример создания инстанса                               | [CreateInstance.py](../examples/sync/partherMethods/CreateInstance.py)            |
| Пример асинхронного создания инстанса                  | [CreateInstanceAsync.py](../examples/async/partnerMethods/CreateInstanceAsync.py) |
| Пример отправки уведомления о наборе текста или записи аудио | [SendTyping.py](../examples/sync/sendTyping.py)                             |
| Пример асинхронной отправки уведомления о наборе текста или записи аудио | [SendTypingAsync.py](../examples/async/sendTypingAsync.py)      |

## Полный список методов библиотеки

| Метод API                              | Описание                                                                                                                  | Ссылка на документацию                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `account.getSettings`                  | Метод предназначен для получения текущих настроек аккаунта                                                                | [GetSettings](https://green-api.com/docs/api/account/GetSettings/)                                       |
| `account.getAccountSettings`                | Метод предназначен для получения информации о аккаунте Telegram                                                           | [getAccountSettings](https://green-api.com/docs/api/account/getAccountSettings/)                                   |
| `account.setSettings`                  | Метод предназначен для установки настроек аккаунта                                                                        | [SetSettings](https://green-api.com/docs/api/account/SetSettings/)                                       |
| `account.getStateInstance`             | Метод предназначен для получения состояния аккаунта                                                                       | [GetStateInstance](https://green-api.com/docs/api/account/GetStateInstance/)                             |
| `account.reboot`                       | Метод предназначен для перезапуска аккаунта                                                                               | [Reboot](https://green-api.com/docs/api/account/Reboot/)                                                 |
| `account.logout`                       | Метод предназначен для разлогинивания аккаунта                                                                            | [Logout](https://green-api.com/docs/api/account/Logout/)                                                 |
| `account.qr`                           | Метод предназначен для получения QR-кода                                                                                  | [QR](https://green-api.com/docs/api/account/QR/)                                                         |
| `account.setProfilePicture`            | Метод предназначен для установки аватара аккаунта                                                                         | [SetProfilePicture](https://green-api.com/docs/api/account/SetProfilePicture/)                           |
| `account.startAuthorization`           | Метод предназначен для авторизации инстанса по номеру телефона                                                            | [startAuthorization](https://green-api.com/docs/api/account/startAuthorization/)                     |
| `account.sendAuthorizationCode`        | Метод предназначен для отправки кода авторизации                                                                 | [sendAuthorizationCode](https://green-api.com/docs/api/account/sendAuthorizationCode/)                   |
| `account.sendAuthorizationPassword}`   | Метод предназначен для отправки пароля авторизации                                                                 | [sendAuthorizationPassword](https://green-api.com/docs/api/account/sendAuthorizationPassword/)                   |
| `groups.createGroup`                   | Метод предназначен для создания группового чата                                                                           | [CreateGroup](https://green-api.com/docs/api/groups/CreateGroup/)                                        |
| `groups.updateGroupName`               | Метод изменяет наименование группового чата                                                                               | [UpdateGroupName](https://green-api.com/docs/api/groups/UpdateGroupName/)                                |
| `groups.getGroupData`                  | Метод получает данные группового чата                                                                                     | [GetGroupData](https://green-api.com/docs/api/groups/GetGroupData/)                                      |
| `groups.addGroupParticipant`           | Метод добавляет участника в групповой чат                                                                                 | [AddGroupParticipant](https://green-api.com/docs/api/groups/AddGroupParticipant/)                        |
| `groups.removeGroupParticipant`        | Метод удаляет участника из группового чата                                                                                | [RemoveGroupParticipant](https://green-api.com/docs/api/groups/RemoveGroupParticipant/)                  |
| `groups.setGroupAdmin`                 | Метод назначает участника группового чата администратором                                                                 | [SetGroupAdmin](https://green-api.com/docs/api/groups/SetGroupAdmin/)                                    |
| `groups.removeAdmin`                   | Метод лишает участника прав администрирования группового чата                                                             | [RemoveAdmin](https://green-api.com/docs/api/groups/RemoveAdmin/)                                        |
| `groups.setGroupPicture`               | Метод устанавливает аватар группы                                                                                         | [SetGroupPicture](https://green-api.com/docs/api/groups/SetGroupPicture/)                                |
| `groups.leaveGroup`                    | Метод производит выход пользователя текущего аккаунта из группового чата                                                  | [LeaveGroup](https://green-api.com/docs/api/groups/LeaveGroup/)                                          |
| `journals.getChatHistory`              | Метод возвращает историю сообщений чата                                                                                   | [GetChatHistory](https://green-api.com/docs/api/journals/GetChatHistory/)                                |
| `journals.getMessage`                  | Метод возвращает сообщение чата                                                                                           | [GetMessage](https://green-api.com/docs/api/journals/GetMessage/)                                        |       
| `journals.lastIncomingMessages`        | Метод возвращает крайние входящие сообщения аккаунта                                                                      | [LastIncomingMessages](https://green-api.com/docs/api/journals/LastIncomingMessages/)                    |
| `journals.lastOutgoingMessages`        | Метод возвращает крайние отправленные сообщения аккаунта                                                                  | [LastOutgoingMessages](https://green-api.com/docs/api/journals/LastOutgoingMessages/)                    |
| `queues.showMessagesQueue`             | Метод предназначен для получения списка сообщений, находящихся в очереди на отправку                                      | [ShowMessagesQueue](https://green-api.com/docs/api/queues/ShowMessagesQueue/)                            |
| `queues.clearMessagesQueue`            | Метод предназначен для очистки очереди сообщений на отправку                                                              | [ClearMessagesQueue](https://green-api.com/docs/api/queues/ClearMessagesQueue/)                          |
| `marking.readChat`                     | Метод предназначен для отметки сообщений в чате прочитанными                                                              | [ReadChat](https://green-api.com/docs/api/marks/ReadChat/)                                               |
| `receiving.receiveNotification`        | Метод предназначен для получения одного входящего уведомления из очереди уведомлений                                      | [ReceiveNotification](https://green-api.com/docs/api/receiving/technology-http-api/ReceiveNotification/) |
| `receiving.deleteNotification`         | Метод предназначен для удаления входящего уведомления из очереди уведомлений                                              | [DeleteNotification](https://green-api.com/docs/api/receiving/technology-http-api/DeleteNotification/)   |
| `receiving.downloadFile`               | Метод предназначен для скачивания принятых и отправленных файлов                                                          | [DownloadFile](https://green-api.com/docs/api/receiving/files/DownloadFile/)                             |
| `sending.sendMessage`                  | Метод предназначен для отправки текстового сообщения в личный или групповой чат                                           | [SendMessage](https://green-api.com/docs/api/sending/SendMessage/)                                       |
| `sending.sendFileByUpload`             | Метод предназначен для отправки файла, загружаемого через форму (form-data)                                               | [SendFileByUpload](https://green-api.com/docs/api/sending/SendFileByUpload/)                             |
| `sending.sendFileByUrl`                | Метод предназначен для отправки файла, загружаемого по ссылке                                                             | [SendFileByUrl](https://green-api.com/docs/api/sending/SendFileByUrl/)                                   |
| `sending.uploadFile`                   | Метод предназначен для загрузки файла в облачное хранилище, который можно отправить методом sendFileByUrl                 | [UploadFile](https://green-api.com/docs/api/sending/UploadFile/)                                         |
| `sending.sendLocation`                 | Метод предназначен для отправки сообщения геолокации                                                                      | [SendLocation](https://green-api.com/docs/api/sending/SendLocation/)                                     |
| `sending.sendContact`                  | Метод предназначен для отправки сообщения с контактом                                                                     | [SendContact](https://green-api.com/docs/api/sending/SendContact/)                                       |
| `sending.sendPoll`                     | Метод предназначен для отправки сообщения с опросом в личный или групповой чат                                            | [SendPoll](https://green-api.com/docs/api/sending/SendPoll/)                                             |
| `serviceMethods.checkAccount`         | Метод проверяет наличие аккаунта Account на номере телефона                                                              | [CheckAccount](https://green-api.com/docs/api/service/CheckAccount/)                                   |
| `serviceMethods.getAvatar`             | Метод возвращает аватар корреспондента или группового чата                                                                | [GetAvatar](https://green-api.com/docs/api/service/GetAvatar/)                                           |
| `serviceMethods.getContacts`           | Метод предназначен для получения списка контактов текущего аккаунта                                                       | [GetContacts](https://green-api.com/docs/api/service/GetContacts/)                                       |
| `serviceMethods.getContactInfo`        | Метод предназначен для получения информации о контакте                                                                    | [GetContactInfo](https://green-api.com/docs/api/service/GetContactInfo/)                                 |
| `serviceMethods.deleteMessage`         | Метод удаляет сообщение из чата                                                                                           | [DeleteMessage](https://green-api.com/docs/api/service/deleteMessage/)                                   |
| `serviceMethods.editMessage`           | Метод изменяет сообщение в чате                                                                                           | [EditMessage](https://green-api.com/docs/api/service/editMessage/)                                   |
| `serviceMethods.archiveChat`           | Метод архивирует чат                                                                                                      | [ArchiveChat](https://green-api.com/docs/api/service/archiveChat/)                                       |
| `serviceMethods.unarchiveChat`         | Метод разархивирует чат                                                                                                   | [UnarchiveChat](https://green-api.com/docs/api/service/unarchiveChat/)                                   |
| `serviceMethods.sendTyping`         | Метод предназначен для отправки уведомления о наборе текста или записи аудио в чат                                           | [SendTyping](https://green-api.com/docs/api/service/SendTyping/)                                   |
| `webhooks.startReceivingNotifications` | Метод предназначен для старта получения новых уведомлений                                                                 |                                                                                                          |
| `webhooks.stopReceivingNotifications`  | Метод предназначен для остановки получения новых уведомлений                                                              |                                                                                                          |
| `partner.GetInstances`   | Метод предназначен для получения всех инстансов аккаунтов созданных партнёром.                                           | [GetInstances](https://green-api.com/docs/partners/getInstances/)                       |
| `partner.CreateInstance`   | Метод предназначен для создания инстанса от имени партнёра.                                           | [CreateInstance](https://green-api.com/docs/partners/createInstance/)                       |
| `partner.DeleteInstanceAccount`   | Метод предназначен для удаления инстанса аккаунта партнёра.                                           | [DeleteInstanceAccount](https://green-api.com/docs/partners/deleteInstanceAccount/)                       |

## Документация по методам сервиса

[https://green-api.com/telegram/docs/api/](https://green-api.com/docs/api/).

## Сторонние продукты

- [requests](https://requests.readthedocs.io/en/latest/) - для HTTP запросов.
- [aiohttp](https://docs.aiohttp.org/) - для асинхронных HTTP запросов.

## Лицензия

Лицензировано на условиях [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/).
[LICENSE](../LICENSE).