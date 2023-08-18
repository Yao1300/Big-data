"""Programme pour compter le nombre évaluations d'un film"""
from mrjob.job import MRJob
from mrjob.step import MRStep

class CompteEvals3(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_eval3,
                   reducer=self.reducer_compte_eval3)       ]

    def mapper_get_eval3(self, _, line):    
         evals3 = line.split('\t')
         eval4=evals3[2]
         eval3=evals3[1]
         if eval4=="5":
            yield eval3, 1
    def reducer_compte_eval3(self, eval3, uns):
     yield eval3, sum(uns)
if __name__ == '__main__':
    CompteEvals3.run()