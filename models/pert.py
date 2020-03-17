class Graph:
    graph = {}    
    states = [10]
    
    def getState(self,state):
        return self.graph[state]
    
    def add_state(self):
        self.states.append(self.states[-1] + 10)
        self.graph[self.states[-1]] = {
                        'in':set(),
                        'out':set()
                        }
    def add_input_to_state(self,state,activity):
        self.graph[state]['in'].add(activity)

    def add_output_to_state(self,state,activity):
        self.graph[state]['out'].add(activity)

    def getGraph(self):
        return self.graph

    def __init__(self):
        self.graph[self.states[-1]] = {
                'in':set(),
                'out':set()
                }

    def optimize(self):
        l = list(self.graph.keys())
        for i in l[:-1]:
            if len(self.graph[i]['out']) == 0:
                self.graph.pop(i)
            

if __name__=="__main__":
    pass
    
 

