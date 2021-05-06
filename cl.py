import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 9898, loop=loop)
    writer.write(message.encode())
    data = await reader.read(1000)
    print(f'Ответ сервера: {data.decode()}')


loop = asyncio.get_event_loop()
while True:
    message = input("Введите сообщение или exit для выхода: ")
    if message == "exit":
        loop.close()
        break
    else:
        loop.run_until_complete(tcp_echo_client(message, loop))