import os

def test_log_file_created():
    assert os.path.exists("logs/system.json"), "Log file should exist after run"
