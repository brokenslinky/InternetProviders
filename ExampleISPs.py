
def BellevueProviders():
    """Return a list of the InternetProviders available in Bellevue."""
    from InternetProviders import InternetProvider
    providers = []

    Frontier = InternetProvider('Frontier')
    Frontier.addPlan(speed=50, price=30)
    Frontier.addPlan(speed=500, price=40)
    Frontier.addPlan(speed=1000, price=75)
    providers.append(Frontier)

    CenturyLink = InternetProvider('CenturyLink')
    CenturyLink.addPlan(speed=80, price=49)
    CenturyLink.addPlan(speed=140, price=49)
    providers.append(CenturyLink)

    xfinity = InternetProvider('Xfinity')
    xfinity.addPlan(speed=75, price=30)
    xfinity.addPlan(speed=175, price=45)
    xfinity.addPlan(speed=275, price=60)
    xfinity.addPlan(speed=500, price=75)
    xfinity.addPlan(speed=1000, price=90)
    #xfinity.addPlan(speed=2000, price=300)
    providers.append(xfinity)

    Viasat = InternetProvider('Viasat')
    Viasat.addPlan(speed=12, price=50)
    Viasat.addPlan(speed=25, price=150)
    providers.append(Viasat)

    HughesNet = InternetProvider('HughesNet')
    HughesNet.addPlan(speed=10, price=60)
    HughesNet.addPlan(speed=20, price=70)
    HughesNet.addPlan(speed=30, price=100)
    HughesNet.addPlan(speed=50, price=150)
    providers.append(HughesNet)
    return providers