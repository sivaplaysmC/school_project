import asyncio


async def hello():
    print("Hi")

# while 1 : 
#     asyncio.run(hello())
async def main () : 
    await asyncio.create_task(hello())

    await asyncio.sleep(2 )
    asyncio.create_task(hello())
    asyncio.create_task(hello())
# loop = asyncio.get_event_loop()

# loop.run(main())
asyncio.run(main())
