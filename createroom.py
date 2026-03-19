import os
import asyncio
from livekit import api
from livekit.api import LiveKitAPI, VideoGrants, AccessToken
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("LIVEKIT_URL")
api_key = os.getenv("LIVEKIT_API_KEY")
api_secret = os.getenv("LIVEKIT_API_SECRET")


async def create_room():
    room_name = "interview-room"

    lkapi = LiveKitAPI(url, api_key, api_secret)

    try:
        await lkapi.room.delete_room(api.DeleteRoomRequest(room=room_name))
        print("Deleted existing room")
    except:
        print("No existing room to delete")

    await lkapi.room.create_room(api.CreateRoomRequest(name=room_name))
    print(f"Room created: {room_name}")
    await lkapi.aclose()

    token = AccessToken(api_key, api_secret)
    token.with_grants(VideoGrants(
        room_join=True,
        room=room_name,
        can_publish=True,
        can_subscribe=True,
        can_publish_data=True,
    ))
    token.with_identity("student")
    access_token = token.to_jwt()

    print(f"\nURL: {url}")
    print(f"\nAccess Token:\n{access_token}")


asyncio.run(create_room())