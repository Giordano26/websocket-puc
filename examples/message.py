import asyncio
import websockets

SERVER_IP = "ws://localhost:"
PORT = 8765

async def msg():
    uri = SERVER_IP + str(PORT)
    async with websockets.connect(uri) as websocket:
        await websocket.send("Eu sou o Jonga")
        msg_send = await websocket.recv()
        print(f"Recebi: {msg_send}")

# Execute o loop de eventos do asyncio
asyncio.run(msg())
