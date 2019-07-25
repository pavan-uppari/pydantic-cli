"""
Simple Example of using Pydantic to generate a CLI

This example will generate a CLI tool with 2 (required) positional arguments
"""
from pydantic import BaseModel

from pydantic_cli import run_and_exit


class Options(BaseModel):
    input_file: str
    max_records: int


def example_runner(opts: Options) -> int:
    print(f"Mock example running with {opts}")
    print(f"Fields {opts.fields}")
    return 0


if __name__ == "__main__":
    run_and_exit(Options, example_runner, description=__doc__, version='0.1.0')
