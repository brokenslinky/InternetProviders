class InternetProvider:
    """A class representing an internet provider."""

    class Plan:
        """A plan offered by the InternetProvider"""
        def __init__(self, speed, price):
            self.speed = speed
            self.price = price

    def __init__(self, name):
        """Return a new InternetProvider with the name provided."""
        self.name = name
        self.plans = []

    def addPlan(self, speed, price):
        """
        Add a plan to the InternetProvider.

        Parameters:
            speed (Mb/s): The upload/download speed supported by the plan.
            price ($/mo): The monthly cost of the plan.
        """
        plan = InternetProvider.Plan(speed, price)
        self.plans.append(plan)

def plotOptions(providers):
    """
    Display a visual comparison of the providers

    Parameters:
        providers: A list of InternetProviders to compare.
    """
    import matplotlib.pyplot as plt

    for provider in providers:
        print(provider.name)
        speeds = []
        prices = []
        for plan in provider.plans:
            speeds.append(plan.speed)
            prices.append(plan.price)
            print(f'    {plan.speed} Mb/s    ${plan.price} / mo')
        plt.plot(speeds, prices, label=provider.name)
        print()

    plt.legend()
    plt.title('Comparison of Internet Service Providers')
    plt.xlabel('Speed (Mb/s)')
    plt.ylabel('Cost ($/mo)')
    plt.show()

if __name__ == '__main__':
    # Compare the internet service providers in Bellevue.
    import ExampleISPs
    providers = ExampleISPs.BellevueProviders()
    plotOptions(providers)