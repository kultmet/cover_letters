import asyncio

import aio_pika


async def main() -> None:
    connection = await aio_pika.connect_robust(
        'amqp://guest:guest@localhost:5672/'
    )

    async with connection:
        routing_key = 'test_queue'

        channel = await connection.channel()
        for i in range(100):
            await channel.default_exchange.publish(
                aio_pika.Message(body=f'хуй {i} пососи мою жопу!!!!!!'.encode()),
                routing_key=routing_key,
            )


if __name__ == '__main__':
    asyncio.run(main())