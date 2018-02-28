#include <iostream>
#include <ctime>
int main() {
  unsigned t0, t1;

  //como ejemplo se usa una matriz 5x5


 // int n=2;
  for(int n=2; n<10; n++){
      t0=clock();
  //int n=5;
  int matriz[n][n];
  int sum;
  //llena la matriz con 1 en todas las posiciones por facilidad
  for(int i=0; i<n; i++){
    for(int j=0; j<n; j++){
      matriz[i][j]=1;
    }
  }
  //suma las posiciones unicamente que corresponden a la triangular superior
    for(int i=0; i<n; i++){
    for(int j=0; j<n; j++){
      sum+=matriz[i][j];
      j++;
    }
  }
  std::cout<<"valor suma: "<<sum<< std::endl;;
  t1 = clock();
  double time = (double(t1-t0)/CLOCKS_PER_SEC);
  std::cout << "Tiempo ejecucion: " << time << std::endl;
    for(int i=0; i<n; i++){
    for(int j=0; j<n; j++){
      matriz[i][j]=0;
    }
  }
  }
}

 
