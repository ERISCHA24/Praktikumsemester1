#include <stdio.h> 
int main(){ 
    int stop; 
    scanf("%d", &stop);
    for (int i = 1; i <= stop; i += 2) printf("%d ", i); 
    printf("\n"); 
    for (int i = stop % 2 == 0 ? stop : stop - 1; i >= 2; i -= 2) printf("%d ", i); 
return 0; 
} 