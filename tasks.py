from pathlib import Path
from invoke import task

TYPES = {
    "raw": Path("robot/raw.robot"),
    "workflow": Path("robot/workflow.robot"),
    "bdd": Path("robot/bdd.robot"),
}

LISTENER = "src.RobotFrameworkResultAnalyzer"


@task
def demo(c, type="raw", dry_run=False):
    try:
        test_file = TYPES[type]
    except KeyError:
        raise ValueError(f"Type was allowed, allowed values {TYPES.keys()}")
    dryrun_option = ""
    if dry_run:
        dryrun_option = "--dryrun"
    c.run(f"cd demo && robot {dryrun_option} --listener {LISTENER} -d ../results --pythonpath=lib --pythonpath=../ {test_file}")