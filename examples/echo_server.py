import asyncio
from websockets.server import serve

PORT = 8765

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", PORT):
        print("Web socket server on, listening on PORT: " + str(PORT))
        print("Waiting for conections...")
        await asyncio.Future()  # run forever

asyncio.run(main())