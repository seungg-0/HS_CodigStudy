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


using loc = pair<int, int>;
auto check_value = [](int val) -> bool {
    return 0 <= val && val < board_size;
  };
auto in_boundary = 
[](const loc& l1, const loc& l2) -> bool {
  return check_value(l1.first) && check_value(l1.second) &&
          check_value(l2.first) && check_value(l2.second);
};
set<loc> diagonal(const loc& l) {
  set<loc> x;
  int row = 0;
  int col = l.second + l.first;
  while (col) {
    x.insert(make_pair(row++, col--));
  }
  return x;
}
auto horizontal = [](const loc& l) -> set<loc> {
  set<loc> x;
  int col = board_size - 1;
  while (col) {
    x.insert(make_pair(l.first, col--));
  }
  return x;
};
auto vertical = [](const loc& l) -> set<loc> {
  set<loc> x;
  int row = board_size - 1;
  while (row) {
    x.insert(make_pair(row--, l.second));
  }
  return x;
};

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

bool validate_king(const loc& l1, const loc& l2) {
  if (abs(l1.first - l2.first) > 1 || abs(l1.second - l2.second) > 1) {
    return false;
  }
  return true;
}
bool validate_queen(const loc& l1, const loc& l2) {
  //type : set<loc>
  auto s1 = horizontal(l1);
  auto s2 = vertical(l1);
  auto s3 = diagonal(l1);
  s1.insert(s2.begin(), s2.end());
  s1.insert(s3.begin(), s3.end());
  return s1.find(l2) != s1.end();
}

// compare the input move and actual piece movability
bool validate_move(int turn, const loc& l1, const loc& l2) {
  
  const auto& current_val = board[l1.first][l1.second];

  // empty area
  if (!current_val.has_value())
    return false;
  // even turn = black's turn
  if (turn % 2 == 0) {
    if (current_val.value().first == Color::white)
      return false;
  } else {
    // odd turn = white's turn
    if (current_val.value().first == Color::black)
      return false;
  }

  // location should be in board
  if (!in_boundary(l1, l2)) {
    return false;
  }
  // remain same area is false
  if (l1.first == l2.first && l1.second == l2.second) {
    return false;
  }

  const auto &current_ptype = current_val.value().second;
  if (current_ptype == ptype::King) {
    return validate_king(l1, l2);
  } else if (current_ptype == ptype::Queen) {
    return validate_queen(l1, l2);
  } else {
    return false;
  }
}

// 1. move piece
// 2. check king's status (to see who wins)
bool process_move(const loc& l1, const loc& l2) {
  auto dest_val = board[l2.first][l2.second];
  if (dest_val.value().second == ptype::King) {
    cout << to_string(dest_val.value().first) << " wins!\n";
    return true;
  }
  board[l2.first][l2.second] = board[l1.first][l1.second];
  board[l1.first][l1.second] = nullopt;
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
  auto l1 = make_pair(row1, col1);
  auto l2 = make_pair(row2, col2);
  if (!validate_move(turn, l1, l2)) {
    cout << "Invalid input. Please reinput command.\n";
  } else {
    if (process_move(l1, l2))
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
  // init_board();
  // play(1);
  return 0;
}
