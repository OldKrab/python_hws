import os
import click
import aiohttp
import asyncio

IMAGES_URL = "https://random-image-pepebigotes.vercel.app/api/random-image"


async def get_image(session: aiohttp.ClientSession, file_path: str):
    async with session.get(IMAGES_URL) as response:
        if not response.ok:
            raise RuntimeError(f"Error: response status is {response.status}, {await response.text()}")

        bytes = await response.read()
        with open(file_path, "wb") as file:
            file.write(bytes)


async def get_images(files_number: int, folder: str):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(files_number):
            task = asyncio.create_task(
                get_image(session, os.path.join(folder, f"image_{i}.jpeg"))
            )
            tasks.append(task)
        done = 0
        for task in tasks:
            print(f"Loaded {done}/{len(tasks)}", end="\r")
            await task
            done += 1
        print()


@click.command()
@click.argument("files_number", type=int)
@click.argument("folder", type=str)
def main(files_number, folder) -> None:
    asyncio.run(get_images(files_number, folder))


main()
