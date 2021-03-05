def likelihood():
    likelihoods=(50, 38, 27, 99, 4)
    return (min(likelihoods),max(likelihoods))

def run():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value[0]}%")
    print(f"Maximum likelihood of falling: {value[1]}%")

if __name__=='__main__':
    run()
