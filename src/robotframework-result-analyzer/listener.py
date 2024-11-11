class TestAnalyzerListener:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, output="test_summary.txt"):
        self.output = output