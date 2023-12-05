print("Hello")
def legal_moves(position):
    column = position[0]
    row = int(position[1])
    
    # Tạo danh sách các ô mà quân hậu có thể di chuyển tới
    moves = []
    
    # Di chuyển theo hàng ngang
    for c in 'abcdefgh':
        if c != column:
            moves.append(c + str(row))
    
    # Di chuyển theo hàng dọc
    for r in range(1, 9):
        if r != row:
            moves.append(column + str(r))
    
    # Di chuyển theo đường chéo chính
    diff = min(row - 1, ord(column) - ord('a'))
    for i in range(1, diff + 1):
        moves.append(chr(ord(column) - i) + str(row - i))
    
    diff = min(8 - row, ord('h') - ord(column))
    for i in range(1, diff + 1):
        moves.append(chr(ord(column) + i) + str(row + i))
    
    # Di chuyển theo đường chéo phụ
    diff = min(row - 1, ord('h') - ord(column))
    for i in range(1, diff + 1):
        moves.append(chr(ord(column) + i) + str(row - i))
    
    diff = min(8 - row, ord(column) - ord('a'))
    for i in range(1, diff + 1):
        moves.append(chr(ord(column) - i) + str(row + i))
    
    return moves

position = input("Nhập vào vị trí của quân hậu (ví dụ: a8): ")
moves = legal_moves(position)
print("Các ô mà quân hậu có thể di chuyển tới là:", moves)
