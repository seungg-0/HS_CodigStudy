#include <bits/stdc++.h>
using namespace std;

const int board_size = 8;
char board[board_size][board_size];
void init_board() {
  for (int i = 0; i < board_size; ++i) {
    for (int j = 0; j < board_size; ++j) {
      board[i][j] = '-';
    }
  }
  board[0][0] = 'W';
  board[board_size - 1][board_size - 1] = 'B';
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


void process_move(const string& input1, const string& input2) {
  // e.g : a3 b3
  int col_1 = input1[0] - 'a';
  int row_1 = input1[1] - '1';
  int col_2 = input2[0] - 'a';
  int row_2 = input2[1] - '1';
  // cout << "before test" << endl;
  // cout << col_1 << endl;
  // cout << row_1 << endl;
  // cout << col_2 << endl;
  // cout << row_2 << endl;
  // cout << "after test" << endl;
  board[row_2][col_2] = board[row_1][col_1];
  board[row_1][col_1] = '-';
}
void play() {
  cout << "press q to quit" << endl;
  cout << "input example : a1 b1" << endl;
  print_board();
  string input1{}, input2;
  cin >> input1;
  if (input1[0] == 'q')
    return;
  cin >> input2;
  process_move(input1, input2);
  return play();
}
int main() {
  init_board();
  play();
  return 0;
}
