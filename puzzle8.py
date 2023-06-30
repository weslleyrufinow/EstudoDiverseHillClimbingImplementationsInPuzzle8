import random
import copy

class Puzzle8:
    def __init__(self, board=None): #Construtor. Se não receber argumento, gera tabuleiro aleatório
        if board is None:
            self.board = self.generate_random_board()
        else:
            self.board = board

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(str(num) for num in row) + "\n"
        return board_str

    def deepcopy(self): # Faz uma copia profunda
        return copy.deepcopy(self)

    def generate_random_board(self): #Gera tabuleiros aleatórios
        numbers = list(range(0, 9))  
        random.shuffle(numbers)     
        board = [numbers[i:i+3] for i in range(0, 9, 3)]  
        return board

    def is_goal_state(self): #Verifica se é o estado ideal
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal_state

    def evaluate(self): # Avalia o estado atual do tabuleiro em relação ao estado ideal.
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != goal_state[i][j]:
                    count += 1
        return count #Retorna o número de peças fora do lugar

    def swap_tiles(self, row1, col1, row2, col2): #Trocar as posições de duas peças no tabuleiro
        self.board[row1][col1], self.board[row2][col2] = self.board[row2][col2], self.board[row1][col1]

    def get_blank_position(self): #Encontra a posição do espaço vazio no tabuleiro                        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j #Retorna a posição do espaço vazio
        return None

    def is_valid_move(self, row, col): #Verifica se um movimento para uma posição (linha, coluna) é válido
        return (0 <= row < 3 and 0 <= col < 3) #Retorna True se o movimento for válido, False caso não seja
   