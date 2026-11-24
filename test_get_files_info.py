from functions.get_files_info import get_files_info

def test_result(target_dir: str, directory: str):
    result = get_files_info(target_dir, directory)

    if directory == ".":
        print(f"Result for current directory:")
    else:
        print(f"Result for '{directory}' directory:")

    print(result)

test_result("calculator", ".")
test_result("calculator", "pkg")
test_result("calculator", "/bin")
test_result("calculator", "../")