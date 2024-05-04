from typing import Optional

from flask import Flask
from flask_socketio import SocketIO
from engineio.async_drivers import gevent

socketio: Optional[SocketIO] = None


def init_socketio(app: Flask) -> None:
    global socketio
    if socketio is not None:
        raise ValueError('SocketIO is already initialized.')
    socketio = SocketIO(app, cors_allowed_origins='*', async_mode='gevent')


def get_socketio() -> SocketIO:
    global socketio
    if socketio is None:
        raise ValueError('SocketIO is not initialized.')
    return socketio
