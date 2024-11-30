# Initial steps/scenarios
steps_1 = ["open browser", "navigate to page", "click login"]
steps_2 = ["open browser", "navigate to page", "fill form"]
steps_3 = ["open browser", "navigate to page", "click login", "click log out"]

# Convert each scenario's steps to frozensets
scenario_1 = frozenset(steps_1)
scenario_2 = frozenset(steps_2)
scenario_3 = frozenset(steps_3)

# Dictionary of scenarios with frozensets
dic_scenarios = {
    "Test Case 1": scenario_1,
    "Test Case 2": scenario_2,
    "Test Case 3": scenario_3
}

# Function to check if a new test scenario already exists
#If we want to see only exact matches:
def check_exact_matches(test_name, new_steps, existing_scenarios):
    new_scenario = frozenset(new_steps)
    if new_scenario in existing_scenarios.values():
        duplicate = [key for key, value in existing_scenarios.items() if value == new_scenario]
        print('scenario already exists in the', duplicate)
    else:
            print('it is new scenario')

#If we want to see that such steps already exist in any of our scenarios:
def check_scenario(test_name, new_steps, existing_scenarios):
    new_scenario = frozenset(new_steps)
    duplicate = []
    for key, val in existing_scenarios.items():
        if val.issuperset(new_scenario):
            duplicate.append(key)
    if duplicate:
            print('scenario already exists in the', duplicate)
    else:
            print('it is new scenario')


new_steps = ["open browser", "navigate to page", "click login"]  # Same steps as Test Case 1 and part of Test Case 3
check_exact_matches("Test Case 4", new_steps, dic_scenarios)
check_scenario("Test Case 4", new_steps, dic_scenarios)