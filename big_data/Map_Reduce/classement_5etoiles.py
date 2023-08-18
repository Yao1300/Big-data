"""Programme pour compter le nombre évaluations d'un film"""
from mrjob.job import MRJob
from mrjob.step import MRStep

class CompteEvals3(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_eval3,
                  reducer=self.reducer_compte_eval3)
                  , 
           MRStep( reducer=self.reducer_classement  )   
             ]

    def mapper_get_eval3(self, _, line):    
         evals3 = line.split('\t')
         eval4=evals3[2]
         film=evals3[1]
         if eval4=="5":
            yield film, 1
    def reducer_compte_eval3(self, film, uns):
     yield str(sum(uns)).zfill(4), film
    def reducer_classement(self,film, nombre_5etoiles):
         for nombre in nombre_5etoiles:
              yield  nombre, int(film)
if __name__ == '__main__':
    CompteEvals3.run()