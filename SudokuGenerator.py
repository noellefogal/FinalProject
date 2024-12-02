#most of the methods

def valid_in_row(self,row,num):
  return num if not self.board[row]


def valid_in_col(self,col,num):
  for row in range(self.row_length):
    if self.board[row][col] == num:
      return False
  return True
