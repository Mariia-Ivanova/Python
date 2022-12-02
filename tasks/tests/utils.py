import subprocess
import tempfile
from typing import List


def run_script(run_cmd: List[str], *file_contents: str, file_names=None) -> str:

    if file_names is None:
        file_names = []
        for file_content in file_contents:
            with tempfile.NamedTemporaryFile("w", delete=False) as f:
                f.write(file_content)
                file_names.append(f.name)

    result = subprocess.run(run_cmd + file_names, stdout=subprocess.PIPE)

    return result.stdout.decode("utf-8"), file_names
