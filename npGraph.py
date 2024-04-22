import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(graph, path=None, bfs_tree=None, title="Graph"):
    pos = nx.spring_layout(graph)  # Generate a layout for visualizing the graph
    plt.figure(figsize=(12, 8))    # Set the figure size
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue')  # Draw nodes
    nx.draw_networkx_labels(graph, pos)  # Draw node labels
    nx.draw_networkx_edges(graph, pos, edge_color='gray')  # Draw all edges

    # Highlight the path if provided
    if path:
        edges_in_path = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color='blue', width=2)

    # Highlight BFS tree if provided
    if bfs_tree:
        nx.draw_networkx_edges(graph, pos, edgelist=bfs_tree, edge_color='red', width=2)

    plt.title(title)
    plt.show()

def dijkstra(graph, start, end):
    try:
        path = nx.dijkstra_path(graph, start, end)
        print(f'Dijkstra shortest path from {start} -> {end}: {path}')
        plot_graph(graph, path=path, title=f"Dijkstra's Path from {start} to {end}")
    except Exception as e:
        print(f"Error in Dijkstra's algorithm: {str(e)}")

def astar(graph, start, end):
    try:
        path = nx.astar_path(graph, start, end)
        print(f'A* shortest path from {start} -> {end}: {path}')
        plot_graph(graph, path=path, title=f"A* Path from {start} to {end}")
    except Exception as e:
        print(f"Error in A* algorithm: {str(e)}")

def bfs(graph, start):
    try:
        bfs_edges = list(nx.bfs_edges(graph, start))
        bfs_tree = [(start, *edge) for edge in bfs_edges]  # Construct the tree from the edges
        print(f'Breadth-first search from {start}: {bfs_edges}')
        plot_graph(graph, bfs_tree=bfs_edges, title=f"BFS Tree from {start}")
    except Exception as e:
        print(f"Error in BFS: {str(e)}")

park_graph = nx.Graph()
park_list = [
    ('Joshua Tree', 'Shenandoah', 8),
    ('Olympic', 'Shenandoah', 8),
    ('Badlands', 'Lassen Volcanic', 1),
    ('Great Smoky Mountains', 'Cuyahoga Valley', 1),
    ('Acadia', 'Sequoia and Kings Canyon', 2),
    ('Joshua Tree', 'Mount Rainier', 3),
    ('Bryce Canyon', 'Saguaro', 1),
    ('Bryce Canyon', 'Badlands', 2),
    ('Great Smoky Mountains', 'Sequoia and Kings Canyon', 7),
    ('Grand Canyon', 'Shenandoah', 7),
    ('Rocky Mountain', 'Lassen Volcanic', 3),
    ('Acadia', 'Shenandoah', 2),
    ('Joshua Tree', 'Cuyahoga Valley', 7),
    ('Joshua Tree', 'Arches', 2),
    ('Rocky Mountain', 'Bryce Canyon', 1),
    ('Everglades', 'Lassen Volcanic', 9),
    ('Grand Canyon', 'Mount Rainier', 3),
    ('Glacier', 'Bryce Canyon', 3),
    ('Zion', 'Lassen Volcanic', 2),
    ('Yellowstone', 'Glacier', 1),
    ('Great Smoky Mountains', 'Mount Rainier', 8),
    ('Grand Canyon', 'Rocky Mountain', 2),
    ('Acadia', 'Everglades', 5),
    ('Sequoia and Kings Canyon', 'Badlands', 3),
    ('Bryce Canyon', 'Cuyahoga Valley', 6),
    ('Yellowstone', 'Death Valley', 2),
    ('Everglades', 'Badlands', 6),
    ('Rocky Mountain', 'Joshua Tree', 2),
    ('Mount Rainier', 'Lassen Volcanic', 1),
    ('Sequoia and Kings Canyon', 'Lassen Volcanic', 1),
    ('Great Smoky Mountains', 'Death Valley', 7),
    ('Acadia', 'Mount Rainier', 9),
    ('Yellowstone', 'Everglades', 8),
    ('Joshua Tree', 'Lassen Volcanic', 2),
    ('Great Smoky Mountains', 'Everglades', 3),
    ('Yellowstone', 'Lassen Volcanic', 2),
    ('Glacier', 'Mount Rainier', 1),
    ('Everglades', 'Shenandoah', 3),
    ('Olympic', 'Everglades', 10),
    ('Glacier', 'Shenandoah', 7)
]

park_graph.add_weighted_edges_from(park_list)

def main():
    start_point = input("Enter the start point: ")
    end_point = input("Enter the end point: ")
    dijkstra(park_graph, start_point, end_point)
    astar(park_graph, start_point, end_point)
    bfs(park_graph, start_point)

if __name__ == "__main__":
    main()
