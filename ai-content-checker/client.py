import argparse
import asyncio
import sys

from temporalio.client import Client
from workflow import AIContentWorkflow


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    """Set up and return the argument parser.
    parser = argparse.ArgumentParser(description="Daily ChatGPT prompt tracker")
    parser.add_argument(
        "-p", "--prompt", required=True, help="The prompt to send to ChatGPT"
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=5,
        help="Interval in minutes between prompts (default: 5)",
    )
    args = parser.parse_args()
    """

    # Execute a workflow
    handle = await client.start_workflow(
        AIContentWorkflow.run,
        "Temporal",
        id="ai-content-check",
        task_queue="ai-content",
    )

    print(f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}")

    result = await handle.result()

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
