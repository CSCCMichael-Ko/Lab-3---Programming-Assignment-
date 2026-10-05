from pathlib import Path

path = Path('programming.txt')

contents = """
I also love working with data.
I also love making robots work."""

path.write_text(contents)
