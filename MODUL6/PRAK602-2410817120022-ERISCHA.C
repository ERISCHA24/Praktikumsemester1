#include <stdio.h>
int main() {
    int Ruangan;
    scanf("%d", &Ruangan);
    int zetsuPutih[Ruangan];
    for (int i = 0; i < Ruangan; i++) {
        scanf("%d", &zetsuPutih[i]);
    }
    for (int i = 0; i < Ruangan; i++) {
        printf("%d ", zetsuPutih[i] * (i + 1));
    }
return 0;
}