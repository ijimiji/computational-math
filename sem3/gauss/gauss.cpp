#include <iostream>
#include <vector>


using namespace std;
typedef vector<vector<double>> Matrix;

Matrix randomMatrix(int n){
    Matrix matrix(n, vector<double>(n));
    for (auto &row : matrix){
        for(auto &element : row){
            element = rand() % 200 - 100;
        }
    }
    return matrix;
}

void printMatrix(const Matrix &matrix){
    for (auto &row : matrix){
        for(auto &element : row){
            cout << element << " ";
        }
        cout << endl;
    }
}

void swapRows(Matrix &matrix, int from, int to){
  std::swap(matrix[from], matrix[to]);
}

int main(){
    auto A = randomMatrix(3);
    printMatrix(A);
    swapRows(A, 0, 3);
    printMatrix(A);
    return 0;
}