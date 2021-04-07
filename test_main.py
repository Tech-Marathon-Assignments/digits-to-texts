# Test Case 1:
# Input: year = 2000
# Output: "2000 is a lap year"
def test_main_1(capfd):
    main(123)
    out, err = capfd.readouterr()
    assert out == "one hundred and twenty-three\n"

# Test Case 2:
# Input: year = 2001
# Output: "2001 is a lap year"
def test_main_2(capfd):
    main(211)
    out, err = capfd.readouterr()
    assert out == "two hundred and eleven\n"
