#include <iostream>
#include <optional>
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
  King, Queen
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
    return "-";
  return to_string(p.value().first) + to_string(p.value().second);
}

std::ostream& operator<<(std::ostream& os, const Piece& p) {
  os << to_string(p);
  return os;
}
const int board_size{8};
using loc = pair<int, int>;
loc left(const loc& l) {
  return loc(l.first, l.second - 1);
}
loc right(const loc& l) {
  return loc(l.first, l.second + 1);
}
loc up(const loc& l) {
  return loc(l.first - 1, l.second);
}
loc down(const loc& l) {
  return loc(l.first + 1, l.second);
}
class Board {
  public:
    Piece get_val(const loc& l) const {
      return board[l.first][l.second];
    }
    bool set_val(const loc& l, const Piece& p) {
      board[l.first][l.second] = p;
      return true;
    }
    void print() {
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
  private:
    Piece board[board_size][board_size];
};
void init_board(Board& board) {
  auto wk = make_pair(Color::white, ptype::King);
  auto bk = make_pair(Color::black, ptype::King);
  auto wq = make_pair(Color::white, ptype::Queen);
  auto bq = make_pair(Color::black, ptype::Queen);
  board.set_val(make_pair(0, 0),wk);
  board.set_val(make_pair(0, 1),wq);
  board.set_val(make_pair(board_size - 1, board_size - 1),bk);
  board.set_val(make_pair(board_size - 1, board_size - 2),bq);
}
auto check_value = [](const int& val) -> bool {
    return 0 <= val && val < board_size;
  };
auto in_boundary = [](const loc& l) -> bool {
  return check_value(l.first) && check_value(l.second);
};

bool visit[board_size][board_size];
void init_visit() {
  for (size_t i = 0; i < board_size; ++i) {
    for (size_t j = 0; j < board_size; ++j) {
      visit[i][j] = false;
    }
  }
}
bool is_empty_slot(const Board& b, const loc& l) {
  return b.get_val(l) == nullopt;
}

bool queen_reachable(const Board& b, const loc& cur, const loc& dest) {
  if (!in_boundary(cur) || !is_empty_slot(b, cur) ||
      visit[cur.first][cur.second]) {
    return false;
  }
  if (cur == dest)
    return true;
  else {
    visit[cur.first][cur.second] = true;
    //left, right, up, down, leftup, leftdown, rightup, rightdown
    return queen_reachable(b, left(cur), dest) ||
          queen_reachable(b, right(cur), dest) ||
          queen_reachable(b, up(cur), dest) || 
          queen_reachable(b, down(cur), dest) ||
          queen_reachable(b, up(left(cur)), dest) ||
          queen_reachable(b, up(right(cur)), dest) ||
          queen_reachable(b, down(left(cur)), dest) ||
          queen_reachable(b, down(right(cur)), dest);
  }
}
bool king_reachable(const Board& b, const loc& cur, const loc& dest) {
  return abs(cur.first - dest.first) <= 1 &&
        abs(cur.second - dest.second) <= 1;
}
bool reachable(const Board& b, const loc& l1, const loc& l2) {
  init_visit();
  auto p = b.get_val(l1);
  const auto& piece_type = p.value().second;
  if (piece_type == ptype::Queen) {
    return queen_reachable(b, l1, l2);
  } else if (piece_type == ptype::King) {
    return king_reachable(b, l1, l2);
  } else {
    return false;
  }
}

void print_menu(const int& turn) {
  cout << "turn " << turn << endl;
  cout << "press q to quit" << endl;
  cout << "input example : a1 b1" << endl;
}
string to_string(const loc& l) {
  return "[" + to_string(l.first) + "][" + to_string(l.second) + "]";
}
// check if input is valid
// 1. l1 & l2 should be in boundary
// 2. turn & piece color should be matched.
bool validate_input(const Board& b, int turn, const loc& l1, const loc& l2) {
  // location should be in board boundary
  if (!in_boundary(l1) || !in_boundary(l2)) {
    cout << "boundary error\n";
    cout << to_string(l1) << ", " << to_string(l2) << endl;
    return false;
  }
  // remain same area is false
  if (l1 == l2) {
    cout << "same area error\n";
    return false;
  }

  const auto& current_val = b.get_val(l1);

  // empty area
  if (!current_val.has_value()) {
    cout << "empty area error\n";
    return false;
  }
  // even turn = black's turn
  if (turn % 2 == 0) {
    if (current_val.value().first == Color::white) {
      cout << "turn error\n";
      return false;
    }
  } else {
    // odd turn = white's turn
    if (current_val.value().first == Color::black) {
      cout << "turn error\n";
      return false;
    }
  }
  return true;
}
bool process_move(Board& b, const loc& l1, const loc& l2) {
  init_visit();
  auto p1 = b.get_val(l1);
  auto p2 = b.get_val(l2);
  if (p2.has_value() && p2.value().second == ptype::King) {
    cout << to_string(p1.value().first) << " wins!\n";
    return true;
  }
  b.set_val(l2, b.get_val(l1).value());
  b.set_val(l1, nullopt);
  return false;
}
void play(Board& b, int turn) {
  // print in every turn
  print_menu(turn);
  b.print();

  // input
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
  if (!validate_input(b, turn, l1, l2)) {
    cout << "Invalid input. Please reinput command.\n";
  } else {
    if (process_move(b, l1, l2))
      return;
    turn += 1;
  }
  return play(b, turn);
}
int main() {
  Board b{};
  init_board(b);
  play(b, 1);
}
