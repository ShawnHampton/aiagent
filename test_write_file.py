from functions.write_file import write_file

def test_result(target_dir: str, file_path: str, content: str):
    result = write_file(target_dir, file_path, content)
    print(result)

test_result("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
test_result("calculator", "pkg/morelorem.txt", "lorem ipsim dolor sit amet")
test_result("calculator", "/tmp/temp.txt", "this should not be allowed")