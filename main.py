import time
import asyncio
from src.spotify import get_currently_playing
from src.scenes import update_light_scene

WAIT_SECONDS = 2

async def main():

    print('Running Spotify process....')
    previous_song = None
    playback = get_currently_playing()
    current_song = playback.get('song')

    while True:
        if previous_song == current_song:
            # Song is still the same. Wait a bit and check again
            time.sleep(WAIT_SECONDS)
            playback = get_currently_playing()
            current_song = playback.get('song')

        else:
            # Change the song name
            print(f'Song changed to {current_song} by {playback.get("artist")}')
            previous_song = current_song

            # Attempt to change scene based on new song
            await update_light_scene(playback)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError or KeyboardInterrupt as e:
        print(f'Ending shopify light process: {e}')
    except Exception as e:
        print(f'Non-graceful exit: {e}')