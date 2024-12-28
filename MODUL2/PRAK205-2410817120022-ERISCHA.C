#include <stdio.h>
#include <math.h>
int main(){
    float A, B, C, keliling, Luas;
    printf("nilai A: ");
    scanf("%f", &A);
    printf("nilai B: ");
    scanf("%f", &B);
 C = sqrt(B * B - A * A);
 keliling = A + B + C;
 Luas = (A * C) / 2;
printf("Alas = %d cm\n", (int)C);
printf("Tinggi = %d cm\n", (int)A);
printf("Keliling = %d cm\n", (int)keliling);
printf("Luas : %d cm^2\n", (int)Luas);
return 0;
}