from models.pert import Graph
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def show_graph(filename):
    data = pd.read_excel(filename)
    activity = {}
    duration = {}
    for i in range(len(data)):
        duration[data.ix[i, 'ID']] = data.ix[i, 'Te']
        if data.ix[i, 'predecessor'] != "-":
            activity[data.ix[i, 'ID']] = set(data.ix[i, 'predecessor'].split(','))
        else:
            activity[data.ix[i, 'ID']] = set()

    graph = Graph()

    for i in activity:
        if len(activity[i]) == 0:
            graph.add_output_to_state(graph.states[0], i)
            graph.add_state()
            graph.add_input_to_state(graph.states[-1], i)
        if len(activity[i]) == 1:
            for state in graph.getGraph():
                if graph.getState(state)['in'] == activity[i]:
                    graph.add_output_to_state(state, i)
            for state in graph.getGraph():
                if i in graph.getState(state)['in']:
                    pass
            else:
                graph.add_state()
                graph.add_input_to_state(graph.states[-1], i)
        if len(activity[i]) > 1:
            for state in graph.getGraph():
                found = True
                for precedessor in activity[i]:
                    if precedessor not in graph.getState(state)['in']:
                        found = False
                        break
                if found:
                    graph.add_output_to_state(state, i)
                    for state in graph.getGraph():
                        if i in graph.getState(state)['in']:
                            pass
                    else:
                        graph.add_state()
                        graph.add_input_to_state(graph.states[-1], i)
            if not found:
                graph.add_state()
                for precedessor in activity[i]:
                    graph.add_input_to_state(graph.states[-1], precedessor)
                graph.add_output_to_state(graph.states[-1], i)
                for state in graph.getGraph():
                    if i in graph.getState(state)['in']:
                        pass
                else:
                    graph.add_state()
                    graph.add_input_to_state(graph.states[-1], i)

    graph.optimize()
    for i in graph.getGraph():
        print(i, graph.getState(i))

    G = nx.DiGraph()
    keys = list(graph.getGraph().keys())
    labels = {}
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            for out in graph.getGraph()[keys[i]]['out']:
                if out in graph.getGraph()[keys[j]]['in']:
                    G.add_edge(keys[i], keys[j], edge_labels=out, duration=duration[out] )
                    labels[keys[i], keys[j]] = out
    pos=nx.layout.spring_layout(G,k =0.4)
    plt.figure()
    nx.draw(G,pos,
            with_labels=True,
            node_size=500,
            alpha=0.5,
            arrows=True)
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels= labels,
                                 font_size =6,
                                 label_pos=0.5)
    plt.show()
    plt.savefig("graph.png")