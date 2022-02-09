import numpy as np

#sample linear problem for genetic algorithm
"""
f(x) = a +2b + 3c +4d -30
"""
# Initializing n = 6
n = 6
# Initialization of chromosomes
# chromosome variable is the entire population
chromosome = np.random.randint(0, 30, (n, 4))
print("chromosomes :", chromosome)
epoch = 0


while epoch < 50:
    # Computation of the objective function
    objective = abs(30 - chromosome[:, 0] - 2 * chromosome[:, 1] - 3 * chromosome[:, 2] -
                    4 * chromosome[:, 3])
    print("Fitness object :", objective)

    # Selection of the fittest chromosome
    # Fittest chromosome have the higher probability to be selected for the next generation
    # To avoid divide by zero problem we add 1 to the value of objective[i]
    fitness = 1 / (1 + objective)
    print("Fitness :", fitness)

    # Calculating the total of fitness function
    # We will use this later to calculate the probability of a chromosome
    total = fitness.sum()
    print("Total :", total)

    # Calculating Probability for each chromosome
    prob = fitness / total
    print("Probability :", prob)

    # Selection using Roulette Wheel And Calculating Cumulative Probability
    # Roulette Selection in genetic algorithm is the process of selecting the chromosome in a random chance but the chromosome
    # with a higher probability also has the higher chance of being selected
    cum_sum = np.cumsum(prob)
    print("Cumulative Sum :", cum_sum)

    # Generating Random Numbers in the range 0-1
    Ran_nums = np.random.random((chromosome.shape[0]))
    print("Random Numbers :", Ran_nums)

    # Making a new matrix of chromosome for calculation purpose
    # we declare an array of zeros by numpy.zeros, so we can replace its value per index later easily
    chromosome_2 = np.zeros((chromosome.shape[0], 4))

    #here we loop to generate the new chromosomes
    # if the ran_num of that chromosome is less than the cum_sum of the chromosome, new chromosome will be equal to that chromsome
    for i in range(Ran_nums.shape[0]):
        for j in range(chromosome.shape[0]):
            if Ran_nums[i] < cum_sum[j]:
                chromosome_2[i, :] = chromosome[j, :]
                break

    #declaring new set of chromosomes or as we called earlier an entire population
    chromosome = chromosome_2
    print("Chromosomes after updation :", chromosome)

    # Crossover Process

    #first we declare some random floats for later use
    R = [np.random.random() for i in range(n)]
    print("Random Values :", R)

    # Crossover Rate
    # we declare a fixed crossover rate
    # now we compare if the ran_nums and the defined crossover rate.
    pc = 0.25
    flag = Ran_nums < pc
    print("Flagged Values :", flag)

    # Determining the cross chromosomes
    # so if the ran_nums of new chromosome[i] is less than the crossover rate
    # those which are less than will undergo the crossover process
    cross_chromosome = chromosome[[(i == True) for i in flag]]
    print("Cross chromosome :", cross_chromosome)
    len_cross_chrom = len(cross_chromosome)

    # Calculating cross values
    cross_values = np.random.randint(1, 3, len_cross_chrom)
    print("Cross Values :", cross_values)

    #setting up the array to be filled upon the crossover
    cpy_chromosome = np.zeros(cross_chromosome.shape)

    # Performing Cross-Over

    # Copying the chromosome values for calculations
    for i in range(cross_chromosome.shape[0]):
        cpy_chromosome[i, :] = cross_chromosome[i, :]

    if len_cross_chrom == 1:
        cross_chromosome = cross_chromosome
    else:
        for i in range(len_cross_chrom):
            c_val = cross_values[i]
            if i == len_cross_chrom - 1:
                cross_chromosome[i, c_val:] = cpy_chromosome[0, c_val:]
            else:
                cross_chromosome[i, c_val:] = cpy_chromosome[i + 1, c_val:]

    print("Crossovered Chromosome :", cross_chromosome)

    index_chromosome = 0
    index_newchromosome = 0
    for i in flag:
        if i == True:
            chromosome[index_chromosome, :] = cross_chromosome[index_newchromosome, :]
            index_newchromosome = index_newchromosome + 1
        index_chromosome = index_chromosome + 1

    print("New Chromosomes:", chromosome)

    # Calculating the total no. of generations
    a, b = chromosome.shape[0], chromosome.shape[1]
    total_gen = a * b
    print("Total Generations :", total_gen)

    # mutation rate = pm
    pm = 0.1
    no_of_mutations = int(np.round(pm * total_gen))
    print("No. of Mutations :", no_of_mutations)

    # Calculating the Generation number
    gen_num = np.random.randint(0, total_gen - 1, no_of_mutations)
    print(" Generated Random Numbers : ", gen_num)

    # Generating a random number which can replace the selected chromosome to be mutated
    Replacing_num = np.random.randint(0, 30, no_of_mutations)
    print(" Numbers to be replaced : ", Replacing_num)

    for i in range(no_of_mutations):
        a = gen_num[i]
        row = a // 4
        col = a % 4
        chromosome[row, col] = Replacing_num[i]

    print(" Chromosomes After Mutation : ", chromosome)

    epoch = epoch + 1
    print(epoch)