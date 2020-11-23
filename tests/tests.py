from click.testing import CliRunner
from autoflow.main import new, git_cli, jump, start
import os

# Start: Test incorrect usage
def test_start_wrong():
    runner = CliRunner()
    result = runner.invoke(start.start)
    assert result.output.rstrip('\n') == "Usage: start [OPTIONS] DIR\nTry 'start --help' for help.\n\nError: Missing argument 'DIR'."

# Start: test when the project doesn't exist
def test_start_noproj():
    runner = CliRunner()
    result = runner.invoke(start.start, ['testproj'])
    assert result.output.rstrip('\n') == "😅 Project doesn't exists"

# Start: test when project exists but af-config.json doesn't
def test_start_proj_noconfig():
    runner = CliRunner()
    result = runner.invoke(start.start, ['myproject'])
    assert result.output.rstrip('\n') == "🤦 af-config.json doesn't exists"

# Start: test when both the project and local configuration file exists
def test_start_proj_config():
    runner = CliRunner()
    result = runner.invoke(start.start, ['myproject2'])

# Git-cli: test command normally used
# This should be tested locally, and not within Github Actions due to credentials

# Jump: test normal af jump with existing repository
def test_jump_existing():
    runner = CliRunner()
    result = runner.invoke(jump.jump, ['myproject2'])
    assert result.exit_code == 0
    assert os.getcwd() == '/home/runner/work/autoflow/autoflow/myproject2'



