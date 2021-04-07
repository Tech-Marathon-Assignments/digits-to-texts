# Test Case 1:
# Input: 93
# Output: “Change: 50 20 20 2 1”
def test_main_1(capfd):
    main(123)
    out, err = capfd.readouterr()
    assert out == "one hundred and twenty-three\n"

# Test Case 2:
# Input: 113
# Output: “Change: 100 10 2 2”
def test_main_2(capfd):
    main(211)
    out, err = capfd.readouterr()
    assert out == "two hundred and eleven\n"
