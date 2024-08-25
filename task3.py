import streamlit as st
import math

# Function to display the board with styled buttons and lines between boxes
def display_board(board, disabled=False):
    """Displays the Tic-Tac-Toe board with styled buttons and lines between boxes."""
    st.markdown("<h2 style='text-align: center;'>Tic-Tac-Toe</h2>", unsafe_allow_html=True)
    
    # Grid styling
    cols = st.columns(3)
    for i in range(3):
        row_buttons = []
        for j in range(3):
            idx = i * 3 + j
            if board[idx] == ' ':
                button_text = ''
            else:
                button_text = board[idx]
                
            # Button styling
            button_style = f"background-color: {'#' if board[idx] == ' ' else '#d0d0d0'}; border-radius: 10px; font-size: 24px; width: 100px; height: 100px;"

            # Button display
            button = cols[j].button(
                button_text,
                key=idx,
                disabled=disabled or board[idx] != ' ',
                on_click=make_move,
                args=(idx,),
                help=f"Position {idx + 1}",
                use_container_width=True
            )
            row_buttons.append(button)
        

# Function to check if there's a winner or the game is a draw
def check_winner(board):
    winning_combinations = [
        (0, 1, 2),  # rows
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # columns
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # diagonals
        (2, 4, 6)
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None

# Function to get a list of available moves on the board
def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)
    if result == st.session_state.ai:
        return 1
    elif result == st.session_state.human:
        return -1
    elif result == 'Draw':
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = st.session_state.ai
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = st.session_state.human
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Function to determine the best move for the AI
def best_move(board):
    best_val = -math.inf
    move = -1
    for m in get_available_moves(board):
        board[m] = st.session_state.ai
        move_val = minimax(board, 0, False, -math.inf, math.inf)
        board[m] = ' '
        if move_val > best_val:
            best_val = move_val
            move = m
    return move

# Function to handle human move
def make_move(idx):
    if st.session_state.board[idx] == ' ':
        st.session_state.board[idx] = st.session_state.human
        st.session_state.player_turn = st.session_state.ai
        result = check_winner(st.session_state.board)
        if result:
            st.session_state.game_over = True
            st.session_state.result = result
        else:
            ai_turn()

# Function for AI's move
def ai_turn():
    if not st.session_state.game_over:
        ai_move = best_move(st.session_state.board)
        st.session_state.board[ai_move] = st.session_state.ai
        st.session_state.player_turn = st.session_state.human
        result = check_winner(st.session_state.board)
        if result:
            st.session_state.game_over = True
            st.session_state.result = result

# Function to reset the game
def reset_game():
    st.session_state.board = [' ' for _ in range(9)]
    st.session_state.player_turn = st.session_state.human
    st.session_state.game_over = False
    st.session_state.result = None
    if st.session_state.ai == 'X':
        ai_turn()

# Function to start the game
def start_game():
    st.session_state.started = True
    reset_game()

# Function to show rules
def show_rules():
    st.write("""
    **Tic-Tac-Toe Rules:**
    
    1. The game is played on a grid that's 3 squares by 3 squares.
    2. You are 'X' or 'O'. Your opponent (the AI) is the other symbol.
    3. Players take turns putting their marks in empty squares.
    4. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
    5. If all 9 squares are full and no player has 3 marks in a row, the game ends in a draw.
    """)

# Main function for the Streamlit app
def main():
    st.title("Tic-Tac-Toe with AI")

    if 'started' not in st.session_state:
        st.session_state.started = False

    if not st.session_state.started:
        st.write("<h2 style='text-align: center;'>Welcome to Tic-Tac-Toe!</h2>", unsafe_allow_html=True)
        if st.button("Start Game"):
            st.session_state.human = st.radio("Choose your symbol:", ["X", "O"], index=1)
            st.session_state.ai = 'O' if st.session_state.human == 'X' else 'X'
            start_game()
        if st.button("Rules"):
            show_rules()
        st.stop()

    # Display the current game board
    display_board(st.session_state.board)

    if st.session_state.game_over:
        if st.session_state.result == st.session_state.human:
            st.success("Congratulations! You win!")
        elif st.session_state.result == st.session_state.ai:
            st.error("AI wins! Better luck next time.")
        else:
            st.info("It's a draw!")
        if st.button("Play Again"):
            reset_game()
        elif st.button("Exit"):
            st.write("Thank you for playing the game :)")
            st.stop()

if __name__ == "__main__":
    main()
