#include <iostream>
#include <iterator>
#include <vector>


using namespace std;
typedef vector<vector<double>> Matrix;

vector<double> operator+(const vector<double> &a, const vector<double>& b){
    vector<double> v;
    for (int i = 0; i < a.size(); i++){
        v[i] = a[i] +b[i];
    }
    return v;
}

vector<double> operator*(double alpha, const vector<double> &a){
    vector<double> v;
    for (int i = 0; i < a.size(); i++){
        v[i] = a[i] * alpha;
    }
    return v;
}

Matrix randomMatrix(int n){
    Matrix matrix(n, vector<double>(n));
    for (auto &row : matrix){
        for(auto &element : row){
            element = rand() % 200 - 100;
        }
    }
    return matrix;
}
Matrix hilbertMatrix(int n){
    Matrix matrix(n, vector<double>(n));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            matrix[i][j] = 1.0 / (i+1+j);
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

int indMaxElementInColumn(Matrix &matrix, int column, int start){
    int pos = start;
    for (int i = start; i < matrix.size(); i++){
        if (matrix[i][column] > matrix[pos][column]){
            pos = i;
        }
    }
    return pos;
}

Matrix straightMove(Matrix A, vector<double> b){
    
    // int n = A.size();
    // for (int i = 0; i < n; i++){
    //     for (int j = n - i; j < n; j++){

    //     }
    // }
}

Matrix reverseMove(Matrix A, vector<double> b){
    int n = A.size();
    for (int i = n - 1 ; i >= 0; i--){

    }
}

int main(){
    auto A = randomMatrix(3);
    Matrix B = copy(A.begin(), A.)

    auto H = hilbertMatrix(4);
    printMatrix(H);
    return 0;
}