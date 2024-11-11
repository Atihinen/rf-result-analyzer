#documentation https://docs.robotframework.org/docs/extending_robot_framework/listeners_prerun_api/listeners
from robot import result, running
from robot.api.interfaces import ListenerV3
class TestAnalyzerListener(ListenerV3):
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, output="test_summary.txt"):
        raise Exception("testing")
        self.output = output
        self.test_summary_file = open(self.output, "w", encoding="utf-8")

    
    def end_test(self, data: running.TestCase, result: result.TestSuite):
        self.test_summary_file.write(data)

    def close(self):
        self.test_summary_file.close()