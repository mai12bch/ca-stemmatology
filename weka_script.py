import weka.core.jvm as jvm 
import weka.plot.graph as graph  # NB: pygraphviz and PIL are required
from weka.core.converters import Loader
from weka.classifiers import Classifier
import time 
# Start JVM (Java Virtual Machine) 
jvm.start() 

#Data folder 
data_dir = "/home/assen/Development/stemmatology/Python_Script/weka_wrapper/example_usage/data_dir/"


###################################################
'''Load dataset and print it (import Loader)'''####
###################################################
 
loader = Loader(classname="weka.core.converters.ArffLoader")

data = loader.load_file(data_dir + "iris.arff")
#data = loader.load_file(data_dir + "heinrichi.arff")

data.class_is_last()

#print data 
#print(data)


###################################################
''' Build classifier on dataset ''' ###############
###################################################
 
cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.3"])
cls.build_classifier(data)

#print(cls.to_help)

for index, inst in enumerate(data):
    pred = cls.classify_instance(inst)
    dist = cls.distribution_for_instance(inst)
# print
    print(str(index+1) + ": label index=" + str(pred) + ", class distribution=" + str(dist))


###################################################
''' Print model and draw a graph '''###############
###################################################

#print(cls)
#graph.plot_dot_graph(cls.graph)


###################################################
'''NaiveBayesUpdateable, incremental=True '''######
###################################################
'''
iris_inc = loader.load_file(data_dir + "iris.arff", incremental=True)
iris_inc.class_is_last()

print(iris_inc)

cls = Classifier(classname="weka.classifiers.bayes.NaiveBayesUpdateable")
cls.build_classifier(iris_inc)
for inst in loader:
    cls.update_classifier(inst)

print(cls)
'''
###################################################
''' Some Experiments ''' ##########################
###################################################

#   data_dir + "vote.arff"
#   data_dir + "anneal.arff"
'''
datasets = [
    data_dir + "iris.arff",
   data_dir + "vote.arff",
   data_dir + "anneal.arff"


]

classifiers = [
    Classifier(classname="weka.classifiers.rules.ZeroR"),
    Classifier(classname="weka.classifiers.trees.J48"),
    Classifier(classname="weka.classifiers.trees.REPTree"),
]
result = "exp.arff"

from weka.experiments import SimpleCrossValidationExperiment

exp = SimpleCrossValidationExperiment(
    classification=True,
    runs=10,
    folds=10,
    datasets=datasets,
    classifiers=classifiers,
    result=result)

exp.setup()
exp.run()

import weka.core.converters

loader = weka.core.converters.loader_for_file(result)
data = loader.load_file(result)

from weka.experiments import Tester, ResultMatrix

matrix = ResultMatrix(classname="weka.experiment.ResultMatrixPlainText")
tester = Tester(classname="weka.experiment.PairedCorrectedTTester")
tester.resultmatrix = matrix
comparison_col = data.attribute_by_name("Percent_correct").index
tester.instances = data

print(tester.header(comparison_col))
print(tester.multi_resultset_full(0, comparison_col))
print(tester.multi_resultset_full(1, comparison_col))

'''

jvm.stop()
