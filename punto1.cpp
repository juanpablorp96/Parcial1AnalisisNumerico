#include <iostream>
#include <ctime>
//PUNTOS A,B
int main() {
  unsigned t0, t1;

  //para las pruebas se usan matrices desde 2x2 hasta 9x9


 
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
//PUNTO C
//la complejidad es O(n^2) ya que se manejan dos ciclos for para recorrer la matriz
 
