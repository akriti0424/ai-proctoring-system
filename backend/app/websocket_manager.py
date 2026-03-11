from fastapi import WebSocket
from typing import List

class ConnectionManager:
    def __init__(self):
        self.admins: List[WebSocket] = []

    async def connect_admin(self, websocket: WebSocket):
        await websocket.accept()
        self.admins.append(websocket)

    def disconnect_admin(self, websocket: WebSocket):
        self.admins.remove(websocket)

    async def broadcast_to_admins(self, message: dict):
        for connection in self.admins:
            try:
                await connection.send_json(message)
            except:
                pass

manager = ConnectionManager()
