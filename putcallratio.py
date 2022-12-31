import refinedata

def putcallratio():
    df = refinedata.refinedata()
    calldf = df[df["Instrument Type"]=="CE"]
    putdf = df[df["Instrument Type"] == "PE"]
    oic_call = calldf["changeinOpenInterest"].sum()
    oic_put = putdf["changeinOpenInterest"].sum()
    putcallratio = oic_put/oic_call
    return putcallratio


