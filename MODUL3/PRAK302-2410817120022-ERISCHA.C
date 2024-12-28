#include <stdio.h> 
int main() { 
    float nilai; 
    printf("Masukkan nilai (0-100): "); 
    scanf("%f", &nilai); 
    if (nilai >= 80 && nilai <= 100) { 
        printf("A"); 
    } else if (nilai >= 70 && nilai < 80) { 
        printf("B"); 
    } else if (nilai >= 60 && nilai < 70) { 
        printf("C"); 
    } else if (nilai >= 50 && nilai < 60) { 
        printf ("D"); 
    } else if (nilai >= 0 && nilai < 50) { 
        printf("E"); 
    } else { 
        printf("Tidak Valid"); 
    } 
    return 0; 
} 