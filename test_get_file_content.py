from functions.get_file_content import get_file_content

def test_result(target_dir: str, file_path: str):
    result = get_file_content(target_dir, file_path)

    print(f"{file_path} length: {len(result)}")
    print(f"{file_path} truncated: {'truncated' in result}")

    print(f"Result for '{file_path}' file_path:")
    print(result)

test_result("calculator", "lorem.txt")
test_result("calculator", "main.py")
test_result("calculator", "pkg/calculator.py")
test_result("calculator", "/bin/cat")
test_result("calculator", "pkg/does_not_exist.py")