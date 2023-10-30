import graph

def get_strongly_connectec_components(nodes: list[list])->list[list]:
  return graph.graph().Kosaraju(nodes)

def get_Matrix_paths(matrix):
    return graph.Matrix_Operator().find_all_Paths(matrix)

def get_sort_rows(matrix):
    return graph.Matrix_Operator().sort_rows(matrix)

def get_sort_columns(ordered_matrix, yaxis):
    return graph.Matrix_Operator().sort_colums(ordered_matrix, yaxis)

def get_Matrix_components(yaxis, matrix):
    return graph.Matrix_Operator().find_components(matrix, yaxis)

