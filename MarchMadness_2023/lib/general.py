import argparse

def get_options():
    """Get the command line options"""
    parser = argparse.ArgumentParser(description='March Madness 2023')
    parser.add_argument('-n', '--num-sims', help='Number of simulations to run', type=int, default=100_000)
    
    return parser.parse_args()
