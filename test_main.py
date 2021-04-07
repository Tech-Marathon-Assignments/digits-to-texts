from main import main

# Test Case 1:
# Input: 123
# Output: “one hundred and twenty-three”
def test_main_1(capfd):
    main(123)
    out, err = capfd.readouterr()
    assert out == "one hundred and twenty-three\n"

# Test Case 2:
# Input: 211
# Output: “two hundred and eleven”
def test_main_2(capfd):
    main(211)
    out, err = capfd.readouterr()
    assert out == "two hundred and eleven\n"
