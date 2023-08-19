""" Programme pour compter le nombre évaluations d'un film"""
from mrjob.job import MRJob
from mrjob.step import MRStep
from essai2 import est_numerque # if not element.isdigit()
class CompteEvals2(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_data,
                   reducer=self.reducer_compte_jointure)       ]

    def mapper_get_data(self, _, line):
         line = line.strip()  
         line=line.replace('\t',',')
         line=line.replace('|',',')
         datas= line.split(',')
         if len(datas)==4:
             id_film=datas[1]
             eval=datas[2]
             yield id_film, eval
         elif len(datas)>4:
             id_film=datas[0]
             titre=datas[1]
             yield id_film, titre 
    def reducer_compte_jointure(self, id_film,titre_eval):
        titre_eval=[x for x in titre_eval]
        titre=''
        for caract in titre_eval:
            if est_numerque(caract)==False: # if not caract .isdigit()
                titre=caract
                titre_eval.remove(caract)
                break
        for element in titre_eval:
           yield titre, element    
if __name__ == '__main__':
    CompteEvals2.run()