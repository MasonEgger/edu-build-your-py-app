import asyncio
import concurrent.futures

from activities import say_hello
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import AIContentWorkflow


async def main():
    client = await Client.connect("localhost:7233", namespace="default")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as activity_executor:
        worker = Worker(
            client,
            task_queue="ai-content",
            workflows=[AIContentWorkflow],
            activities=[say_hello],
            activity_executor=activity_executor,
        )
        print("Starting the worker....")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
