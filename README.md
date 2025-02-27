# rf-result-analyzer
rf-result-analyzer is a tool designed to analyze Robot Framework test results with AI-powered insights using AnythingLLM. The repository includes demo tests, a custom listener to capture test execution data, and prompts for automated failure analysis and improvement suggestions.

## Project

This project is providing a global [listener](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface) to Robot Framework to make test output human-readable by generating a txt file.

[Listener is released as a PyPI package](https://pypi.org/project/RobotFrameworkResultAnalyzer/)

To use the listener, first install it via PyPI, then run `robot --listener RobotFrameworkResultAnalyzer /path/to/robot/tests`

The listener by default will create a `test_summary.txt` file in the location where you run the robot command. Use this file to check if your test cases are human-readable. If they are, then they can also be used with GenAI LLM solutions to help debug the test case results.

## Development environment

To use the GenAI-powered bot, you need to have Ollama installed as well; otherwise, this is purely a Python-based project.

### Requirements

1. Python 3.9 or higher
1. pip for Python
1. [Ollama](https://ollama.com/)

### Setup

1. Clone the repository
1. Run `pip3 install -r dev-requirements.txt`

### Running the local project

To test out the demo environment, run the command `invoke demo`. This will run robot tests under `demo/robot` and generate `test_summary.txt` under the `demo` folder.

`test_summary.txt` is generated by the listener code when the tests are executed.

Check `invoke demo -h` for more options.

### Using Ollama with analyze "bot"

To ask the GenAI "bot" to analyze test results, run `invoke demo -a` to automatically provide the `test_summary.txt` to an LLM model, which will print to the console possible fixes for the test cases if they failed. Feel free to change the default model to something more appropriate to get better results.

# Contributing to the Project

Thank you for your interest in contributing to our project! Here are some guidelines to help you get started:

## How to Contribute

1. **Fork the Repository**: Start by forking the repository to your own GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine using:
    ```sh
    git clone https://github.com/Atihinen/rf-result-analyzer.git
    ```

3. **Create a Branch**: Create a new branch for your feature or bug fix:
    ```sh
    git checkout -b feature-or-bugfix-name
    ```

4. **Make Changes**: Make your changes to the codebase. Ensure your code follows the project's coding standards and conventions.

5. **Commit Changes**: Commit your changes with a clear and descriptive commit message:
    ```sh
    git commit -m "Description of the changes made"
    ```

6. **Push Changes**: Push your changes to your forked repository:
    ```sh
    git push origin feature-or-bugfix-name
    ```

7. **Create a Pull Request**: Open a pull request to the main repository. Provide a clear description of your changes and any related issues.

## Reporting Issues

If you encounter any issues or have suggestions for improvements, please open an issue in the repository. Provide as much detail as possible to help us understand and address the problem.

## Getting Help

If you need help or have questions, feel free to reach out by opening an issue.

Thank you for contributing!