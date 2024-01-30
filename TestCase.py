class TestCase: 


    def __init__(self, fnc) -> None:
        self.fnc = fnc

    def test_testcase(self, expected_val, **kwargs): 

        try: 
            answer = self.fnc(**kwargs)
            assert(answer == expected_val)
            print(f"Test case passed: expected {expected_val} and got {answer}")
        except AssertionError: 
            print(f'Test case failed: expected {expected_val} but got {answer}')
