import logging

# Configure logger
logger=logging.getLogger('logger')
FORMAT = '%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

###################
# Graph Config    #
###################
GRAPH_COLOURS = ['purple', 'orange', 'black', 'blue', 'pink', "coral", "indigo", "forestgreen", "peru", "violet"]

######################
# Simulation Config  #
######################

# Number of times to run the tests for average
TEST_ITERATIONS = 10

# Time window across which sensors select a timestamp (affects Pr(collision))
SIMULATED_DURATION=10

# Tag sample sizes for simultation
SAMPLE_SIZES = [50, 100, 300, 500, 1000, 1500, 2000]

# (tag, slot) data from the research paper
PAPER_BINARY_PROTOCOL_DATA = [(50,181), (100,373), (300, 984), (500,1763), (1000, 3881), (1500, 5484), (2000, 7716)]