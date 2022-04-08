#  Copyright (C) 2021 The Authors

from . import *


@BotzHub.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def starter(event):
    user = await BotzHub.get_entity(event.sender_id)
    if not await check_user(event.sender_id):
        await add_user(event.sender_id)
    await event.reply(
        f"Welcome Boss! I hope you are going to have a great time with us. /n So happy to have you among us",
        
    )
