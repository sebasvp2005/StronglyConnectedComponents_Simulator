import graph

def get_strongly_connectec_components(nodes: list[list])->list[list]:
  return graph.graph().Kosaraju(nodes)

def get_Matrix_paths(matrix):
    return Matrix_Operator().find_all_Paths(matrix)

def get_sort_rows(matrix):
    return Matrix_Operator().sort_rows(matrix)

def get_sort_columns(ordered_matrix):
    return Matrix_Operator().sort_colums(ordered_matrix)

def get_Matrix_components(yaxis, matrix):
    return Matrix_Operator().find_components(matrix, yaxis)

