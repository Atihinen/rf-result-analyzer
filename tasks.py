from invoke import task

@task
def demo(c, dry_run=False):
    dryrun_option = ""
    if dry_run:
        dryrun_option = "--dryrun"
    c.run(f"cd demo && robot {dryrun_option} -d ../results --pythonpath=lib robot")