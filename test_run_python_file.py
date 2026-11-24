from functions.run_python_file import run_python_file

def test_result(target_dir: str, file_path: str, args: list[str] | None = None):
    result = run_python_file(target_dir, file_path, args)
    print(result)

test_result("calculator", "main.py")
test_result("calculator", "main.py", ["3 + 5"])
test_result("calculator", "tests.py")
test_result("calculator", "../main.py")
test_result("calculator", "nonexistent.py")
test_result("calculator", "lorem.txt")
