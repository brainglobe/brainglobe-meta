import subprocess


def test_smoke_cli() -> None:
    """
    Smoke test the citation CLI command.
    """
    completed_process: subprocess.CompletedProcess = subprocess.run(
        ["cite-brainglobe", "--help"],
        capture_output=True,
        text=True,
    )

    assert (
        completed_process.returncode == 0
    ), "Smoke test citation CLI exited with code: "
    f"{completed_process.returncode}.\n"
    f"STDERR capture: {completed_process.stderr}."
