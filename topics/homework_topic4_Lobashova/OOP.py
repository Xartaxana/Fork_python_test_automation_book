# Write a TestCase class with methods for setup(), run(), and teardown().
# Create objects of the TestCase class to represent individual test cases.
class TestCase:
    # Constructor of the class
    def __init__(self, name):
        self.name = name  # Attribute/Property/State

    def setup(self):
        print(f"Preparing for: {self.name}")

    def run(self):
        print(f"Running test case: {self.name}")

    def teardown(self):
        print(f"Clearing after: {self.name}")


print('For first test')
test = TestCase("Login Test")
test.setup()
test.run()
test.teardown()

print('For second test')
test2 = TestCase("Index page Test")
test2.setup()
test2.run()
test2.teardown()


# Implement method overriding in a test automation context.
# Override a method in the child test class to customize the test execution.
class ChildTestCase(TestCase):

    def setup(self):
        print(f"Child preparing for: {self.name}")

    def run(self):
        print(f"Child running test case: {self.name}")


print('For child test')
child_test = ChildTestCase("Child Login Test")
child_test.setup()
child_test.run()
child_test.teardown()  # will use method from parent class


# Create a multiple inheritance example: Write a class that inherits from multiple parent classes
# (e.g., BaseTest and a custom mixin class), and check how MRO impacts method calls.
class BaseTest:
    # Constructor of the class
    def __init__(self, name):
        self.name = name  # Attribute/Property/State

    def setup(self):
        print(f"Base preparing for: {self.name}")

    def run(self):
        print(f"Base running test case: {self.name}")

    def teardown(self):
        print(f"Base clearing after: {self.name}")


class MixTest(TestCase, BaseTest):

    def setup(self):
        print(f"Mix preparing for: {self.name}")

    def teardown(self):
        BaseTest.teardown(self)


print('For test with two parents')
mix_test = MixTest("Mix Login Test")
mix_test.setup()  # from MixTest
mix_test.run()  # from TestCase
mix_test.teardown()  # from BaseTest

print(MixTest.mro())
