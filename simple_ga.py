from fuzzywuzzy import fuzz
import random
import string


class Agent:

    def __init__(self, length):
        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.fitness = 0

    def __str__(self):
        return f'String is {self.string} and Fitness is {self.fitness}'


in_string = None
len_in_string = None
population = None
generations = None


def ga():
    agents = agent_init(len_in_string, population)

    for generation in range(generations):
        print(f'Generation is {generation}')

        agents = fitness(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)

        if any(agent.fitness >= 95 for agent in agents):
            print('String Matched')
            exit(0)


def agent_init(length, pop):
    return [Agent(length) for _ in range(pop)]


def fitness(agents):
    for agent in agents:
        agent.fitness = fuzz.ratio(agent.string, in_string)
    return agents


def selection(agents):
    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    agents = agents[:int(0.2 * len(agents))]
    print('\n'.join(map(str, agents)))
    return agents


def crossover(agents):
    offsprings = []

    for _ in range(int((population - len(agents)) / 2)):
        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = Agent(len_in_string)
        child2 = Agent(len_in_string)
        split = random.randint(0, len_in_string)
        child1.string = parent1.string[0:split] + parent2.string[split:len_in_string]
        child2.string = parent2.string[0:split] + parent1.string[split:len_in_string]

        offsprings.append(child1)
        offsprings.append(child2)

    agents.extend(offsprings)

    return agents


def mutation(agents):
    for agent in agents:

        for idx, param in enumerate(agent.string):

            if random.uniform(0.0, 1.0) <= 0.1:
                agent.string[:idx] + random.choice(string.ascii_letters) + agent.string[idx + 1:len_in_string]

    return agents


if __name__ == '__main__':
    in_string = 'jomon'
    len_in_string = len(in_string)
    population = 1000
    generations = 1000
    ga()
