#import controller


class graph:
  def __init__(self):
      pass
  
  def Kosaraju(self, arr:list[list]):
      def dfs(n,  nodes, v, st):
          v[n] = True;
          for i in nodes[n]:
              if v[i]==False: dfs(i, nodes, v, st)
          st.append(n)
    
      def dfs2(n, nodes, v, com):
          v[n]=True
          com.append(n)
          for i in nodes[n]:
              if v[i]==False: dfs2(i,nodes,v,com)


      n = len(arr)
      inverse =[]
      for i in range(n): inverse.append([])
      for i in range(n):
          for j in arr[i]: inverse[j].append(i)

      v = [False] * n;
      stack = []
      for i in range(n): 
          if v[i]==False: dfs(i, arr,v, stack)
      for i in range(n): v[i]=False
      ans = []
      while stack:
          temp = stack.pop()
          if v[temp]: continue
          
          ans.append([])
          dfs2(temp, inverse, v, ans[-1])
      return ans

class Matrix_Operator:
    def __init__(self):
        pass

    def find_all_Paths(self, matrix):
        n = len(matrix)
        ans = [[False] * n for i in range(n)]
        nodes=[[]for  i in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j]: nodes[i].append(j)
        for i in range(n):
            v = [0]*n
            q = [i]
            v[i]=1
            while q:
                temp = q.pop(0)
                for e in nodes[temp]:
                    if v[e]==1: continue
                    q.append(e)
                    v[e]=1
            for j in range(n):
                ans[i][j] = v[j]
        return ans

    def sort_rows(self, matrix):
        n= len(matrix)
        ans = [[] for i in range(n)]
        for i in range(n):
            count =0
            for e in matrix[i]:
                if e == True: count+=1
            ans[i] = [-count, i, matrix[i]]
        ans.sort()
        return ans
    def sort_colums(self, matrix):
        n = len(matrix)
        newma  = [[]for i in range(n)]
        yaxis = [matrix[i][1] for i in range(n)]
        for i in range(n):
            local = []
            count=0
            for j in range(n):
                local.append(matrix[j][2][i])
            newma[i] = local
        realma = [[0]*n for i in range(n)]
        for i in range(n):
            v = yaxis[i]
            for j in range(n):
                realma[j][i]=newma[v][j]
        for a in realma: print(a)
        return [yaxis, realma]

            
    def find_components(self, matrix, y_axis):
        n = len(matrix)
        i = 0
        ans = []

        while i<n:
            comp = [y_axis[i]]
            if i==n-1: 
                ans.append(comp)
                break
            for j in range(1, n-i):
                g = True
                for k in range(j+1):
                    g&= matrix[i+j][i+k]
                for k in range(j+1):
                    g&= matrix[i+k][i+j]
                if g==False: break
                comp.append(y_axis[i+j])
            ans.append(comp)
            i+=len(comp)
        return ans



def main():
    matrix= [
            [1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1]
            ]
    paths = Matrix_Operator().find_all_Paths(matrix)
    for a in paths: print(a)
    sor =  Matrix_Operator().sort_rows(paths)
    for a in sor: print(a)
    yaxis, ma = Matrix_Operator().sort_colums(sor)
    ans = Matrix_Operator().find_components(ma, yaxis)
    print(ans)



main()

    

