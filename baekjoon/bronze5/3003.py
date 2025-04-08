king, queen, rook, bishop, knight, pawn = tuple(map(int, input().split(sep=' ')))

answer_king, answer_queen, answer_rook, answer_bishop, answer_knight, answer_pawn = 1, 1, 2, 2, 2, 8

print(answer_king - king, answer_queen - queen, answer_rook - rook, answer_bishop - bishop, answer_knight - knight, answer_pawn - pawn)