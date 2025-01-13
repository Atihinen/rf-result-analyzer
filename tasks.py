from pathlib import Path
from invoke import task
from genai.analyzer_bot import analyze_test_results

TYPES = {
    "raw": Path("robot/raw.robot"),
    "workflow": Path("robot/workflow.robot"),
    "bdd": Path("robot/bdd.robot"),
}

LISTENER = "src.RobotFrameworkResultAnalyzer"


@task
def demo(c, type="raw", level="plain", dry_run=False):
    try:
        test_file = TYPES[type]
    except KeyError:
        raise ValueError(f"Type was allowed, allowed values {TYPES.keys()}")
    dryrun_option = ""
    if dry_run:
        dryrun_option = "--dryrun"
    c.run(f"cd demo && robot --nostatusrc {dryrun_option} --variable LEVEL:{level} --listener {LISTENER} -d ../results --pythonpath=lib --pythonpath=../ {test_file}")
    analysis = analyze_test_results("demo/test_summary.txt")
    print(analysis)

@task
def lint(c):
    c.run("pylint src")

@task
def build(c):
    c.run("pdm import -f requirements requirements.txt")
    c.run("pdm install")
    c.run("pdm build")

