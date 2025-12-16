import os
from pathlib import Path
from typing import Any

import yaml
from box import ConfigBox
from box.exceptions import BoxValueError

# Patch for ensure library on newer Python versions
import unittest
if not hasattr(unittest.TestCase, 'assertRaisesRegexp'):
    unittest.TestCase.assertRaisesRegexp = unittest.TestCase.assertRaisesRegex

from ensure import ensure_annotations

from textSummarizer.logging import logger


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox.

    Args:
        path (Path): Path to the YAML file

    Raises:
        BoxValueError: If YAML file is empty
        Exception: If file is not found or unreadable

    Returns:
        ConfigBox: Parsed YAML content
    """
    try:
        with open(path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise BoxValueError("YAML file is empty")

            logger.info(f"YAML file loaded successfully: {path}")
            return ConfigBox(content)

    except Exception as e:
        logger.error(f"Error reading YAML file: {path}")
        raise e


def create_directories(paths: list, verbose: bool = True) -> None:
    """
    Create directories if they do not exist.

    Args:
        paths (list): List of directory paths
        verbose (bool): usage of logger
    """
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get file size in KB.

    Args:
        path (Path): Path to file

    Returns:
        str: File size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"
