#documentation https://docs.robotframework.org/docs/extending_robot_framework/listeners_prerun_api/listeners
import os
from datetime import datetime, timedelta
from robot import result, running
from robot.api import logger
from robot.api.interfaces import ListenerV3

PASSING_TEMPLATE = """The test named "{test_name}" passed successfully. It started at {start_time} and ended at {end_time}, taking a total of {elapsed_time}. The steps executed were as follows:
{steps}"""

FAILING_TEMPLATE = """The test named "{test_name}" failed. It started at {start_time} and ended at {end_time}, taking a total of {elapsed_time}. The steps executed were as follows:
{steps}
The error encountered in test "{test_name}" was: {error_message}
"""

SKIPPED_TEMPLATE = """The test named "{test_name}" was skipped. It was scheduled to start at {start_time}. The reason for skipping is: {skip_reason}"""

TEMPLATES = {
    "PASS": PASSING_TEMPLATE,
    "FAIL": FAILING_TEMPLATE,
    "SKIP": SKIPPED_TEMPLATE
}

class RobotFrameworkResultAnalyzer(ListenerV3):
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, output="test_summary.txt"):
        self.output = output
        self.test_summary_file = open(self.output, "w", encoding="utf-8")

    
    def end_test(self, data: running.TestCase, result: result.TestSuite):
        name = data.name
        status = result.status
        start_time = result.start_time
        elapsed_time = result.elapsed_time
        end_time = start_time + elapsed_time
        steps_summary = ""
        for step in data.body:
            step_args = " ".join([arg for arg in step.args])
            step_full = f"{step.name} {step_args}".strip()
            steps_summary += f"{step_full}\n"
        test_summary = TEMPLATES[status].format(test_name=name, start_time=start_time, end_time=end_time, elapsed_time=elapsed_time, steps=steps_summary, error_message=result.message, skip_reason=result.message)
        self.test_summary_file.write(f"{test_summary}{os.linesep}")

    def close(self):
        self.test_summary_file.close()