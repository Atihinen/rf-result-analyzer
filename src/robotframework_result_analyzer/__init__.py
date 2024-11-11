from .listener import TestAnalyzerListener

class RobotFrameworkResultAnalyzer(TestAnalyzerListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)