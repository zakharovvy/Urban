import asyncio


async def start_strongman(name:str, power:int):
    strong = 1/power
    print(f'Силач {name} начал соревнования.')
    for i in range (1,6):
        await asyncio.sleep(strong)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_strongman_starter():
    t1 = asyncio.create_task(start_strongman('Pasha', 3))
    t2 = asyncio.create_task(start_strongman('Denis', 4))
    t3 = asyncio.create_task(start_strongman('Apollon', 5))
    result = await asyncio.gather(t1,t2,t3) #Этот метод удобнее чем прописывать await t1 await2 и т.д.



asyncio.run(start_strongman_starter())