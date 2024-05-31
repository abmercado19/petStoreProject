
def before_all(context):
    context.base_url = "http://localhost:8080/api/v3/"


def before_scenario(context, scenario):
    print("-" * 40)
    print("Running Scenario: {}".format(scenario.name))
    print("-" * 40)
