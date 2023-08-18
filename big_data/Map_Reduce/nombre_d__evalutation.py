""" Programme pour compter le nombre évaluations d'un film"""
from mrjob.job import MRJob
from mrjob.step import MRStep
class CompteEvals2(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_eval2,
                   reducer=self.reducer_compte_eval2)       ]

    def mapper_get_eval2(self, _, line):    
         evals2 = line.split('\t')
         if evals2[1]=="419":
            eval2=evals2[1]
            yield eval2, 1
    def reducer_compte_eval2(self, eval2, uns):
     yield eval2, sum(uns)
if __name__ == '__main__':
    CompteEvals2.run()