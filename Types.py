import random

geneset = [0,1,2,3,4,5,6,7,8,9]
target_length = 5
pop_size = 10

def uniform_crossover(parent1, parent2):
     mask = [1 , 1 , 0 , 1 , 0 , 1 , 1 , 0]#[random.randint(0, 1) for _ in range(target_length)]
     child1 = [parent1[i] if mask[i] == 1 else parent2[i] for i in range(len(parent1))]
     child2 = [parent1[i] if mask[i] == 0 else parent2[i] for i in range(len(parent2))]
     return child1 , child2

# ch1 , ch2 = uniform_crossover([1 , 0 , 1 , 1 , 0 , 0 , 1 , 1] , [0 , 0 , 0 , 1 , 1 , 0 , 1 , 0])
# print(ch1 , ch2)

def one_point_crossover(p1 , p2):
     point = sorted(random.sample(range(len(p1)) , 1))

     ch1 = p1[:point[0]] + p2[point[0]:]
     ch2 = p2[:point[0]] + p1[point[0]:]

     return ch1 , ch2


def two_point_crossover(p1 , p2 , prob):
     if random.random() < prob:
          point = sorted(random.sample(range(len(p1)) , 2))
          ch1 = p1[:point[0]] + p2[point[0]:point[1]] + p1[point[1]:]
          ch2 = p2[:point[0]] + p1[point[0]:point[1]] + p2[point[1]:]
     else:
          ch1 = p1.copy()
          ch2 = p2.copy()
     return ch1 , ch2



def threeParent_crossover(p1 , p2 , p3 , prob):
     r = random.random() 
     if r < prob:
          ch1 = [p1[i] if p1[i] == p2[i] else p3[i] for i in range(len(p1))]
          ch2 = [p1[i] if p1[i] == p2[i] else p3[i] for i in range(len(p1))]
     else:
          ch1 = p1.copy()
          ch2 = p2.copy()
     return ch1 , ch2

def PMX(p1 , p2):
     size = len(p1)
     ch1 = [None]*size
     ch2 = [None]*size

     point = sorted(random.sample(range(size) , 2))
     point1 = point[0]
     point2 = point[1]

     ch1[point1:point2]=p2[point1:point2]
     ch2[point1:point2]=p1[point1:point2]

     for i in range(size):
          if ch1[i] == None:
               if p1[i] not in ch1:
                    ch1[i] = p1[i]
               else:
                    value = p1[i]
                    while True:
                         index = ch1.index(value)
                         value = ch2[index]

                         if value not in ch1:
                              ch1[i] = value
                              break
                    

               if p2[i] not in ch2:
                    ch2[i] = p2[i]
               else:
                    value = p2[i]
                    while True:
                         index = ch2.index(value)
                         value = ch1[index]

                         if value not in ch2:
                              ch2[i] = value
                              break
     return ch1 , ch2
     
def shuffle_crossover(p1 , p2):
     random.shuffle(p1)
     random.shuffle(p2)
     ch1 , ch2 = one_point_crossover(p1 , p2)
     return ch1 , ch2 

p1 = [1 , 2 , 3 , 4, 5, 6]
p2 = [7 , 8 , 9 , 10 , 11 ,12]

c1 , c2 = shuffle_crossover(p1 , p2)
print(c1 , c2)


     


# ordered crossover between two parents
def ordered_crossover(parent1, parent2):
     size = len(parent1)
     start, end = 3 , 7 #sorted(random.sample(range(size), 2))
     child1 = [None]*size
     child2 = [None]*size
     child1[start:end] = parent1[start:end]
     child2[start:end] = parent2[start:end]
     p1_filtered = [x for x in parent2 if x not in child1[start:end]]
     p2_filtered = [x for x in parent1 if x not in child2[start:end]]
     child1 = [p1_filtered.pop(0) if x is None else x for x in child1]
     child2 = [p2_filtered.pop(0) if x is None else x for x in child2]

     return child1 , child2


# ch1 , ch2 = ordered_crossover([1 , 2 , 3 , 4 , 5 , 6 ,7 , 8 , 9],[4 , 5 , 2 , 1 , 8 , 7 , 6 , 9 , 3])
# print(ch1)
# print(ch2)


# replacement
def replacement_mutate(individual ,mutation_rate):
     index = random.randrange(0 , len(individual))
     child = individual[:]

     if random.random() < mutation_rate:
          new_gene , alter = random.sample(geneset , 2)

          if new_gene == child[index]:
               child[index] = alter
          else:
               child[index] = new_gene
     return child

# interchanging
def interchanging_mutate(individual, mutation_rate):
     individual = individual[:]
     if random.random() < mutation_rate:
          i, j = random.sample(range(len(individual)), 2)
          individual[i], individual[j] = individual[j], individual[i]
     return individual

# fliping
def fliping_mutate(individual , mutation_rate):
     if random.random() < mutation_rate:
          mask = [1 , 0 , 0 , 0 , 1 , 0 , 0 , 1]#[random.randint(0 , 1) for _ in range(len(individual))]
          for i in range(len(individual)):
               if mask[i]:
                    individual[i] = 0 if individual[i] == 1 else 1
     return individual

# ch = fliping_mutate([1 , 0 , 1 , 1 , 0 , 1 , 0 , 1])
# print(ch)

# reversing
def reversing_mutate(individual , mutation_rate):
     if random.random() < mutation_rate:
          point = random.randrange(0 , len(individual))
          # print(point)
          part1 = individual[:point]
          part2 = individual[point:]
          part2.reverse()
          part1.extend(part2)
     return part1

# print(reversing_mutate([1 , 0 , 1 , 1 , 0 , 1 , 0 , 1]))

