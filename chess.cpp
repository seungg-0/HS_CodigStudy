#include <bits/stdc++.h>
using namespace std;


enum class Color {
  black, white
};
string to_string(const Color& c) {
  if (c == Color::black)
    return "b";
  return "w";
}
enum class ptype {
  None, King, Queen
};
string to_string(const ptype& p) {
  switch (p) {
    case ptype::King:
      return "K";
    case ptype::Queen:
      return "Q";
    default:
      return "?";
  }
}

using Piece = optional<pair<Color, ptype>>;

string to_string(const Piece& p) {
  if (!p.has_value())
    return "";
  return to_string(p.value().first) + to_string(p.value().second);
}

ostream& operator<<(ostream& os, const Piece& p) {
  os << to_string(p);
  return os;
}
const int board_size = 8;
Piece board[board_size][board_size];
void init_board() {
  board[0][0] = make_pair(Color::white, ptype::King);
  board[board_size - 1][board_size - 1] = make_pair(Color::black, ptype::King);
}




void print_board() {
  for (int i = 0; i < board_size; ++i) {
    cout << to_string(i + 1) + "\t";
    for (int j = 0; j < board_size; ++j) {
      cout << board[i][j] << "\t";
    }
    cout << endl << endl;
  }
  cout << "\t";
  for (int i = 0; i < board_size; ++i) {
    cout << static_cast<char>('a' + i) << "\t";
  }
  cout << endl;
}


// For now, only king exists.
bool validate_move(int turn, int col1, int row1, int col2, int row2) {
  auto check_value = [](int val) -> bool {
    return 0 <= val && val < board_size;
  };
  auto check_boundary = 
    [&check_value](int col1, int row1, int col2, int row2) -> bool {
    return check_value(col1) && check_value(row1) &&
            check_value(col2) && check_value(row2);
  };
  auto current_val = board[row1][col1];

  // even turn = black's turn
  if (turn % 2 == 0) {
    if (current_val != 'B')
      return false;
  } else {
    // odd turn = white's turn
    if (current_val != 'W')
      return false;
  }
  if (!check_boundary(col1, row1, col2, row2)) {
    return false;
  }
  if (col1 == col2 && row1 == row2) {
    return false;
  }
  if (abs(col1 - col2) > 1 || abs(row1 - row2) > 1) {
    return false;
  }
  return true;
}

// 1. validate move
// 2. check king's status (to see who win the game)
bool process_move(int col1, int row1, int col2, int row2) {
  if (board[row2][col2] == 'B') {
    cout << "White win!\n";
    return true;
  }
  if (board[row2][col2] == 'W') {
    cout << "Black win!\n";
    return true;
  }
  board[row2][col2] = board[row1][col1];
  board[row1][col1] = '-';
  return false;
}
void play(int turn) {
  cout << "turn " << turn << endl;
  cout << "press q to quit" << endl;
  cout << "input example : a1 b1" << endl;
  print_board();
  string input1{}, input2;
  cin >> input1;
  if (input1[0] == 'q')
    return;
  cin >> input2;
  int col1 = input1[0] - 'a';
  int row1 = input1[1] - '1';
  int col2 = input2[0] - 'a';
  int row2 = input2[1] - '1';
  if (!validate_move(turn, col1, row1, col2, row2)) {
    cout << "Invalid input. Please reinput command.\n";
  } else {
    if (process_move(col1, row1, col2, row2))
      return;
    turn += 1;
  }
  return play(turn);
}
extern "C" {
  void play_chess() {
    init_board();
    play(1);
  }
}
int main() {
  init_board();
  play(1);
  return 0;
}
