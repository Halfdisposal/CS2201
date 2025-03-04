import numpy as np
class Individual():
    def __init__(self, generation = 0, relative_position = 0, prededing_generation_info = (0, 0)):
        self.gen = generation
        self.rel = relative_position
        self.pre = prededing_generation_info
        self.relation_coeff = 0

i1 = Individual(1, 1)
i2 = Individual(1, 2)
i3 = Individual(2, 1, (1, 2))
i4 = Individual(2, 2, (1, 2))
i5 = Individual(3, 1, (0, 1))
i6 = Individual(3, 2, (2, 3))
i7 = Individual(4, 1, (0, 1))
i8 = Individual(4, 2, (2, 3))
i9 = Individual(4, 3, (2, 3))
generations = [[i1, i2], [i3, i4], [i5, i6], [i7,i8, i9]]
individuals = [i8, i7]
def find_relation(individuals, generations):
    iterations = 0
    found_link = False
    while not found_link and iterations < 100:
        relations = []
        parents = []
        individual1 = individuals[0]
        individual2 = individuals[1]
        if individual1 == individual2:
            print('Same Individuals')
            break 
        else:
            print(f'Different Individual in Iteration {iterations+1}')
            for generation in generations:
                set_individual = set(individuals)
                set_generation = set(generation)
                if set_generation.intersection(set_individual) != set():
                   current_gen_index = generations.index(generation)
            preceed_generation = generations[current_gen_index - 1]
            for parent in preceed_generation:
                if parent.rel == individual1.pre[0] or parent.rel == individual1.pre[1]:
                    relations.append((parent, individual1))
                    parents.append(parent)
                if parent.rel == individual2.pre[0] or parent.rel == individual2.pre[1]:
                    relations.append((parent, individual2) )
                    parents.append(parent)
            if parents[0].pre == parents[1].pre:
                    found_link = True
            individuals = parents
           
        for relation in relations:
                    print('Parent: ',relation[0].gen, relation[0].rel, relation[0].pre, 'Child: ',relation[1].gen, relation[1].rel, relation[1].pre)

    for relation in relations:
        print('Closest Common Ancestors: ',relation[0].gen, relation[0].rel, relation[0].pre)
    iterations += 1




if __name__ == '__main__':
    find_relation(individuals, generations)
